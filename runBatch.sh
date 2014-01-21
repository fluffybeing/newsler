
for f in $*
do
    echo "Processing $f"
    `scrapy crawl NewsSpider -a src_json=$f`
done