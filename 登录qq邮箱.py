from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get("https://mail.qq.com/")

#登录
handles=browser.window_handles
# browser.switch_to.window(handles[1])
browser.switch_to.frame(browser.find_element(By.ID,"login_frame"))
browser.find_element(By.CSS_SELECTOR,"[id=u]").send_keys("2601696779")
browser.find_element(By.ID,"p").send_keys("Wyy020115")
browser.find_element(By.CSS_SELECTOR,".login_button [id=login_button]").click()