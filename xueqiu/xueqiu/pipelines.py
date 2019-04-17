from openpyxl import Workbook


class XueqiuPipeline(object):
    def __init__(self):
        self.wb = Workbook()
        self.sheet = self.wb.active
        self.sheet.append(['股票代码', '股票名称', '当前价', '涨跌幅', '市值', '市盈率'])

    def process_item(self, item, spider):
        line = [item['symbol'], item['name'], item['current'], item['chg'], item['market_capital'], item['pe_ttm']]
        self.sheet.append(line)
        self.wb.save('xueqiu.xlsx')
        return item
