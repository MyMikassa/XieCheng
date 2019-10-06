import scrapy.commands.crawl as crawl
from scrapy.exceptions import UsageError
from scrapy.commands import ScrapyCommand
import time
import datetime

CityCode = {
	"北京":"BJS",
	"上海":"SHA",
	"广州":"CAN",
	"深圳":"SZX",
	"成都":"CTU",
	"杭州":"HGH",
	"武汉":"WUH",
	"西安":"SIA",
	"重庆":"CKG",
	"青岛":"TAO",
	"长沙":"CSX",
	"南京":"NKG",
	"厦门":"XMN",
	"昆明":"KMG",
	"大连":"DLC",
	"天津":"CGO",
	"郑州":"SYX",
	"三亚":"SHA",
	"济南":"TNA",
	"福州":"FOC"
}

class Command(crawl.Command):

    def verify_date_str_lawyer(self, datetime_str):
        '''用来检测输入的日期是否合法'''
        try:
            datetime.datetime.strptime(datetime_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def add_options(self, parser):
        '''添加命令'''
        ScrapyCommand.add_options(self, parser)
        parser.add_option("-m", "--travelmode", dest="travelmode", default="飞机", type="str",
                          action="store", help="travel mode")
        parser.add_option("-t", "--traveltime", dest="traveltime", default=time.strftime("%Y-%m-%d", time.localtime()),
                          type="str", action="store",
                          help="travel time")
        parser.add_option("-s", "--startstation", dest="startstation", default="北京", type="str",
                          action="store", help="start city")
        parser.add_option("-e", "--endstation", dest="endstation", default="上海", type="str",
                          action="store", help="end city")

    def process_options(self, args, opts):
        '''对输入的命令进行解析'''
        ScrapyCommand.process_options(self, args, opts)

        if opts.travelmode:
            travelmode = opts.travelmode.strip()
            if travelmode not in ("飞机", "火车"):
                raise UsageError("you must input correct travelmode")
            else:
                self.settings.set("travelmode", travelmode, priority="cmdline")

        if opts.traveltime:
            traveltime = opts.traveltime.strip()
            if self.verify_date_str_lawyer(traveltime):
                self.settings.set("traveltime", traveltime, priority="cmdline")
            else:
                raise UsageError("you must input correct traveltime")

        if opts.startstation:
            startstation = opts.startstation.strip()
            self.settings.set("startstation", startstation, priority="cmdline")
            if startstation in list(CityCode.keys()):
                startcitycode = CityCode[startstation]
                self.settings.set("startcitycode", startcitycode, priority="cmdline")
            else:
                raise UsageError("you must input correct startstation")

        if opts.endstation:
            endstation = opts.endstation.strip()
            self.settings.set("endstation", endstation, priority="cmdline")
            if endstation in list(CityCode.keys()):
                endcitycode = CityCode[endstation]
                self.settings.set("endcitycode", endcitycode, priority="cmdline")
            else:
                raise UsageError("you must input correct endstation")

    def run(self, args, opts):
        self.crawler_process.crawl("xiecheng")
        self.crawler_process.start()