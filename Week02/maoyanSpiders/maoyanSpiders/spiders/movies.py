# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from bs4 import BeautifulSoup as bs
from maoyanSpiders.items import MaoyanspidersItem
from fake_useragent import UserAgent
ua = UserAgent(verify_ssl=False)

class DoubanSpider(scrapy.Spider):
    # 定义爬虫名称
    name = 'maoyanSpiders'
    allowed_domains = ['maoyan.com']
    # 起始URL列表
    start_urls = ['https://maoyan.com/films?showType=3']

#   注释默认的parse函数
#   def parse(self, response):
#        pass

    def parse(self, response):
        item = MaoyanspidersItem()        
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        # movies = Selector(response="response_text.html").xpath('//div[@class="movie-hover-info"]')
        print("movies len, {}".format(len(movies)))

        # 提取前10个
        getMovies = []
        for i in range(10):
            getMovies.append(movies[i])

        # 遍历前10个电影列表
        for movie in getMovies:
            movieName = movie.xpath('.//div[2]/@title')
            movieType = movie.xpath('.//div[2]/text()')
            movieDate = movie.xpath('.//div[4]/text()')
            # print("movie{}, {}, {}".format(movieName, movieType, movieDate))
            # print("type , {}".format(type(movieName)))
            getTitle = movieName.extract_first().strip()
            getType = movieType.getall()[-1].strip()
            getDate = movieDate.getall()[-1].strip()
            item["getTitle"] = getTitle
            item["getType"] = getType
            item["getDate"] = getDate
            # print("DoubanSpider：{}, {}, {}".format(getTitle, getType, getDate))
            yield item

    def parseBS(self, response):
        item = MaoyanspidersItem()
        soup = bs(response.text, 'html.parser')
        # get_divs = soup.find_all('div', attrs = {'class': "movie-item-hover"})
        tags = soup.find_all('div', attrs={'class':'movie-hover-info'}, limit=10)
        print("tags len, {}".format(len(tags)))
        for tag in tags:
            div_tags = tag.find_all("div", attrs={'class': "movie-hover-title"})
            getTitle = div_tags[0]['title']
            getType = (div_tags[1]).get_text().split()[-1]
            getDate = (div_tags[3]).get_text().split()[-1]
            item["getTitle"] = getTitle
            item["getType"] = getType
            item["getDate"] = getDate
            print("DoubanSpider：{}, {}, {}".format(getTitle, getType, getDate))
            yield item

