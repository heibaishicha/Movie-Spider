#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/1 16:25
# @Author  : LuoJie
# @Email   : 2715053558@qq.com
# @File    : MoveSpider.py
# @Software: PyCharm

# scrapy框架模块
import scrapy
# json解析模块
import json
# 系统模块
import sys
# items模块
import doubanMovieSpider.items
from scrapy.spiders import Spider
# 爬虫类


class MovieSpider(Spider):
    # 爬虫名
    name = "douban"
    # 域名限定
    allowed_domains = ["www.douban.com"]
    # 爬取URL队列
    start_urls = [
        "http://movie.douban.com/j/serch_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=200&page_start=0"
    ]
    def parse(self, response):
        """
            函数功能:
                解析爬取到的数据
            输入:
                response -> 爬取返回数据对象
            输出:
                空
        """
        # 将爬取到的电影信息存入json容器
        json_container = json.loads(response.body)
        # 构建items。该模块具体含义请查询相关文档。
        items = []
        for movie_elem in json_container['subjects']:
            item = doubanMovieSpider.items.DoubanmoviespiderItem()
            for key in movie_elem:
                if key == 'title':
                    item['title'] = movie_elem[key]
                    print(movie_elem[key])
                if key == 'rate':
                    item['rate'] = movie_elem[key]
                if key == 'id':
                    item['id'] = movie_elem[key]
                    items.append(item)
        # 返回items
        return items
