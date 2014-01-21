# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html


from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from scrapy.contrib.exporter import JsonItemExporter
from scrapy import log

import time

class JsonExportPipeline(object):

    def __init__(self):
        log.start()
        dispatcher.connect(self.spider_opened, signals.spider_opened)
        dispatcher.connect(self.spider_closed, signals.spider_closed)
        self.fjsons = {}

    def spider_opened(self, spider):
        fjson = open('output/%s_%s_items.json' % (spider.name, str(int(time.mktime(time.gmtime())))), 'wb')
        self.fjsons[spider] = fjson
        self.exporter = JsonItemExporter(fjson)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        fjson = self.fjsons.pop(spider)
        fjson.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item