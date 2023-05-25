import scrapy

class AdsSpider(scrapy.Spider):
    name = "ads"
    
    def start_requests(self):
        urls = [
            "https://www.portalinmobiliario.com/MLC-1669967170-luis-thayer-ojeda-2121-cercano-a-parque-pocuro-_JM/"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            
    def parse(self, response):
        title = response.xpath("//h1[@class='ui-pdp-title']/text()").get()
        price_currencies = response.xpath("//span[@class='andes-money-amount__currency-symbol']/text()").getall()
        price_amounts = response.xpath("//span[@class='andes-money-amount__fraction']/text()").getall()
        
        return {
            "title": title,
            "price_currency_1": price_currencies[0],
            "price_amount_1": price_amounts[0],
            "price_amount_2": price_amounts[1],
            "price_currency_2": price_currencies[1]
        }
        
    