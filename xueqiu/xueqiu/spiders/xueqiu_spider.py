from xueqiu.items import XueqiuItem
import scrapy
import json


class XueQiu(scrapy.Spider):
    name = 'xueqiu'
    start_urls = [
        'https://xueqiu.com/service/v5/stock/screener/quote/list?page=1&size=100&order=desc&orderby=percent&order_by=percent&market=US&type=us'
    ]

    def parse(self, response):
        items = []
        stock_list = json.loads(response.text).get('data').get('list')
        for stock in stock_list:
            item = XueqiuItem()
            item['symbol'] = stock['symbol']
            item['name'] = stock['name']
            item['current'] = stock['current']
            item['chg'] = stock['chg']
            item['market_capital'] = stock['market_capital']
            item['pe_ttm'] = stock['pe_ttm']
            items.append(item)
            print(item)
        return items
