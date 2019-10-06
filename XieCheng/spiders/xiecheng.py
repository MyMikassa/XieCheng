# -*- coding: utf-8 -*-
import re

import scrapy
from selenium import webdriver
from XieCheng.items import XiechengItem

class XiechengSpider(scrapy.Spider):
    name = 'xiecheng'
    allowed_domains = ['www.ctrip.com']
    start_urls = ['http://www.ctrip.com/']

    def __init__(self):
        self.options = webdriver.FirefoxOptions()
        self.options.add_argument('-headless')
        self.browser = webdriver.Firefox(options=self.options)
        super().__init__()

    def parse(self, response):
        item = XiechengItem()
        AllData = response.xpath("//*[@class='search_table_header']")
        for data in AllData:
            item["TravelMode"] = self.settings['travelmode'].strip()
            item["TravelTime"] = self.settings['traveltime'].strip()

            information_one = data.xpath("./div[1]").extract()[0].strip()
            try:
                item["AirLine"] = re.search('<strong.*?>([\u4E00-\u9FA5]+)</strong>', information_one).group(1)
            except:
                item["AirLine"] = ""
            try:
                item["AircraftId"] = re.search('</strong><span>(.*?)</span>', information_one).group(1)
            except:
                item["AircraftId"] = ""
            try:
                item["AircraftType"] = re.search('<span.*>([\u4E00-\u9FA5].*?)</span>', information_one).group(1)
            except:
                item["AircraftType"] = ""

            information_two = data.xpath("./div[2]").extract()[0].strip()
            # print(information_two)
            try:
                item["DepartureTime"] = re.search('<.*?class="time">(.*?)</strong>', information_two).group(1)
            except:
                item["DepartureTime"] = ""
            try:
                item["DepartureStation"] = re.search('<.*?class="airport">(.*?)</div>', information_two).group(1)
                if re.search('<.*?class="c-react-frame">(.*?)<span', item["DepartureStation"]):
                    item["DepartureStation"] = "".join(re.search('<.*?class="c-react-frame">(.*?)<span.*?>(.*?)</span>', item["DepartureStation"]).group(1, 2))
            except:
                item["DepartureStation"] = ""

            information_three = data.xpath("./div[4]").extract()[0].strip()
            # print(information_three)
            try:
                item["TerminalTime"] = re.search('<.*?class="time">(.*?)</strong>', information_three).group(1)
            except:
                item["TerminalTime"] = ""
            try:
                item["Terminal"] = re.search('<.*?class="airport">(.*?)</div>', information_three).group(1)
                if re.search('<.*?class="c-react-frame">(.*?)<span', item["Terminal"]):
                    item["Terminal"] = "".join(re.search('<.*?class="c-react-frame">(.*?)<span.*?>(.*?)</span>', item["Terminal"]).group(1, 2))
            except:
                item["Terminal"] = ""

            information_four = data.xpath("./div[5]").extract()[0].strip()
            try:
                item["PunctualityRate"] = re.search("id=.*?>(.*?)</span>", information_four).group(1)
            except:
                item["PunctualityRate"] = ""

            information_five = data.xpath("./div[7]").extract()[0].strip()
            try:
                item["Fare"] = ''.join(re.search("</dfn>(.*?)</span><i>(.*?)</i>", information_five).group(1, 2))
            except:
                item["Fare"] = ""
            try:
                item["Discount"] = re.search("<span>(.*?)</span>", information_five).group(1)
            except:
                item["Discount"] = ""

            yield item

