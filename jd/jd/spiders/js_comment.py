import scrapy
from jd.items import CommentItem

from openpyxl import load_workbook
import json


class Comment(scrapy.Spider):
    name = 'comment'
    allowed_domains = ['jd.com']
    start_urls = []

    wb = load_workbook('goods.xlsx')
    sheet = wb.active
    good_id = sheet['A'][1:]  # 商品id列表
    max_page = sheet['J'][1:]  # 对应的评论数
    for i, j in zip(good_id, max_page):
        for page in range(int(j.value)):
            url = f'https://sclub.jd.com/comment/productPageComments.action?productId={i.value}&score=0&sortType=5&page={page}&pageSize=10'
            start_urls.append(url)

    def parse(self, response):
        items = []
        comments = json.loads(response.text).get('comments', [])
        for comment in comments:
            item = CommentItem()
            item['good_ID'] = comment['referenceId']
            item['user_name'] = comment['nickname']
            item['user_ID'] = comment['id']
            item['date'] = comment['referenceTime']
            item['userLevelName'] = comment['userLevelName']
            item['userClientShow'] = comment['userClientShow']
            item['content'] = comment['content']
            items.append(item)
        return items
