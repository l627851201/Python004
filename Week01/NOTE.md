学习笔记

1、requests.get返回乱码
    解决：response.encoding = response.apparent_encoding
2、请求频繁被禁止
    解决：
    1)、保存成功请求的内容到本地，读取文件内容，做爬虫训练
    2)、增加请求延时，避免多次不停爬取被禁止
3、403 很抱歉，您的访问请求由于过于频繁而被禁止。
    解决：请求头的User-Agent字段写错
