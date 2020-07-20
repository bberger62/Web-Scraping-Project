from scrapy import Spider, Request
from opentable.items import OpentableItem
import re
import math


class OpentableSpider(Spider):
    name = 'opentable_spider'
    allowed_urls = 'https://www.opentable.com/'
    start_urls = 'https://www.opentable.com/lolz-view-all/H4sIAAAAAAAAAKtWMlKyUjIyMDLQNTDXNbQIMbS0MrG0MjBQ0lEyRpEBCpgABYDyxgYQeVMlKyMdJTOgoImBnrmJpYmhpY6uubGepYWpqaUxUIEFUCrANSjY38_RxzPKNSg-MNQ1KBIoYQmUUHYsS8zMSUzKSXXLL3LJzMtLLfLLLwdKGgLtjY6tBQC3ifQKmgAAAA==?originid=1f4c4203-db0e-4172-88e6-f0c35289c50d&corrid=41ddff54-b9d7-46a4-828d-241ac04ab86b&page=1'

    url_list = [f'https://www.opentable.com/lolz-view-all/H4sIAAAAAAAAAKtWMlKyUjIyMDLQNTDXNbQIMbS0MrG0MjBQ0lEyRpEBCpgABYDyxgYQeVMlKyMdJTOgoImBnrmJpYmhpY6uubGepYWpqaUxUIEFUCrANSjY38_RxzPKNSg-MNQ1KBIoYQmUUHYsS8zMSUzKSXXLL3LJzMtLLfLLLwdKGgLtjY6tBQC3ifQKmgAAAA==?originid=1f4c4203-db0e-4172-88e6-f0c35289c50d&corrid=41ddff54-b9d7-46a4-828d-241ac04ab86b&page={i+1}' for i in  total_pages]            


    def page_parse(self, response):

        total_pages = int(response.xpath('//li[@class="_3Y_18dirxSlbwfPU0nr-t_"]/a/text()').extract()[2])
        total_rest = 3395
        rest_per_page = 30

        rest_name = response.xpath('//div[@class="_1liK37RaUN7lnBs9g1TPyp"]/div/a/h6/text()').extract()[1::2]

        rating = response.xpath('//div[@class="_25xMNiLip-SZ1zuCkSA7ge"]/div/text()').extract() ####take a look at these

        num_reviews = response.xpath('//div[@class="_23JVvFevCvj_mutWbEzTgU"]/a/text()').extract()[1::3]

        expensive = response.xpath('//div[@class="_1Y-E7ZnLMoyE5mrwg00NBj"]/span/text()').extract()

        genre = response.xpath('//div[@class="_2p0jcmKJSDjEh-wNrLIpzJ"]/text()').extract()

        location = ^^^^#gotta find a way to split these

        booked_today = response.xpath('//span[@class="_3v-BAA6RD6_J0v34nZo2Qv"]/text()').extract() #need to extract number
        #also need to add something here to account for restaurants that have not been booked

        delivery_partners = response.xpath #what will we do with this?

        for url in url_list:
            yield Request(url=url, callback=self.)### i dont think i need this



        item['rest_name'] = rest_name
        item['rating'] = rating
        item['num_reviews'] = num_reviews
        item['expensive'] = expensive
        item['genre'] = genre
        item['location'] = location
        item['booked_today'] = booked_today  
        item['delivery_partners'] = delivery_partners



