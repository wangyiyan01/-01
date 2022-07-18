from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get("https://www.baidu.com")
browser.find_element(By.ID,"kw").send_keys("重庆")
browser.find_element(By.ID,"su").click()

# browser.find_element(By.XPATH,"//a[@href='https://www.baidu.com/link?url=CtcBNR9d1vUu6tTnjltoXRW6L_zDQkS1xTe_j5hOb6N-C76gRUDxQiJw0eiIGp91b76-hchj2Ia2gGfJjAIcUGdsnallPDCSF7zwhhk7EucL8_8ONFtB96PRyjVroijbQd6AEcLyzr3TOnpRJSqFMLv8eQKG-AzpU0_aNxnl4Xm&wd=&eqid=e3e7f20b000bf3030000000562d3b374']").click()
browser.find_element(By.PARTIAL_LINK_TEXT,"重庆市地图_百度地图").click()
handles=browser.window_handles
browser.switch_to.window(handles[1])
browser.find_element(By.NAME,"userName").send_keys("重庆的兔斯基")  #登录百度账号
browser.find_element(By.CLASS_NAME,"pass-text-input.pass-text-input-password").send_keys("5137642")
browser.find_element(By.XPATH,"//form[@class='pass-form pass-form-normal']//input[@type='submit']").click()
browser.find_element(By.ID,"sole-input").clear()
browser.find_element(By.ID,"sole-input").send_keys("重庆渝北回兴")
browser.find_element(By.ID,"search-button").click()