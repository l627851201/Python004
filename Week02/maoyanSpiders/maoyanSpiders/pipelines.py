# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os,sys,csv

class MaoyanspidersPipeline:
    def process_item(self, item, spider):
        # return item
        # 写入csv
        file_name = "./spider_bs.csv"
        with open(file_name, 'a', encoding='utf8', newline='') as csvWriter:
            # 文件标题
            csv_writer = csv.writer(csvWriter)
            # hearer = ["电影名称", "电影类型", "上映时间"]
            # csv_writer.writerow(hearer)
            getTitle = item['getTitle']
            getType = item['getType']
            getDate = item['getDate']
            print("MaoyanspidersPipeline: {}, {}, {}".format(getTitle, getType, getDate))
            
            getData = [getTitle, getType, getDate]
            csv_writer.writerow(getData)
        return item

