import unittest,allure,time,requests,os,sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
import pytesseract
from fake_useragent import UserAgent
ua = UserAgent(verify_ssl=False)

class LoginProcessOn:
    def __init__(self, url = "https://processon.com"):
        self.url = url
        self.mobile = "18668222825"
        self.password = "Cai15778"
        self.driver = ""

    def loginProcessOnBySelenium(self):
        try:
            # 打开浏览器
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
            self.driver.get(self.url)

            # 登录
            self.driver.find_element_by_xpath('//a[text()="登录"]').click()

            # 手机号&密码
            mobileEle = self.driver.find_element(by=By.CSS_SELECTOR, value='input#login_email')
            mobileEle.clear()
            mobileEle.send_keys(self.mobile)

            # 密码
            passwordEle = self.driver.find_element(by=By.CSS_SELECTOR, value='input#login_password')
            passwordEle.clear()
            passwordEle.send_keys(self.password)

            # 立即登录
            self.driver.find_element_by_css_selector('span#signin_btn').click()

            # 获取网页内容，保存至文件
            fileName = os.path.abspath(os.path.dirname(__file__)) + os.sep + "selenium_pageSource.txt"
            with open(fileName, 'w', encoding='utf8') as f:
                f.write(self.driver.page_source)

            # 校验登录成功
            self.driver.find_element_by_xpath('//a[text()="新建"]').is_displayed()
        except Exception as e:
            print(e)
        finally:
            # 关闭
            self.driver.close()
    
    def loginProcessOnByPost(self):
        # 请求头
        headers = {
            'User-Agent': ua.random,
            "Referer": self.url
        }
        print("请求头，{}".format(headers))

        # 请求体
        payload = {
            "login_email": self.mobile,
            "login_password": self.password
        }

        # 请求
        session = requests.Session()

        # 请求url
        login_url = self.url + "/login"
        result = session.post(login_url, data = payload, headers = headers)

        # 获取网页内容，保存至文件
        fileName = os.path.abspath(os.path.dirname(__file__)) + os.sep + "post_result.txt"
        with open(fileName, 'w', encoding='utf8') as f:
            f.write(result.text)
        getCookie = session.get(self.url + "/cookies")
        print("cookie, {}".format(getCookie))

if __name__ == '__main__':
    loginProcessOnObj = LoginProcessOn()
    # loginProcessOnObj.loginProcessOnBySelenium()
    loginProcessOnObj.loginProcessOnByPost()