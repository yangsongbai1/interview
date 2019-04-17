# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XueqiuItem(scrapy.Item):
    symbol = scrapy.Field()             # 股票代码
    name = scrapy.Field()               # 股票名称
    current = scrapy.Field()            # 当前价
    chg = scrapy.Field()                # 涨跌幅
    market_capital = scrapy.Field()     # 市值
    pe_ttm = scrapy.Field()             # 市盈率
