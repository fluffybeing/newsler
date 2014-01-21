__author__ = 'nightwing'

import requests

from sys import argv
from bs4 import BeautifulSoup



if __name__ == "__main__":
    if len(argv) == 2:
        URL = argv[1]
    else:
        URL = "http://www.bloomberg.com/quote/AAPL:US/news"

    r = requests.get(URL)
    soup = BeautifulSoup(r.text)
    links = filter(len, [a_tag['href'] if a_tag.has_attr('href') else "" for a_tag in soup.find_all("a")])

    for link in sorted(links):
        print link