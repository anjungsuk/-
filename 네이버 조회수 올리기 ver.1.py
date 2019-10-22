from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, time
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains

options= webdriver.ChromeOptions()
driver = webdriver.Chrome()

options.add_argument("disable-gpu")   # 가속 사용 x
options.add_argument("lang=ko_KR")    # 가짜 플러그인 탑재

driver.get("https://www.naver.com") #네이버 검색 주소창
print(driver.window_handles)
clicka = 0

text1 = input('검색어를 입력해주세요: ')

#첫번째 검색부
elem = driver.find_element_by_id("query") #네이버 검색 부
elem.send_keys(text1) #초기에 입력한 내용들 전달받는값
sleep(5)
elem = driver.find_element_by_id("search_btn")
elem.click()
sleep(3)
driver.find_element_by_css_selector('li.lnb6 > a').click()
sleep(10)
continue_link=driver.find_element_by_partial_link_text(text1) # 검색구문 확인후 링크로 이동 하는 부분
continue_link.click()
sleep(10)

while True :
    driver.switch_to_window(driver.window_handles[1])
    driver.refresh()
    sleep(180)

