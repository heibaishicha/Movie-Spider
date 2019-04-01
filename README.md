doubanMovieSpider是工程名，工程包里将会有如下这些文件：

1) scrapy.cfg: 项目配置文件
2) items.py: 需要提取的数据结构定义文件
3) pipelines.py:管道定义，用来对items里面提取的数据做进一步处理，如保存等
4) settings.py: 爬虫配置文件
5) spiders: 放置spider的目录

该工程用于从豆瓣网爬取电影信息(如电影名，评分等等)。

