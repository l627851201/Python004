# -*- coding: utf-8 -*-

import os,sys,csv
import requests
from bs4 import BeautifulSoup as bs

class RequestsBS():
    """
    1)安装并使用 requests、bs4 库，
    2)爬取猫眼电影的前 10 个电影名称、电影类型和上映时间，
    3)并以 UTF-8 字符集保存到 csv 格式的文件中。
    """
    
    def __init__(self, nums):
        self.movie_nums = nums
        self.file_name =  os.path.abspath(os.path.dirname(__file__)) + os.sep + "response_text.txt"
        self.target_csv =  os.path.abspath(os.path.dirname(__file__)) + os.sep + "resquests_bs.csv"
        self.domain_url = 'https://maoyan.com'
        self.url = 'https://maoyan.com/films?showType=3'

    def saveResponse(self):
        """
            请求目标网页，获取返回内容
        """
        # 请求头
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Accept-Encoding": "gzip, deflate, br"
        }
        
        # 请求url
        response = requests.get(self.url, headers=header)
        status_code = response.status_code
        if 200 == status_code:
            response.encoding = response.apparent_encoding
            return response.text

        return None
    
    def writeResponse(self):
        """
            保存网页请求数据到本地目录
        """
        text = self.saveResponse()
        with open(self.file_name, 'w', encoding='utf8') as f:
            f.write(text)

    def readResponse(self):
        """
            读取本地文件保存的网页内容
        """
        return_text = ""
        with open(self.file_name, 'r', encoding='utf8') as f:
            return_text = f.read()

        return return_text
 
    def getMovies(self):
        """
            使用bs获取电影名称、电影类型和上映时间
        """
        # 读取文件内容
        response_text = self.readResponse()

        # 写入csv
        with open(self.target_csv, 'w', encoding='utf8', newline='') as csvWriter:
            # 文件标题
            csv_writer = csv.writer(csvWriter)
            hearer = ["电影名称", "电影类型", "上映时间"]
            csv_writer.writerow(hearer)

            # bs解析
            bs_info= bs(response_text, 'html.parser')
            # for i in range(self.movie_nums):
            tags = bs_info.find_all('div', attrs={'class':'movie-hover-info'})
            i = 0
            for tag in tags:
                if self.movie_nums == i:
                    return
                div_tags = tag.find_all("div", attrs={'class': "movie-hover-title"})
                getTitle = div_tags[0]['title']
                getType = (div_tags[1]).get_text().split()[-1]
                getDate = (div_tags[3]).get_text().split()[-1]
                getData = [getTitle, getType, getDate]
                print("{}, {}, {}".format(getTitle, getType, getDate))
                csv_writer.writerow(getData)
                i = i + 1

if __name__ == '__main__':
    rbObj = RequestsBS(10)
    rbObj.getMovies()