Generic Crawl for News Websites.

How to use:

1. Create a JSON file in sources folder with required fields.
Refer to sample.json which has seekingalpha configuration for INTUIT company.

For start_urls enter the urls of the pages from the site where you find the listing of the articles as links.

To add the AJAX pages (or hidden listing) you have to enter it in the start_urls

Rules will define which pages to parse from, in other words, it will match the urls with the expressions before proceeding.
If it matches it will accept the link for either parsing, following or both.

Paths define the XPATHs to the different fields of the pages to the parsed. As in sample.json, we have paths to Title,
Date, Text.

2. Once the json file for source setting is done, run the following in the terminal:

`scrapy crawl NewsSpider -a src_json=sources/<source_json_name>`

Replace source_json_name with the given name to the json file like sample.json

3. To run the crawler on a list of files:

`bash runBatch.sh <list of files>`

e.g. `bash runBatch.sh sources/bloomberg*.json` will run on all settings json named with bloomberg.

The scrapped information will be in the MongoDB / Output JSON file.