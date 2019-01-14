# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#管道：数据清洗、去重
# 持久化：写txt，scv.写入数据


#scrapy框架将爬去spider模块和处理pipeline分离开，是的程序更容易扩展
# spider yield生成的item会交给pipline处理，如果速度不一致的话，scrapy框架会自动调度
# spider yield相当于生产消费模型中的生产者，
class MoviePipeline(object):
    def process_item(self, item, spider):
        #爬虫部分在for循环yield item ,所以process——item方法会重复执行
        # 覆盖上次写的信息
        with open('my_meiju.txt','a',encoding='utf-8') as f:
            f.write(str(item['name'])+'\n')
        return item
