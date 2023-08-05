import scrapy


class BestSellersSpider(scrapy.Spider):
    name = "best_sellers"
    allowed_domains = ["kidega.com"]
    start_urls = ["https://www.kidega.com/cok-satanlar"]

    def start_requests(self):
        yield scrapy.Request(url="https://www.kidega.com/cok-satanlar", callback=self.parse, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        })  # to set the user agent. If the user agent is not set, the website will block the request. So we need to set the user agent.

    def parse(self, response):
        books = response.xpath("//ul[@class='emosInfinite product-list-grid view-box']/li/div")
        for book in books:
            yield {
                "title": book.xpath(".//h3[@class='book-name']/text()").get(),
                "image": book.xpath(".//div[@class='prd-image image']/div/img/@data-original").get(),
                "author": book.xpath(".//div[@class='authorArea']/div/a/span[@class='manufacturer-name']/text()").get(),
                "publisher": book.xpath(".//div[@class='publisherArea']//span[@class='distributor-name']/text()").get(),
                "discount_rate": book.xpath(".//div[@class='prd-price']//span[@class='redDiscont']/text()").get(),
                "old_price": book.xpath(".//div[@class='firstPrice']/div/text()").get(),
                "new_price": book.xpath(".//div[@class='lastPrice']/div/text()").get(),
                "user_agent": response.request.headers["User-Agent"].decode("utf-8")  # to get the user agent from the request headers
            }

        next_page = response.xpath("//a[@id='ctl00_u8_ascUrunList_ascPagingDataAlt_lnkNext']/@href").get()
        if next_page:
            # full_link = f"http://kidega.com{next_page}" # another way to get the full link  # https://kidega.com/cok-satanlar/?page=2
            full_link = response.urljoin(next_page)  # to get the full link  # https://kidega.com/cok-satanlar/?page=2
            yield scrapy.Request(url=full_link, callback=self.parse, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
            })  # recursive call to parse function. It will continue to scrape until there is no next page. Self.parse is the callback function and it will be called when the response is ready. Url is the next page url.


# to run = scrapy crawl best_sellers

# to write to csv = scrapy crawl best_sellers -o best_sellers.csv

# to write to json = scrapy crawl best_sellers -o best_sellers.json

# to write to json lines = scrapy crawl best_sellers -o best_sellers.jl

# to write to xml = scrapy crawl best_sellers -o best_sellers.xml

# to write to pickle = scrapy crawl best_sellers -o best_sellers.pickle

# to write to marshal = scrapy crawl best_sellers -o best_sellers.marshal

# to write to msgpack = scrapy crawl best_sellers -o best_sellers.msgpack

# ctrl + shift + p and type javascript and select disable javascript

# scrapy shell https://www.kidega.com/cok-satanlar

# for find user agent = scrapy shell https://www.whatismybrowser.com/detect/what-is-my-user-agent

