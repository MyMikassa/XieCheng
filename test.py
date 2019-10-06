from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
driver = webdriver.Firefox()
driver.get("https://flights.ctrip.com/itinerary/oneway/BJS-SHA,SHA?date=2019-9-28")

while True:
    try:
        driver.find_element_by_xpath("//*[@class='page_neighbor']")
        print("Yes")
        break
    except:
        js = "var q=document.documentElement.scrollTop=100000"
        driver.execute_script(js)

#
# print("hello world")
#
# # for i in range(2, 100):
# #     js="var q=document.documentElement.scrollTop={}".format(i*100)
# #     driver.execute_script(js)
# # wait = WebDriverWait(driver, 10)
# # wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='arrow_left']")))
#
# # time.sleep(3)
#
# #
# # text = driver.find_elements_by_class_name("search_table_header")
# #
# # print(len(text))
# # for i in text:
# #     print(i.text)


