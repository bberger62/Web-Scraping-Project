from scrapy import Spider, Request
from opentable.items import OpentableItem
import re
import math


class OpentableSpider(Spider):
    name = 'opentable_spider'
    allowed_urls = 'https://www.opentable.com/'
    start_urls = 'https://www.opentable.com/s/?covers=2&currentview=list&datetime=2020-07-31+18%3A30&from=0&metroid=8&regionids=16&size=100&sort=Popularity'

    url_list = [f'https://www.opentable.com/s/?covers=2&currentview=list&datetime=2020-07-31+18%3A30&from={(i-1)*100}&metroid=8&regionids=16&size=100&sort=Popularity' for i in  total_pages]            


    def page_parse(self, response):

        total_pages = 13
        total_rest = 1300
        rest_per_page = 100

        # rest_name = response.xpath('//span[@class="rest-row-name-text"]/text()').extract()
        # rest_name = response.xpath('//div[@class="rest-row with-image "]/div/div/a/span/text()').extract()
        rest_name = response.xpath('//ul[@class="content-section-list infinite-results-list analytics-results-list"]/li/div/div/div/div/a/span/text()').extract()
        rest_name = response.xpath('//ul[@class="content-section-list infinite-results-list analytics-results-list"]/li//span[@class="rest-row-name-text"]/text()').extract()
        ^right
        

        # rating = response.xpath('//div[@class="rest-row-meta rest-row-meta-grid flex-row-justify"]/div/div//div/text()') #THIS ISNT WORKING
        rating = response.xpath('//ul[@class="content-section-list infinite-results-list analytics-results-list"]/li//div[@class="star-rating-score"]') #need to pull aria label
        ^not right


        num_reviews = response.xpath('//a[@class="review-link"]/span/text()').extract() #need to check this
        num_reviews = response.xpath('//ul[@class="content-section-list infinite-results-list analytics-results-list"]/li/div/div/div/div/div/a/span')
        ^not right



        expensive = response.xpath('//ul[@class="content-section-list infinite-results-list analytics-results-list"]/li//i[@class="pricing--the-price"]/text()').extract()
        kind of^

        genre = response.xpath('//ul[@class="content-section-list infinite-results-list analytics-results-list"]/li//span[@class="rest-row-meta--cuisine rest-row-meta-text sfx1388addContent"]/text()').extract()
        works^

        location = response.xpath('//ul[@class="content-section-list infinite-results-list analytics-results-list"]/li//span[@class="rest-row-meta--location rest-row-meta-text sfx1388addContent"]/text()').extract()
        works^

        booked_today = response.xpath('//ul[@class="content-section-list infinite-results-list analytics-results-list"]/li//div[@class="booking"]/text()').extract()
        ^not quite

        delivery_partners = response.xpath('//ul[@class="content-section-list infinite-results-list analytics-results-list"]/li//div[@class="booking"]/text()').extract()


        # total_pages = int(response.xpath('//li[@class="_3Y_18dirxSlbwfPU0nr-t_"]/a/text()').extract()[2])
        # total_rest = 3395
        # rest_per_page = 30

        # rest_name = response.xpath('//div[@class="_1liK37RaUN7lnBs9g1TPyp"]/div/a/h6/text()').extract()[1::2]

        # rating = response.xpath('//div[@class="_25xMNiLip-SZ1zuCkSA7ge"]/div/text()').extract() ####take a look at these

        # num_reviews = response.xpath('//div[@class="_23JVvFevCvj_mutWbEzTgU"]/a/text()').extract()[1::3]

        # expensive = response.xpath('//div[@class="_1Y-E7ZnLMoyE5mrwg00NBj"]/span/text()').extract()

        # genre = response.xpath('//div[@class="_2p0jcmKJSDjEh-wNrLIpzJ"]/text()').extract()

        # location = ^^^^#gotta find a way to split these

        # booked_today = response.xpath('//span[@class="_3v-BAA6RD6_J0v34nZo2Qv"]/text()').extract() #need to extract number
        # booked_today = int(re.findall(r'\d+', booked_today[0])[0])
        # for i in booked_today:
        #     list(int(re.findall(r'\d+', i)[0]))





        # #also need to add something here to account for restaurants that have not been booked

        # delivery_partners = response.xpath #what will we do with this?

        # for url in url_list:
        #     yield Request(url=url, callback=self.)### i dont think i need this


        item = OpentableItem()

        item['rest_name'] = rest_name
        item['rating'] = rating
        item['num_reviews'] = num_reviews
        item['expensive'] = expensive
        item['genre'] = genre
        item['location'] = location
        item['booked_today'] = booked_today  
        item['delivery_partners'] = delivery_partners





