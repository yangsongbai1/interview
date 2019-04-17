# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdItem(scrapy.Item):
    good_ID = scrapy.Field()            # 商品ID
    title = scrapy.Field()              # 商品名称
    shop_name = scrapy.Field()          # 店铺名称
    price = scrapy.Field()              # 价格
    link = scrapy.Field()               # 商品链接
    goodCountStr = scrapy.Field()       # 好评
    generalCountStr = scrapy.Field()    # 中评
    poorCountStr = scrapy.Field()       # 差评
    commentCountStr = scrapy.Field()    # 总评论
    max_page = scrapy.Field()           # 评论页数


class CommentItem(scrapy.Item):
    good_ID = scrapy.Field()  # 评论的商品ID
    user_name = scrapy.Field()  # 评论用户的名字
    user_ID = scrapy.Field()  # 评论用户的ID
    date = scrapy.Field()  # 评论时间
    userLevelName = scrapy.Field()  # 会员等级
    userClientShow = scrapy.Field()  # 客户端
    content = scrapy.Field()  # 评论内容
