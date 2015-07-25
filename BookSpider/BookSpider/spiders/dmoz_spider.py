
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from _cffi_backend import string
from encodings.utf_8 import decode
from tokenize import String
import scrapy
from scrapy.http import Request
from BookSpider.items import BookspiderItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["salttiger.com"]
    start_urls = [
        "http://www.salttiger.com/category/ebooks/"
    ]

    def parse(self, response):
            item = BookspiderItem()

            title = response.xpath(".//*/header/h1/a/text()").extract()
            item['title'] =[t.encode('utf-8') for t in title]
            url = response.xpath(".//*/header/h1/a/@href").extract()
            item['url'] = [t.encode('utf-8') for t in url]
            image = response.xpath(".//*/div/p[1]/img/@src").extract()
            item['image'] = [t.encode('utf-8') for t in image]

            for t in title:
                print(t.encode('utf-8'))

            yield item
            urls = response.xpath(".//*[@id='nav-below']/div/a[@class='page larger']/@href").extract()
            for ul in urls:
                print (urls)
                yield Request(ul, callback=self.parse)
