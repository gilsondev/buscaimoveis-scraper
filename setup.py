# Automatically created by: shub deploy

from setuptools import setup, find_packages

setup(
    name         = 'buscaimoveis-scraper',
    version      = '1.0',
    packages     = find_packages(),
    entry_points = {'scrapy': ['settings = buscaimoveis.settings']},
)
