from os import times
import multiprocessing

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote_plus
from urllib.request import urlretrieve 
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#, chrome_options=options)

def html_get():
    search = input ('검색어를 입력하세요: ')

    num = int(input ('다운로드 받고 싶은 이미지의 갯수를 입력하세요: '))

    options = webdriver.ChromeOptions()

    options.add_argument('--ignore-certificate-errors')

    options.add_argument('--ignore-ssl-errors')

    driver = webdriver.Chrome("C:/Users/chltp/Documents/GitHub/studycode/homework/chromedriver.exe", chrome_options=options)

    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&ogbl")

    elem = driver.find_element_by_name("q") 

    elem.send_keys(str(search))

    elem.send_keys(Keys.RETURN) 

    if num>=50:

        SCROLL_PAUSE_TIME = 1.5

        # Get scroll height

        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:

            # Scroll down to bottom

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page

            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height

            new_height = driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:

                try:

                    driver.find_element_by_css_selector(".mye4qd").click()

                except:

                    break

            last_height = new_height

    count = 1

    images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")

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
    """
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome("C:/Users/chltp/Documents/GitHub/studycode/homework/chromedriver.exe", chrome_options=options)
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&ogbl")
    elem = driver.find_element_by_name("q") 
    elem.send_keys(str(word))
    elem.send_keys(Keys.RETURN)

        headers = {'Content-Type': 'application/json; charset = utf-8'} 
    cookies = {'id': 'WJEJGJ9231M1RR2OP'}
    html = requests.get(url, headers=headers, cookies=cookies)
    # 웹 페이지 로딩 시간
    time.sleep(1)
    soup = BeautifulSoup(html.content, "lxml")
    print(soup)
    return soup
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

    #cp = multiprocessing.current_process()
    count = 1
    for image in images:
        try:
            image.click()  
            time.sleep(1)
            imgURL=driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img").get_attribute("src")
            urlretrieve(imgURL , "./img/" + str(word) + str(count) + ".jpg")
            count = count + 1
        except:
            pass
        if count == int(word)+1:
            break

    
    for num in range(10):
            images = driver.find_elements_by_xpath(f'//*[@id="islrg"]/div[1]/div[{num}]/a[1]/div[1]')
            for image in images:
                image.click()
                time.sleep(2)
                url_img = driver.find_element_by_xpath(f'//*[@id="islrg"]/div[1]/'
                                                       f'div[{num}]/a[1]/div[1]/img').get_attribute('src')
                img_url.append(url_img)
    
    for img in soup.find_all("img"):
        img_url.append(img.get("src"))
    print(img_url)
    # 첫번째 필요없는 url 삭제 
    # img_url.pop(0)
    n = 1    
    for imgurl in img_url:
        savename = str(n) + ".jpg"
        urlretrieve(imgurl, "./img/"+savename)
        time.sleep(1)
        n += 1
    """
def url_html_search(plusUrl):
    #cp = multiprocessing.current_process()
    baseUrl = "https://www.google.com/"
    #elem = driver.find_element_by_name("q")
   #elem.send_keys("치킨")
    #elem.send_keys(Keys.RETURN)

def url_crawling():
    url = []
    soup = url_html_search()
    #img = soup.find_all('img')
    url_list = []
    for i in soup.find_all('a'):
        for j in i.find('href'):
            url_list.append(j)
    print(url_list)

if __name__=="__main__":
    html_get()
"""    p1 = multiprocessing.Process(target=url_crawling, args=())
    p2 = multiprocessing.Process(target=img_crawling, args=())

    p1.start()
    p2.start()

    p1.join()
    p2.join()"""