# Python 3.7连接到MySQL数据库的模块推荐使用PyMySQL模块
# pip install pymysql
#  /usr/local/mysql/support-files/mysql.server start
# 一般流程
# 开始-创建connection-获取cursor-CRUD(查询并获取数据)-关闭cursor-关闭connection-结束
import pymysql
import requests

dbInfo = {
    'host' : 'localhost',
    'port' : 3306,
    'user' : 'root',
    'password' : 'Root123',
    'db' : 'spiders'
}

sqls = [
    'select VERSION()', 
    'insert into maoyandata (name,type,startDate) values("test1","test2",now());',
    'select * from maoyandata;']
# sqls = ['insert into maoyanData("name","type","startDate") values("test", "test", now())']

result = []

class ConnDB(object):
    def __init__(self, dbInfo, sqls):
        self.host = dbInfo['host']
        self.port = dbInfo['port']
        self.user = dbInfo['user']
        self.password = dbInfo['password']
        self.db = dbInfo['db']
        self.sqls = sqls

        # self.run()

    def run(self):
        conn = pymysql.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.password,
            db = self.db
        )
        # 游标建立的时候就开启了一个隐形的事物
        cur = conn.cursor()
        try:
            for command in self.sqls:
                cur.execute(command)
                result.append(cur.fetchall())
            # 关闭游标
            cur.close()
            conn.commit()
        except:
            conn.rollback()
        # 关闭数据库连接
        conn.close()

class GetProxyIP:
    def __init__(self):
        self.ip = 'https://ip.jiangxianli.com/api/proxy_ip'
        self.ips = 'https://ip.jiangxianli.com/api/proxy_ips'

    def getIPList(self):
        session = requests.Session()

        response = session.get(self.ips)

        ipList = response.json()['data']
        # print("response, {}".format(ipList))

        dataBody = ipList['data']
        # print(dataBody)
        
        # 获取IP和端口号
        targetIPList = []
        for ips in dataBody:
            protocol = ips['protocol']
            ip = ips['ip']
            port = ips['port']
            targetIPList.append(protocol + "://" + ip + ":" + port)

        print(targetIPList)

if __name__ == "__main__":
    # db = ConnDB(dbInfo, sqls)
    # db.run()
    # print(result)

    getProxyIP = GetProxyIP()
    getProxyIP.getIPList()
