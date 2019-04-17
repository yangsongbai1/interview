from openpyxl import Workbook


class JdPipeline(object):
    def __init__(self):
        self.wb = Workbook()
        self.sheet = self.wb.active
        self.sheet.append(['商品ID', '商品名称', '价格', '店铺名称', '商品链接', '好评', '中评', '差评', '总评论', '评论页数'])

    def process_item(self, item, spider):
        line = [item['good_ID'], item['title'], item['price'], item['shop_name'], item['link'], item['goodCountStr'],
                item['generalCountStr'], item['poorCountStr'], item['commentCountStr'], item['max_page']]
        self.sheet.append(line)
        self.wb.save('goods.xlsx')
        return item


class CommentPipeline(object):
    def __init__(self):
        self.wb = Workbook()
        self.sheet = self.wb.active
        self.sheet.append(['商品ID', '用户昵称', '用户ID', '评论时间', '会员等级', '客户端', '评论内容'])

    def process_item(self, item, spider):
        line = [item['good_ID'], item['user_name'], item['user_ID'], item['date'], item['userLevelName'],
                item['userClientShow'], item['content']]
        self.sheet.append(line)
        self.wb.save('comment.xlsx')
        return item
