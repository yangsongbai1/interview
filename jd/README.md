# 京东采集

## python版本
python3.6

## 依赖库
创建虚拟环境，执行以下命令
```
pip install -r requirements.txt

```

## 使用
采集商品信息
```
scrapy crawl jd
```

采集商品的评论信息
```
scrapy crawl comment
```

数据存储为excel格式，
商品信息的文件名为 goods.xlsx 
商品的评论的文件名为 goods.xlsx 