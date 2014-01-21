from bs4 import BeautifulSoup
import re

def clean_html(url, html_doc):
    html_doc = re.sub('\s+', ' ', html_doc).strip()
    f=open("output/%s_garbage.txt"%str(url.replace('/', '_')), 'w')
    soup = BeautifulSoup(html_doc)
    [tag.extract() for tag in soup.find_all(['table', 'ul'])]
    f.write(soup.prettify().encode('ascii', 'ignore')+'\n')
    f.close()