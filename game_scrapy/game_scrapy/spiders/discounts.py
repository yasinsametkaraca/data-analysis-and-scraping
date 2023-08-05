import scrapy


def discount_rate_convert(discount_rate):
    if discount_rate:
        return discount_rate.replace("-", "")
    return "No Discount"


class DiscountsSpider(scrapy.Spider):
    name = "discounts"
    allowed_domains = ["store.steampowered.com"]
    start_urls = ["https://store.steampowered.com/search/?filter=topsellers"]

    def parse(self, response):
        games = response.xpath("//div[@id='search_result_container']//a")

        for game in games:
            yield {
                "title": game.xpath(".//div[@class='col search_name ellipsis']/span[@class='title']/text()").get(),  # get() : if we use get method, it will return the first element and if there is no element, it will return None. Return type is string.
                "image": game.xpath(".//div[@class='col search_capsule']/img/@src").get(),
                "discount_rate": discount_rate_convert(game.xpath(".//div[@class='col search_discount_and_price responsive_secondrow']//div[@class='discount_pct']/text()").get()),
                "old_price": game.xpath(".//div[@class='discount_original_price']/text()").get(),
                "price": game.xpath(".//div[@class='discount_final_price']/text()").get(),
            }

        next_page = response.xpath("//a[@class='pagebtn' and text()='>'] /@href").get()
        if next_page:
            full_link = response.urljoin(next_page)
            yield scrapy.Request(url=full_link, callback=self.parse)

