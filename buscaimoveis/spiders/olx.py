import logging
import datetime

from scrapy import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from buscaimoveis.items import PropertyItem


class OLXSpider(CrawlSpider):
    name = "olx"
    allowed_domains = ["df.olx.com.br"]
    start_urls = ["http://df.olx.com.br/imoveis/venda"]
    rules = [
        Rule(
            LinkExtractor(allow=r'\?o=2'),
            callback='parse_item',
            follow=True
        )
    ]

    def parse_start_url(self, response):
        return self.parse_property_list(response)

    def parse_item(self, response):
        return self.parse_property_list(response)

    def parse_property_list(self, response):
        properties_links = response.xpath(
            u'//*[@id="main-ad-list"]/li[@class="item"]/a/@href'
        ).extract()

        for property_link in properties_links:
            yield Request(property_link, callback=self.parse_property)

    def parse_property(self, response):
        item = PropertyItem()
        item['source'] = 'OLX'

        owner = response.xpath(u'//*[@class="item owner mb10px "]/p/text()')

        if owner:
            item['title'] = response.xpath(
                u'//*[@id="ad_title"]/text()'
            ).extract_first().strip()

            posted_at = response.xpath(
                u'//*[@class="OLXad-date mb5px"]/p/text()'
            ).re_first(r'\d.[\w|\s].+')
            item['posted_at'] = posted_at

            item['created_at'] = datetime.datetime.now()

            item['url'] = response.url

            item['price'] = response.xpath(
                u'//*[@class="OLXad-price-box"]/span/text()'
            ).extract_first()

            item['owner'] = owner.extract_first().strip()

            description = response.xpath(
                u'//*[@class="OLXad-description mb30px"]/p/text()'
            ).extract()
            description = [p.strip() for p in description]
            item['description'] = " ".join(description)

            item['image'] = response.xpath(
                u'//*[@class="module_OLXad-photo"]/'
                u'div[@class="OLXad-photo-main"]/div/img/@src'
            ).extract_first()

            item['property_type'] = response.xpath(
                u'//*[@class="OLXad-details mb30px"]/div/ul/li/p/'
                u'span[text() = "Tipo:"]/following-sibling::strong/text()'
            ).extract_first()

            item['tax'] = response.xpath(
                u'//*[@class="OLXad-details mb30px"]/div/ul/li/p/'
                u'span[text() = "Condomínio:"]/following-sibling::strong/text()'
            ).extract_first()

            area = response.xpath(
                u'//*[@class="OLXad-details mb30px"]/div/ul/li/p/'
                u'span[text() = "Área construída:"]/'
                u'following-sibling::strong/text()'
            )
            item['area'] = area.extract_first(default='').strip()

            item['rooms'] = response.xpath(
                u'//*[@class="OLXad-details mb30px"]/div/ul/li/p/'
                u'span[text() = "Quartos:"]/'
                u'following-sibling::strong/text()'
            ).extract_first()

            item['garage'] = response.xpath(
                u'//*[@class="OLXad-details mb30px"]/div/ul/li/p/'
                u'span[text() = "Vagas na garagem:"]/'
                u'following-sibling::strong/text()'
            ).extract_first()

            item['city'] = response.xpath(
                u'//*[@class="OLXad-location mb20px"]/div/ul/li/p/'
                u'span[text() = "Município:"]/'
                u'following-sibling::strong/text()'
            ).extract_first()
            item['city'] = self._strip_data(item.get('city'))

            item['cep'] = response.xpath(
                u'//*[@class="OLXad-location mb20px"]/div/ul/li/p/'
                u'span[text() = "CEP do imóvel:"]/'
                u'following-sibling::strong/text()'
            ).extract_first()
            item['cep'] = self._strip_data(item.get('cep'))

            item['district'] = response.xpath(
                u'//*[@class="OLXad-location mb20px"]/div/ul/li/p/'
                u'span[text() = "Bairro:"]/'
                u'following-sibling::strong/text()'
            ).extract_first()
            item['district'] = self._strip_data(item.get('district'))

            yield item

    def _strip_data(self, value):
        if hasattr(value, 'strip'):
            value = value.strip()
        return value
