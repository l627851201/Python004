import unittest,allure,time,requests,os,sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
import pytesseract
from fake_useragent import UserAgent
ua = UserAgent(verify_ssl=False)

class LoginShiMo:
    def __init__(self, url = "https://shimo.im"):
        self.imgPath = os.path.abspath(os.path.dirname(__file__)) + "cap.jpg"
        self.ocrImgPath = os.path.abspath(os.path.dirname(__file__)) + "gray2.jpg"
        self.ocrImgPath2 = os.path.abspath(os.path.dirname(__file__)) + "c_th.jpg"
        self.driver = ""

    def loginShiMo(self):
        try:
            # 打开浏览器
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
            self.driver.get(url)

            # 登录
            btnSelector = '//button[text()="{}"]'
            self.driver.find_element_by_xpath(btnSelector.format("登录")).click()

            # 手机号&密码
            selector = '//label[text()="{}"]/following-sibling::div/input'
            mobileEle = self.driver.find_element(by=By.XPATH, value=selector.format('输入注册手机号或邮箱'))
            mobileEle.clear()
            mobileEle.send_keys("18668222825")

            # 密码
            passwordEle = self.driver.find_element(by=By.XPATH, value=selector.format('输入密码'))
            passwordEle.clear()
            passwordEle.send_keys("18668222825")

            # 立即登录
            self.driver.find_element_by_xpath(btnSelector.format("立即登录")).click()

            # 获取图片地址，保存图片
            time.sleep(5)
            imgSelector = '//img[@class="geetest_item_img"]'
            imgUrl = self.driver.find_element_by_xpath(imgSelector).get_attribute("src")
            print(f"图片地址，{imgUrl}")

            return imgUrl
        except Exception as e:
            print(e)
        finally:
            # 关闭
            self.driver.close()

    def saveImg(self, imgUrl):
        session = requests.Session()
        agent = ua.random
        headers = {
            'User-Agent': agent
        }

        r = session.get(imgUrl, headers=headers)
        with open(self.imgPath, 'wb') as f:
            f.write(r.content)

    def ocrImg(self):
        # 打开并显示文件
        im = Image.open(self.imgPath)
        im.show()

        # 灰度图片
        gray = im.convert('L')
        gray.save(self.ocrImgPath)
        im.close()

        # 二值化
        threshold = 100
        table = []

        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)

        out = gray.point(table, '1')
        out.save(self.ocrImgPath2)

        th = Image.open(self.ocrImgPath2)
        print(pytesseract.image_to_string(th,lang='chi_sim+eng'))

if __name__ == '__main__':
    loginShiMo = LoginShiMo()
    # imgUrl = loginShiMo.loginShiMo()
    loginShiMo.ocrImg()