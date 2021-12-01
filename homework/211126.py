"""
다중 스레드로  이미지 크롤링을 진행해보자 
이미지 저장까지 함수형으로 프로그래밍 한다음

클래스 형으로 리팩토링 진행 하면서 mutex 가 생길 시 
극복하는 코드도 함께 작성할것 
---
우리가 전에 만들었던 게임 코드중 몬스터 객체를 선언하는 코드와 
아이템을 사고 파는 장비를 장착 착용효과 코드가 있을것이다 
멀티 프로세싱과 스레드를(둘다 이용해야함) 이용해서 몬스터 객체코드와 아이템을 장착 사고파는 코드를 합쳐서 하나의 코드를 만들거나 객체간 협력을 하도록 만들고 된다면 각 프로세스가 어떻게 돌아가는지 설명하라. 
안된다면 왜 안되는지 설명해서 리포트다 주석으로 설명하세요
"""

from os import times
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from urllib.parse import quote_plus
import urllib.request
from urllib.request import urlretrieve

def html_search():
    plusUrl = input('검색어 입력: ')
    baseUrl = "https://www.google.com/search?q={}&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjgwPKzqtXuAhWW62EKHRjtBvcQ_AUoAXoECBEQAw&biw=768&bih=712".format(plusUrl)
    crawl_num = int(input('크롤링할 갯수 입력: '))
    #url = baseUrl + quote_plus(plusUrl) # 한글 검색 자동 변환
    headers = {'User-Agent':'Chrome/96.0.4664.45'}
    req = urllib.request.Request(baseUrl, headers=headers)
    html = urllib.request.urlopen(req)
    soup = bs(html, "html.parser")
    return soup, crawl_num

def img_crawling():
    soup, crawl_num = html_search()
    #img = soup.find_all('img')
    img_url = []
    for img in soup.find_all("img"):
        img_url.append(img.get("src"))
    print(img_url)
    
    #이후 안됨
    img_url.pop(0)
    
    for imgurl in img_url:
        n = 1
        savename = str(n) + ".jpg"
        urlretrieve(imgurl, savename)
        n += 1
        if n == crawl_num:
            break
    
"""    
    n = 1
    for i in img:
        print(n)
        imgUrl = i['data-source']
        with urlopen(imgUrl) as f:
            with open('./img/' + str(n)+'.jpg','wb') as h: # w - write b - binary
                img = f.read()
                h.write(img)
        n += 1
        if n > crawl_num:
            print('Image Crawling is done.')
            break
"""
   
def img_save():
    pass

if __name__=="__main__":
    img_crawling()