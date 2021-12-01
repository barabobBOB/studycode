"""
Multithreading 이용해서 URL 가져오기
100개 초과 1000개 미만으로 URL 가져와서 csv에 저장하기 

metex 사용 과도한 thread 선점은 피하기 결합도 낮춰서 만드세요
"""
# 네이버 뉴스 URL 크롤링

import time
import threading
from queue import Queue
import csv

from bs4 import BeautifulSoup
from selenium import webdriver

# driver
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome("C:/Users/chltp/Desktop/새 폴더/homework/chromedriver.exe", options=options)

csv__file = "C:/Users/chltp/Desktop/URL"

url = "https://news.naver.com/"

"""
1. 크롤링하는 것과 저장하는 걸 따로 쓰레드를 두자
큐를 이용해 긁어온 URL을 넣고 빼서 CSV 파일로 저장
제목까지 저장? -> 다 짜고 고려
"""
# //*[@id="sp_nws1"]/div[1]/div/a
# //*[@id="sp_nws6"]/div[1]/div/a
# //*[@id="sp_nws10"]/div[1]/div/a

def search():
    driver.get(url)
    # 웹페이지가 로딩되기까지 시간이 필요해서 sleep을 이용해서 조금 기다립니다.
    time.sleep(0.5) # 0.5초
    element = driver.find_element_by_name('query')
    element.send_keys("it")
    element.submit()

def web_html():
    search()
    req = driver.page_source
    soup = BeautifulSoup(req, 'html.parser')
    articles = soup.select('#main_pack > div.news.mynews.section._prs_nws > ul > li')

    for article in articles:
        a_tag = article.select_one('dl > dt > a')

        title = a_tag.text
        url = a_tag['href']
        print(title, url)

def csv_save(url):
    """
    rows = zip(title_list,article)
    with open('naver_news_covid19.csv','w',encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['title','paragraphs'])
    for row in rows:
        writer.writerow(row)
    """

#=======================================================================================================

if __name__ == "__main__":
    web_html()
    """
    i = input()

    q = Queue()
    t1 = threading.Thread(target=sender, args=(q, ))
    t2 = threading.Thread(target=reciver, args=(q, ))

    t1.start()
    t2.start()
    """