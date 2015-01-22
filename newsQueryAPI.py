# To interact with the news articles for specific data

from bs4 import BeautifulSoup
import re


class NewsArticle(object):

    def __init__(self, html_doc=""):
        if html_doc == "":
            raise Exception("html_doc cannot be empty!")
        else:
            self.soup = BeautifulSoup(html_doc)

    def get_images(self):
        return [img['src'] for img in self.soup.find_all('img')]

    def get_tables(self):
        return [table for table in self.soup.find_all('table')]

    def get_lists(self):
        lists = []
        for l in self.soup.find_all(['ol', 'ul']):
            lists.append([li.get_text() for li in l.find_all('li')])
        return lists

    def get_strong_text(self):
        text = []
        for tag in self.soup.find_all(['strong', 'bold']):
            text.append(tag.get_text(" "))
        for tag in self.soup.find_all([re.compile("h[1-6]")]):
            text.append(tag.get_text(" "))
        return text

    def get_all_text(self):
        [table.decompose() for table in self.soup.find_all('table')]
        return self.soup.get_text(" ")

    def get_clean_html(self):
        for s in self.soup.find_all('script'):
            s.extract()
        return self.soup.prettify()
