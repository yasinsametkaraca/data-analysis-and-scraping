import scrapy
from scrapy_splash import SplashRequest


#  when we disabled the javascript in the browser, we can see that the quotes are not loaded. So, we need to use SplashRequest to render the page and then scrape the data.
class SplashExSpider(scrapy.Spider):
    name = "splash_ex"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/js/"]
    script = '''
        function main(splash, args)
    	    url = args.url
            assert(splash:go(url))
            assert(splash:wait(1))
            return splash:html()
        end
    '''

    def start_requests(self):
        yield SplashRequest(url=self.start_urls[0], callback=self.parse, endpoint="execute", args={
            'lua_source': self.script
        })

    def parse(self, response):
        for quote in response.xpath("//div[@class='quote']"):
            yield {
                'quote': quote.xpath(".//span/text()").get(),
                'author': quote.xpath(".//span[2]/small/text()").get(),
                'tags': quote.xpath(".//div[@class='tags']/a/text()").getall()
            }


# Generator: A generator is a function that produces or yields a sequence of values using yield method. When a generator function is called, it returns a generator object without even beginning execution of the function. When the next() method is called for the first time, the function starts executing until it reaches the yield statement, which returns the yielded value. The yield keeps track i.e. remembers the last execution and the second next() call continues from previous value.
# yield is like return. Yield is a generator. Yield is a keyword that is used like return, except the function will return a generator. When you call the function, the code you have written in the function body does not run. The function only returns the generator object. Then, your code will be run each time the for uses the generator.