import scrapy
import re

def convert_clp_str_to_int(clp: str) -> int:
    amount = clp.copy() # pure function restriction -> no alteration to global variable
    amount = amount.replace("$ ", "")
    amount = amount.replace(".", "")
    return int(amount)

def convert_uf_str_to_int(uf: str) -> int:
    amount = uf.copy()
    amount = re.sub(r"[()]", "", amount)
    amount = amount.replace(" UF", "")
    amount = amount.replace(".", "")
    return int(amount)
    

class YapoAdsSpider(scrapy.Spider):
    name = "yapo_ads"
    
    def start_requests(self):
        urls = [
            "https://new.yapo.cl/inmuebles/nogales-con-carlos-antunezentrega-inmediata_86770153"
        ] # example url
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        # TODO: Testing
        title = response.xpath("//h1[@class='my-2 title order-1']/text()").get()
        prices = response.xpath("//adview-amount-info/div/div/p/text()").getall()
        price_clp = convert_clp_str_to_int(prices[0])
        price_uf = convert_uf_str_to_int(prices[1])
        
        return {
            "title": title,
            "price_uf": price_uf,
            "price_clp": price_clp
        }
        