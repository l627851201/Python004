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

上周作业完成情况已同步到小组群
针对常见的问题可以在问题集中找到答案 https://shimo.im/docs/qK36trYXqv9PgvWY

避免频繁开启和关闭数据库连接可以参考：
四、Scrapy 爬虫中，不想在 pipeline 文件中每次执行到 process_item 方法时都做一次I/O访问存储，就想爬虫开始到停止，只做一次 I/O 操作把所有数据存储起来

settings.py 中的代理只配置了 http 的代理，爬虫爬取的是 https 网页，程序不走代理的原因可以参考：
六、用 Scrapy 设置随机代理的时候，def _set_proxy(self, request, scheme):  始终不执行，可能是什么原因呢，其他2个函数都能正常执行

@所有人 
上周的优秀作业大家参考下哈
https://shimo.im/docs/jWYQv8qdPvTTpkTd/