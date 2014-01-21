# #
# # NOT TO BE USED !!
# #
#
#
# import os
#
# os.environ.setdefault('SCRAPY_SETTINGS_MODULE', 'angelco.settings')
#
# from twisted.internet import reactor
#
# from scrapy import log, signals
# from scrapy.crawler import Crawler
# from scrapy.settings import CrawlerSettings
# from scrapy.xlib.pydispatch import dispatcher
#
# #from testspiders.spiders.followall import FollowAllSpider
# from angelco.spiders.spiders import MySpider
# from angelco.spiders.genericSpider import FollowAllSpider
#
# from sys import argv
#
#
# def stop_reactor():
#     log.msg("Crawler Stopped!", level=log.DEBUG)
#     reactor.stop()
#
#
# if __name__ == "__main__":
#
#     if len(argv) == 1:
#         print "Usage : python run_crawler.py <domain_name>"
#         exit(0)
#
#     else:
#         dispatcher.connect(stop_reactor, signal=signals.spider_closed) # To detect closing of spider
#
#         spider = MySpider(src_json=argv[1])
#
#         # settings = CrawlerSettings()
#         # settings.overrides['ITEM_PIPELINES'] = {
#         #   		'angelco.pipelines.JsonExportPipeline':500,
#         # }
#
#         # crawler = Crawler(settings)
#         # crawler.install()
#         # crawler.configure()
#
#         crawler = Crawler(CrawlerSettings())
#         crawler.install()
#         crawler.configure()
#
#         crawler.crawl(spider)
#
#         crawler.start()
#         log.start(loglevel=log.DEBUG)
#
#         log.msg('Running reactor...')
#         reactor.run()  # the script will block here until the spider is closed
#         log.msg('Reactor stopped.')