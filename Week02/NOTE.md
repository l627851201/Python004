作业
作业一：
scrapy startproject proxySpiders
scrapy genspider proxyMovies douban.com
crapy crawl maoyanSpiders

为 Scrapy 增加代理 IP 功能。
将保存至 csv 文件的功能修改为保持到 MySQL，并在下载部分增加异常捕获和处理机制。
备注：代理 IP 可以使用 GitHub 提供的免费 IP 库。

作业二：

使用 requests 或 Selenium 模拟登录石墨文档 https://shimo.im

https://ip.jiangxianli.com/api/proxy_ip

https://ip.jiangxianli.com/api/proxy_ips

学习笔记
1、代理IP的使用，生疏且用了之后还无法判断是否有效
2、图形验证码的大概有个思路，缺少实践，实现起来比较费时间