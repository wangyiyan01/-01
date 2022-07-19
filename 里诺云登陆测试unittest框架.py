import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class testLogin(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get("http://t.lenoyun.com/yck/public/login")
        self.browser.implicitly_wait(20)

    def Login(self,user,password):
        self.browser.find_element(By.ID,"username").clear()
        self.browser.find_element(By.ID, "username").send_keys(user)
        self.browser.find_element(By.ID, "password").clear()
        self.browser.find_element(By.ID, "password").send_keys(password)
        self.browser.execute_script("arguments[0].click();", self.browser.find_element(By.ID, "btnOk"))
    def Load(self):
        loading = self.browser.find_element(By.CSS_SELECTOR, "div.ok-loading")
        WebDriverWait(self.browser,20).until(expected_conditions.invisibility_of_element(loading))
        self.browser.find_element(By.LINK_TEXT, "我知道啦").click()

    def test1(self):
        self.Login('admin', '123456')
        self.Load()
        try:
            msg = self.browser.find_element(By.CLASS_NAME, "userName").text
        except:
            msg = ""
        assert 'admin' in msg

    def test2(self):
        self.Login('admin1', '123456')
        try:
            msg = self.browser.find_element(By.CLASS_NAME, "layui-layer-content.layui-layer-padding").text
        except:
            msg = None
        assert msg == "用户名或密码错误"

    def tearDown(self):
        self.browser.quit()
