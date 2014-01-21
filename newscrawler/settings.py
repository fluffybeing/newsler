# Scrapy settings for angelco project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

from datetime import datetime
from os import environ

# Settings

BOT_NAME = 'newscrawler'

SPIDER_MODULES = ['newscrawler.spiders']

NEWSPIDER_MODULE = 'newscrawler.spiders'

LOG_LEVEL = "INFO"
#LOG_FILE = environ['HOME'] + "/IALogs/newscrawler_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".log"

SPIDER_MIDDLEWARES = {
    'newscrawler.middleware.IgnoreVisitedItems': 500,
    'newscrawler.middleware.RotateUserAgentMiddleware' : 100
}

ITEM_PIPELINES = {
    #'newscrawler.pipelines.JsonExportPipeline':500,
    'scrapy_mongodb.MongoDBPipeline': 200
}

DOWNLOAD_DELAY = 0.25 # To avoid getting banned

MONGODB_HOST = 'localhost'
MONGODB_POST = 27017
MONGODB_DATABASE = 'garbage'
MONGODB_COLLECTION = 'news'


#DOWNLOADER_MIDDLEWARES = {
#    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
#    'angelco.proxy_middleware.ProxyMiddleware': 100,
#}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'angelco (+http://www.yourdomain.com)'