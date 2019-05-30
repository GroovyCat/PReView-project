## 1. 웹크롤링을 위한 웹드라이버 응용 2
from selenium import webdriver
from bs4 import BeautifulSoup # 웹페이지 내용구조 해석
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains #contril click in selenium
import math #math 모듈을 먼저 import해야 한다.
from time import sleep 
 
driver = webdriver.Chrome('/Users/wkddn/Documents/crawling/ChromeDriver 74.0.3729.6/chromedriver')
#driver = webdriver.PhantomJS('/Users\/kddn/Documents/crawling/phantomjs-2.1.1-windows/bin/phantomjs')
driver.implicitly_wait(3)
# url에 접근한다.

driver.get('https://www.naver.com/') #네이버로 이동
#웹드라이버를 사용하여 (검색과 사이트 이동(click))

elem=driver.find_element_by_name("query").send_keys('악인전') #검색창에 악인전 검색
driver.find_element_by_xpath('//*[@id="search_btn"]/span[2]').click() 
#신규텝으로 이동 / 드라이버는 위치는 기존유지

