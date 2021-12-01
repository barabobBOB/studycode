"""
opp로 진행예정 —> 한 클래스당 한 프로세스

셀레니움 클래스(함수) / url 클래스 / 이미지 클래스 / html 클래스 
(어차피 스레드가 아니여서 공유자원 사용 불가능 그래서 클래스를 지정하려고 함)
"""
from selenium import webdriver
from bs4 import BeautifulSoup
import time

#options = webdriver.ChromeOptions()
#options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome("C:/Users/chltp/Desktop/새 폴더/homework/chromedriver.exe")
class selenium:
    def search_word(self, word):
        # 접속할 url
        url = "https://www.google.com"
        driver.get(url)
        # 웹페이지가 로딩되기까지 기다림
        time.sleep(0.5) ## 0.5초

        # driver.find_element_by_name(<element의 name>).send_keys(<검색어>) 
        element = driver.find_element_by_name('q')
        element.send_keys(word)
        element.submit()


    def scoll():
        pass

class html:
    pass

def html_get():
    # 드라이버 현재 페이지의 html 정보 가져오기 
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    return soup

class url_get(selenium):
    def url_search():
        pass

class img_save(selenium):
    def img_search():
        pass
