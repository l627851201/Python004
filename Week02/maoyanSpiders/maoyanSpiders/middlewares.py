# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.exceptions import NotConfigured
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
from collections import defaultdict
from urllib.parse import urlparse
import random
import requests

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class MaoyanspidersSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

class RandomHttpProxyMiddleware(HttpProxyMiddleware):

    def __init__(self, auth_encoding='utf-8'):
        self.proxies = defaultdict(list)

        # 代理列表
        proxy_list = self.get_proxy_ip_list()
        for proxy in proxy_list:
            parse = urlparse(proxy)
            self.proxies[parse.scheme].append(proxy)

    def get_proxy_ip_list(self):
        proxy_address = 'https://ip.jiangxianli.com/api/proxy_ips'

        # 请求
        response = requests.get(proxy_address)

        ipList = response.json()['data']
        # print("response, {}".format(ipList))

        dataBody = ipList['data']
        # print("ip list, \n")
        # print(dataBody)
        
        # 获取IP和端口号
        targetIPList = []
        for ips in dataBody:
            protocol = ips['protocol']
            ip = ips['ip']
            port = ips['port']
            targetIPList.append(protocol + "://" + ip + ":" + port)

        print(targetIPList)
        return targetIPList

    @classmethod
    def from_crawler(cls, crawler):
        # if not crawler.settings.get('HTTP_PROXY_LIST'):
            # raise NotConfigured

        # http_proxy_list = crawler.settings.get('HTTP_PROXY_LIST')
        http_proxy_list = cls.get_proxy_ip_list(cls)
        auth_encoding = crawler.settings.get('HTTPPROXY_AUTH_ENCODING', 'utf-8')

        # return cls(auth_encoding, http_proxy_list)
        return cls(auth_encoding)

    def _set_proxy(self, request, scheme):
        proxy = random.choice(self.proxies[scheme])
        print("_set_proxy, {}".format(proxy))
        request.meta['proxy'] = proxy
    
class MaoyanspidersDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
