# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from pypinyin import lazy_pinyin

class XiechengPipeline(object):
    def process_item(self, item, spider):
        return item

    @classmethod
    def from_settings(cls, settings):
        return cls(settings)

    def __init__(self, settings):
        self.settings = settings

    def open_spider(self, spider):
        if self.settings['travelmode'] == "飞机":
            spider.start_urls = [
                "https://flights.ctrip.com/itinerary/oneway/%s-%s?date=%s"%(
                    self.settings["startcitycode"],
                    self.settings["endcitycode"],
                    self.settings["traveltime"])
            ]
        else:
            spider.start_urls = [
                "https://trains.ctrip.com/TrainBooking/Search.aspx?from=%s&to=%s&day=%s"%(
                    ''.join(lazy_pinyin(self.settings["startstation"])),
                    ''.join(lazy_pinyin(self.settings["endstation"])),
                    self.settings["traveltime"]
                )
            ]
