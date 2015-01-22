from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy import log
import os

from newscrawler.items import NewsItem

import re
import json


# For Date Extraction
p1 = re.compile("\w+ \d+ \d+, \d+:\d+")
p2 = re.compile("\w+ \w+ \d+, \d+ \d+:\d+ \w+")


def get_date(text):
    if re.search(p1, text):
        return re.search(p1, text).group()
    elif re.search(p2, text):
        return re.search(p2, text).group()
    else:
        return text


class NewsSpider(CrawlSpider):
    """ Crawl through web sites you specify """

    name = "NewsSpider"

    rules = []

    def __init__(self, **kw):
        src_json = kw.get('src_json') or 'sources/sample.json'

        # Dynamic loading from specified file
        self.MY_SETTINGS = json.load(open(src_json))

        self.allowed_domains = self.MY_SETTINGS['allowed_domains']
        self.start_urls = self.MY_SETTINGS["start_urls"]
        self.CONT_PATHS = self.MY_SETTINGS["paths"]
        for rule in self.MY_SETTINGS["rules"]:
            allow_r = ()
            if "allow" in rule.keys():
                allow_r = [a for a in rule["allow"]]

            deny_r = ()
            if "deny" in rule.keys():
                deny_r = [d for d in rule["deny"]]

            restrict_xpaths_r = ()
            if "restrict_xpaths" in rule.keys():
                restrict_xpaths_r = [rx for rx in rule["restrict_xpaths"]]

            NewsSpider.rules.append(Rule(
                SgmlLinkExtractor(
                    allow=allow_r,
                    deny=deny_r,
                    restrict_xpaths=restrict_xpaths_r,
                ),
                follow=rule["follow"],
                callback='parse_item' if ("use_content" in rule.keys()) else None
            ))

        self.cookies_seen = set()

        if not os.path.exists("output/"):
            os.makedirs("output/")
            fname = 'output/' + (src_json.split('/')[1].split('.')[0]) + "_visited.txt"

            try:
                f_urls = open(fname, 'r')
            except IOError:
                self.OLD_URLS = []
            else:
                self.OLD_URLS = [url.strip() for url in f_urls.readlines()]
                f_urls.close()
            finally:
                self.URLS_FILE = open(fname, 'a')

            super(NewsSpider, self).__init__(**kw)

    def parse_item(self, response):

        if str(response.url) not in self.OLD_URLS:
            self.log("Scraping: %s" % response.url, level=log.INFO)

            hxs = HtmlXPathSelector(response)

            item = NewsItem()

            #item['_id'] = NewsSpider.k
            item['url'] = response.url
            item['source'] = self.MY_SETTINGS["source"]

            item['title'] = None
            for title_path in self.CONT_PATHS["title"]:
                item['title'] = item['title'] or hxs.xpath(title_path).extract()

            item['date'] = None
            for date_path in self.CONT_PATHS["date"]:
                item['date'] = item['date'] or hxs.xpath(date_path).extract()

            div = None
            for div_path in self.CONT_PATHS["text"]:
                div = div or hxs.xpath(div_path)

            text = re.sub('\s+', ' ', ' '.join(div.extract())).strip().replace("\"", "'")

            #Final item entry
            tmp = ' '.join(item['title']).encode('ascii', 'ignore')
            tmp = tmp.replace("\\", "")
            item['title'] = tmp

            tmp = ' '.join(item['date']).encode('ascii', 'ignore')
            tmp = ' '.join(tmp.split())
            item['date'] = get_date(tmp)

            item['content'] = text
            item['company'] = self.MY_SETTINGS["company"]
            item['isClean'] = False

            self.URLS_FILE.write(str(response.url) + '\n')
            yield item