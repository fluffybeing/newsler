Generic Crawler for News Websites.
================================

<h3> How to use: </h3>

1. Create a JSON file in sources folder with required fields.
Refer to sample.json which has seekingalpha configuration for INTUIT company.
<br/>
   <li>For start_urls enter the urls of the pages from the site where you find the listing of the articles as links.</li>
   <li>To add the AJAX pages (or hidden listing) you have to enter it in the start_urls </li>
   <li> Rules will define which pages to parse from, in other words, it will match the urls with the expressions before proceeding. </li>
  <li> If it matches it will accept the link for either parsing, following or both. </li>
  <li> Paths define the XPATHs to the different fields of the pages to the parsed. As in sample.json, we have paths to Title, Date, Text. </li>
  <li> Once the json file for source setting is done, run the following in the terminal: </li>
   <code>$ scrapy crawl NewsSpider -a src_json=sources/<source_json_name> </code>

  <li> Replace source_json_name with the given name to the json file like sample.json </li>
  <li> To run the crawler on a list of files: </li>
   <code> $ bash runBatch.sh list of files </code> <br/>
   <code> $ bash runBatch.sh sources/bloomberg*.json </code> will run on all settings json named with bloomberg.

<li> The scrapped information will be in the MongoDB / Output JSON file. </li>

for any queries related to the project you can ping me on twitter <a href="https://twitter.com/RahulRRixe"> RahulRRixe </a>
<h2> Cheers! </h2>
