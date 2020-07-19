# -*- coding: utf-8 -*-
import scrapy


class CountrySpider(scrapy.Spider):
    name = 'country'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        title = response.xpath("//div[@class='col-md-12']/h1/text()").get()
        countries = response.xpath("//td/a/text()").getall()

        yield {
            'title': title,
            'countries': countries
        }
