import os
import requests
import queue
import threading
from fake_useragent import UserAgent

class DownloadThread(threading.Thread):
    def __init__(self, q):
        super().__init__()
        self.q = q

    def run(self):
        while True:
            # 从队列中取出元素
            url = self.q.get()

            print(f"{self.name} begin download {url}")
            # 下载文件
            self.download_file(url)
            # 下载完成发送信号
            self.q.task_done()
            print(f"{self.name} download complete")

    def download_file(self, url):
        ua = UserAgent()
        
        # 请求头
        headers = {
            'User-Agent': ua.random
        }

        # 请求数据
        response = requests.get(url, stream=True, headers=headers)
        fileSplit = url.split('.')[1]
        file_name = os.path.abspath(os.path.dirname(__file__))  + os.sep + fileSplit + ".html"
        # file_name = os.path.basename(url) + '.html'
        print(file_name)
        with open(file_name, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if not chunk:
                    break
                f.write(chunk)

if __name__ == "__main__":
    urls = [
        "http://www.baidu.com",
        "http://www.douban.com",
        "http://www.python.org"
    ]

    q = queue.Queue()

    for _ in range(5):
        downObj = DownloadThread(q)
        downObj.setDaemon(True)
        downObj.start()

    for url in urls:
        q.put(url)

    q.join()