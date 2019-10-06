# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XiechengItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    TravelMode = scrapy.Field()     #出行方式
    TravelTime = scrapy.Field()     #出行时间

    AirLine = scrapy.Field()        #航空公司
    AircraftId = scrapy.Field()     #飞机Id
    AircraftType = scrapy.Field()   #飞机型号
    DepartureStation = scrapy.Field()       #飞机始发站
    Terminal = scrapy.Field()       #飞机终点站
    DepartureTime = scrapy.Field()        #出发时间
    TerminalTime = scrapy.Field()       #到达时间
    PunctualityRate = scrapy.Field()        #准点率
    Fare = scrapy.Field()       #票价
    Discount = scrapy.Field()       #折扣




    pass
