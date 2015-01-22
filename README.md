Financial News Crawler
================================
This is a generic news crawler built on the top of Scrapy framework.


Setup Process
---------------------
* Create a JSON file in sources folder with required fields.
Refer to sample.json which has seekingalpha configuration for INTUIT company.
* For start_urls enter the urls of the pages from the site where you find the listing of the articles as links.
* To add the <strong> AJAX pages (or hidden listing) </strong> you have to enter it in the start_urls
* Rules will define which pages to parse from, in other words, it will match the urls with the expressions before proceeding.
* If it matches it will accept the link for either parsing, following or both.
* Paths define the XPATHs to the different fields of the pages to the parsed. As in sample.json, we have paths to Title, Date, Text.

Running
-------
* Once the json file for source setting is done, run the following in the terminal:
  ```bash
    $ scrapy crawl NewsSpider -a src_json=sources/<source_json_name> </code>
  ```
* Replace source_json_name with the given name to the json file like sample.json

To run the crawler on a list of files
-------------------------------------
  ```bash
  $ bash runBatch.sh list of files </code> <br/>
  $ bash runBatch.sh sources/bloomberg*.json </code> will run on all settings json named with bloomberg.
  ```
Storage
-------
* The scrapped information will be in the MongoDB / Output JSON file. </li>
* for any queries related to the project you can ping me on twitter <a href="https://twitter.com/RahulRRixe"> RahulRRixe </a>

## Cheers!
