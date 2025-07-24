import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}
url = "https://www.melon.com/chart/index.htm"

req = requests.get('https://www.melon.com/chart/index.htm',headers=header_user) 
html = req.text

soup = BeautifulSoup(html, 'html.parser')

lst50 = soup.select(".lst50")
lst100 = soup.select(".lst100")
lstall = lst50 + lst100

for rank, i in enumerate (lstall, 1):
    title = i.select_one(".ellipsis.rank01 a").text
    singer = i.select_one(".ellipsis.rank02 a").text        
    album = i.select_one(".ellipsis.rank03 a").text
    print(f'[ㄹㅋ]: {rank}')
    print(f"[ㅈㅁ]: {title}")
    print(f"[ㄳ]: {singer}")
    print(f"[ㅇㅂ]: {album}")
    print('===============')