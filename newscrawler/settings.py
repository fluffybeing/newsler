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
SPIDER_MODULES = ['newscrawler.spiders']
NEWSPIDER_MODULE = 'newscrawler.spiders'

LOG_LEVEL = "INFO"
LOG_FILE = environ['HOME'] + "/IALogs/newscrawler_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".log"

SPIDER_MIDDLEWARES = {
    # 'newscrawler.middleware.IgnoreVisitedItems': 500,
    'newscrawler.middleware.RotateUserAgentMiddleware': 100
}

ITEM_PIPELINES = {
    # 'newscrawler.pipelines.JsonExportPipeline':500,
    'scrapy_mongodb.MongoDBPipeline': 200,
    'newscrawler.pipelines.DuplicatesPipeline': 100,
}

DOWNLOAD_DELAY = 0.25 # To avoid getting banned

# MongoDB setup
MONGODB_HOST = 'localhost'
MONGODB_POST = 27017
MONGODB_DATABASE = 'scrapy'
MONGODB_COLLECTION = 'news'
