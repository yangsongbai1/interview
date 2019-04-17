import scrapy
from jd.items import JdItem

import json


class JD(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    start_urls = [
        'https://search.jd.com/Search?keyword=%E8%BF%9B%E5%8F%A3%E7%89%9B%E5%A5%B6&enc=utf-8&wq=%E8%BF%9B%E5%8F%A3%E7%89%9B%E5%A5%B6&pvid=16abdf7af7b04a2c837a08aaa8705e60'
    ]

    def parse(self, response):
        goods = response.xpath('//li[@class="gl-item"]')
        for good in goods:
            item1 = JdItem()
            gid = good.xpath('./@data-sku').extract_first()
            link = f'https://item.jd.com/{gid}.html'
            item1['good_ID'] = gid
            item1['title'] = good.xpath('string(.//div[@class="p-name p-name-type-2"]//em)').extract_first()
            item1['link'] = link
            item1['price'] = good.xpath('.//div[@class="p-price"]//i//text()').extract_first()
            yield scrapy.Request(url=link, meta={'item': item1}, callback=self.parse_detail)

    def parse_detail(self, response):
        item1 = response.meta['item']
        item1['shop_name'] = response.xpath(
            '//div[@class="J-hove-wrap EDropdown fr"]//div[@class="name"]//a//text()').extract_first()
        gid = item1['good_ID']
        comment_url = f'https://sclub.jd.com/comment/productPageComments.action?productId={gid}&score=0&sortType=5&page=0&pageSize=10'
        yield scrapy.Request(url=comment_url, meta={'item': item1}, callback=self.parse_get_comment)

    def parse_get_comment(self, response):
        item1 = response.meta['item']
        data = json.loads(response.text).get('productCommentSummary')
        item1['commentCountStr'] = data['commentCountStr']
        item1['goodCountStr'] = data['goodCountStr']
        item1['generalCountStr'] = data['generalCountStr']
        item1['poorCountStr'] = data['poorCountStr']
        item1['max_page'] = json.loads(response.text).get('maxPage')
        return item1
