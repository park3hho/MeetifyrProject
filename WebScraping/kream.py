from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By ### Find CSS Selector Class 
from selenium.webdriver.common.keys import Keys ### Keyboard Event
from selenium.webdriver.common.action_chains import ActionChains ### Mouse Event
import time
import pymysql

header_user = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}
url = "https://kream.co.kr/"
options = Options()
options.add_experimental_option('detach',True) 
options.add_argument(f'User-Agent={header_user}')

driver = webdriver.Chrome(options=options)
driver.get(url)
time.sleep(1.002)

driver.find_element(By.CSS_SELECTOR, ".btn_search.header-search-button.search-button-margin").click()
time.sleep(1.003)

driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys("스투시")
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(Keys.ENTER)

for i in range(20):
    driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

items = soup.select(".item_inner")

product_list = [] ## [[1,2,3],[4,5,6]]

for item in items:
    title = item.select_one(".translated_name").text
##    price = item.select_one(".item_price").text
##    link = item.select_one(".item_link")['href']
    if '후드' in title:
        category = "상의"
        product_brand = item.select_one(".brand-name").text
        product_price = item.select_one(".amount").text

        product = [title,category ,product_brand, product_price]
        product_list.append(product)
        print(f"[제목]: {title}")
        print(f"[브랜드]: {product_brand}")
        print(f"[가격]: {product_price}")
    ##    print(f"[가격]: {price}")
    ##    print(f"[링크]: {link}")
        print('====================')
    
driver.quit()
# driver.quit()

connection = pymysql.connect(
    host='localhost', 
    user='root',
    password='As583346!@',
    db='kream',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

def execute_query(connection, query, args=None):
    with connection.cursor() as cursor:
        cursor.execute(query,args or ())  ## 쿼리문에 ?가 없으므로 ()로 대체
        if query.strip().upper().startswith("SELECT"):
            return cursor.fetchall()
        else:
            connection.commit()
    
for product in product_list:
    execute_query(connection, "INSERT INTO produts (category, brand, product_name, price) VALUES (%s, %s, %s, %s)", (product[0], product[1], product[2], product[3]))