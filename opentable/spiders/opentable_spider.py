from scrapy import Spider, Request
from opentable.items import OpentableItem
import re
import math


class OpentableSpider(Spider):
    name = 'opentable_spider'
    allowed_urls = ['https://www.opentable.com/']
    start_urls = ['https://www.opentable.com/s/?covers=2&currentview=list&datetime=2020-07-31+18%3A30&from=0&metroid=8&regionids=16&size=100&sort=Popularity']

    
    def parse(self, response):
        total_pages = 14
        total_rest = 1400
        rest_per_page = 100
        url_list = [f'https://www.opentable.com/s/?covers=2&currentview=list&datetime=2020-07-31+18%3A30&from={(i-1)*100}&metroid=8&regionids=16&size=100&sort=Popularity' for i in  range(1, 15)]


        print('='*50)
        print(len(url_list))
        print('='*50)

        for url in url_list:
            yield Request(url=url, callback=self.page_parse)



    def page_parse(self, response):

        big_xpath = response.xpath('//ul[@class="content-section-list infinite-results-list analytics-results-list"]/li[@class="result content-section-list-row cf with-times"]')

        for item in big_xpath:
            rest_name = item.xpath('.//span[@class="rest-row-name-text"]/text()').extract()

            rating = item.xpath('.//div[@class="star-rating-score"]/@aria-label').extract_first()
            if type(rating) == 'NoneType':
                rating =  'Not Available'
            #if rating == '': 
                #rating =  'Not Available'
            # if rating  is Null:
            #     rating = 'Not Available'  


            num_reviews = item.xpath('.//span[@class="underline-hover"]/text()').extract()
            if type(num_reviews) == 'NoneType':
                num_reviews = 'Not Available'

            expensive = item.xpath('.//i[@class="pricing--the-price"]/text()').extract()

            genre = item.xpath('.//span[@class="rest-row-meta--cuisine rest-row-meta-text sfx1388addContent"]/text()').extract()

            location = item.xpath('.//span[@class="rest-row-meta--location rest-row-meta-text sfx1388addContent"]/text()').extract()

            delivery = item.xpath('.//h6[@class="rest-row-delivery__title"]/text()').extract()
            if delivery == '':
                delivery = 'None'
            elif len(delivery) == 2:
                delivery = '2'
            # else: 
            #     delivery = delivery[0]
            
            #response.xpath('//ul[@class="content-section-list infinite-results-list analytics-results-list"]/li[@class="result content-section-list-row cf with-times"]//h6[@class="rest-row-delivery__title"]/text()').extract()




            item = OpentableItem()

            item['rest_name'] = rest_name
            item['rating_list'] = rating
            item['num_reviews_list'] = num_reviews
            item['expensive'] = expensive
            item['genre'] = genre
            item['location'] = location
            item['delivery'] = delivery

        #item['booked_today_list'] = booked_today_list  
        #item['delivery_partners'] = delivery_partners

            yield item





        
        # # rest_name = response.xpath('//span[@class="rest-row-name-text"]/text()').extract()
        # # rest_name = response.xpath('//div[@class="rest-row with-image "]/div/div/a/span/text()').extract()
        # #rest_name = response.xpath('//ul[@class="content-section-list infinite-results-list analytics-results-list"]/li/div/div/div/div/a/span/text()').extract()
        # rest_name = response.xpath('//ul[@class="content-section-list infinite-results-list analytics-results-list"]/li//span[@class="rest-row-name-text"]/text()').extract()

        # for i in rest_name:



        # #^right


        # print('='*50)
        # print(len(rest_name))
        # print('='*50)

        
        # big_xpath = response.xpath('//ul[@class="content-section-list infinite-results-list analytics-results-list"]/li[@class="result content-section-list-row cf with-times"]')
        
        
        # rating_list = []
        # for item in big_xpath:
        #     rating = item.xpath('.//div[@class="star-rating-score"]/@aria-label').extract_first()
        #     if type(rating) == 'NoneType':
        #         rating =  'Not Available'
        #     rating_list.append(rating)



        # print('='*50)
        # print(len(rating_list))
        # print(rating_list)
        # print('='*50)



        # num_reviews_list = []
        # for item in big_xpath:
        #     num_reviews = item.xpath('.//span[@class="underline-hover"]/text()').extract()
        #     if type(num_reviews) == 'NoneType':
        #         num_reviews = 'Not Available'
        #     num_reviews_list.append(num_reviews)

        # print('='*50)
        # print(len(num_reviews_list))
        # print(num_reviews_list)
        # print('='*50)




        # booked_today_list = []
        # for item in big_xpath:
        #     booked_today = item.xpath('.//li//div[@class="booking"]/text()').extract()
        #     if type(booked_today) == 'NoneType':
        #         booked_today = 'Not Available'
        #     booked_today_list.append(booked_today)







        # expensive = response.xpath('//ul[@class="content-section-list infinite-results-list analytics-results-list"]/li//i[@class="pricing--the-price"]/text()').extract()
        # # kind of^

        # genre = response.xpath('//ul[@class="content-section-list infinite-results-list analytics-results-list"]/li//span[@class="rest-row-meta--cuisine rest-row-meta-text sfx1388addContent"]/text()').extract()
        

        # location = response.xpath('//ul[@class="content-section-list infinite-results-list analytics-results-list"]/li//span[@class="rest-row-meta--location rest-row-meta-text sfx1388addContent"]/text()').extract()
        

        # # booked_today = response.xpath('//ul[@class="content-section-list infinite-results-list analytics-results-list"]/li//div[@class="booking"]/text()').extract()
        # # ^not quite

  









        # item = OpentableItem()

        # item['rest_name'] = rest_name
        # item['rating_list'] = rating_list
        # item['num_reviews_list'] = num_reviews_list
        # item['expensive'] = expensive
        # item['genre'] = genre
        # item['location'] = location
        # #item['booked_today_list'] = booked_today_list  
        # #item['delivery_partners'] = delivery_partners

        # yield item





