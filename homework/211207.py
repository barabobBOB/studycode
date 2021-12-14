from os import times
import multiprocessing

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote_plus
from urllib.request import urlretrieve, urlparse
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

search = input('검색어를 입력하세요: ')
num = int(input ('다운로드 받고 싶은 이미지의 갯수를 입력하세요: '))

def img_crawling(url):
    cp = multiprocessing.current_process()
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome("C:/Users/chltp/Documents/GitHub/studycode/homework/chromedriver.exe", chrome_options=options)
    driver.get(url)
    elem = driver.find_element_by_name("q") 
    elem.send_keys(str(search))
    elem.send_keys(Keys.RETURN)
    if num>=50:
        SCROLL_PAUSE_TIME = 1.5
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                try:
                    driver.find_element_by_css_selector(".mye4qd").click()
                except:
                    break
            last_height = new_height
    images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")

    count = 1
    for image in images:
        try:
            image.click()  
            time.sleep(1)
            imgURL=driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img").get_attribute("src")
            urlretrieve(imgURL , str(search) + str(count) + ".jpg")
            count = count + 1
        except:
            pass
        if count == int(num)+1:
            break

    driver.close()

def url_addition(url_noting, url_):
    def url_feature():
        return f"{urlparse(url_).scheme}://{urlparse(url_).netloc}/"

    fu = url_feature()+url_noting if url_noting.startswith('/') else url_noting

    return fu

def url_crawling(url):
    cp = multiprocessing.current_process()
    url = url + search
    req = requests.get(url, verify=False)
    soup = BeautifulSoup(req.content, 'lxml')
    URL_TEXT_DATA = []
    URL_HREF_DATA = []

    for div_data in soup.find_all("a"):
        time.sleep(2)
        href_data = div_data['href']

        # 필요없는 # 이나 도중에 짤린 URL 붙히기
        if href_data == "#":
            continue
        if href_data.startswith('/'):
            print(url_addition(href_data))
            URL_HREF_DATA.append(url_addition(href_data, url))
            URL_TEXT_DATA.append(div_data.text)

    print(URL_HREF_DATA)
"""    for i in soup.find_all('a'):
        time.sleep(3)
        url_list.append(i['href'])

    print(url_list)
"""
def multi_processing():
    url_ = ["https://www.google.co.kr/imghp?hl=ko", "https://www.google.com/search?q="]
    p1 = multiprocessing.Process(target=img_crawling, args=(url_[0], ))
    p2 = multiprocessing.Process(target=url_crawling, args=(url_[1], ))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__=="__main__":
    #img_crawling("https://www.google.co.kr/imghp?hl=ko&tab=wi&ogbl")
    url_crawling("https://www.google.com/search?q=")
    #multi_processing()