# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field


class NewsItem(Item):
    # define the fields for your item here like:
    # name = Field()
    title = Field()
    date = Field()
    url = Field()
    source = Field()
    content = Field()
    company = Field()
    isClean = Field()
    author = Field()
    link = Field()
    data_url = Field()
    data_a = Field()
    data_b = Field()
    data_c = Field()
    data_d = Field()
    data_key = Field()
    visit_id = Field()
    visit_status = Field()


class Page(Item):
    url = Field()
    title = Field()
    size = Field()
    referer = Field()
    newcookies = Field()
    body = Field()
