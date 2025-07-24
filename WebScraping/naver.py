from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

keyword = input("검색어를 입력하세요: ")
header_user = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}
url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=" + keyword

options = Options()
options.add_experimental_option('detach',True) 

driver = webdriver.Chrome(options=options)
driver.get(url)
time.sleep(2)

### for문은 range 지정, while문은 스크롤이 더이상 되지 않는 지 확인 후 종료

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

results = soup.select(".view_wrap")
print(len(results))
for i in results:
    title = i.select_one(".title_link").text
    link = i.select_one(".title_link")['href']
    writer = i.select_one(".name").text
    dsc = i.select_one(".dsc_link").text
    print(f"[제목]: {title}")
    print(f"[링크]: {link}")
    print(f"[작가]: {writer}")
    print(f"[설명]: {dsc}")
    print('====================')

driver.quit()
