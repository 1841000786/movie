# -*- coding: utf-8 -*-
import scrapy
from movie.items import MovieItem
# //ul[@class="top-list  fn-clear"]/li/h5/a/text()

class MeijuSpider(scrapy.Spider):
    name = 'meiju'    # 爬虫名。一个项目下可能有多个爬虫，并且每个爬虫有优先级、并发等设置。scrapy crawl[spider_name]
    allowed_domains = ['meijutt.com']  # 为了防止爬虫项目自动爬取到其它网站，设置限制，每一次请求前都会检查请求的网址是否属于这个域名下，是的话才允许请求。注意:爬取日志爬取网址后响应总为None,检查allowed_domain书写是否正确。值是一级域名
    start_urls = ['http://meijutt.com/new100.html']  # 第一个请求的url,所有请求的入口。

    def parse(self, response):
        # print(response.status_code,response.content,response.text)
       #非框架写法 dom = lxml.etree.HTML(response.text);dom.xpath('')
        #scrapy框架下正规写法  Selector(response.text).xpath('').extract()
        #获取剧集名
        movie_list = response.xpath('//ul[@class="top-list  fn-clear"]/li')  #
        # / h5 /text()
        for movie in movie_list:
           #  xpath()返回[Selector(),Selector()]
            # xpath.extract()返回['剧集名1','剧集名2']
            # xpath.extract_first()返回’剧集名1
            # #表示在字标签基础上继续解析    extract() 返回的是列表
            name = movie.xpath('./h5/a/text()').extract_first()


            item = MovieItem()
            item ['name']=name
            yield item  #相当于同步脚本中的
        pass

