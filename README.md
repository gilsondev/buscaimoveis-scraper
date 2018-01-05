# Busca Imóveis Scraper

Projeto voltado para raspagem de anúncios de imóveis a venda nas plataformas conhecidas como por exemplo OLX e ZAP Imóveis.

## Instalação

1. Faça o checkout do projeto:

```shell
$ git clone https://github.com/gilsondev/buscaimoveis-scraper.git
```

2. Crie o ambiente virtual e instale as dependências:

```shell
$ cd buscaimoveis-scraper
$ python3 -m venv .venv
```

```shell
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

3. Rode o spider desejado. Nesse exemplo irei buscar vendas na OLX.

```shell
$ scrapy crawl olx
```

OBS.: Por enquanto é raspado vendas de imóveis no Distrito Federal somente, mas em breve estará flexível para outros estados.

Os dados coletados segue a estrutura de exemplo abaixo:

```json
{
  "_id": "<id do documento>",
  "url": "http://df.olx.com.br/distrito-federal-e-regiao/imoveis/setor-total-ville-433892765",
  "type": "Venda - apartamento padrão",
  "tax": "R$ 100,00",
  "garage": 1,
  "price": " R$ 97.000,00",
  "created_at": "ISODate('2018-01-04T16:56:42.669Z')",
  "rooms": 2,
  "posted_at": "4 Janeiro às 16:15",
  "image": "http://img.olx.com.br/images/35/357804005117894.jpg",
  "district": "Santa Maria",
  "cep": "72505-222",
  "area": "",
  "title": "Setor Total Ville",
  "description": "Descrição do anúncio",
  "owner": "Nome do Dono do imóvel"
  "city": "Brasília",
  "phone": "(61) 99999-9999"
}
```

## Como Contribuir
Veja mais no arquivo `CONTRIBUTING.md`, as formas de ajudar com o projeto, e o `AUTHORS.md` para saber quem estão a frente e que pode te auxiliar.
