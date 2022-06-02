import json
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(3)
time.sleep(1)
driver.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cnt&date=20220601')

mvTitle = []
mvUrl = []
mvCode = []

time.sleep(1)
soup = BeautifulSoup(driver.page_source, 'html.parser')
movieList = soup.select_one('#old_content')
trList = movieList.select('div.tit3 > a')
for list in trList:
    mvTitle.append(list.text)
    mvUrl.append(list.attrs['href'])
    mvCode.append(list.attrs['href'][-6:].strip('='))

#     for ranNm in ranNmList:
#         ranLiNm.append(ranNm.text)
#     ranNumList = ranList.select('div.num > em')
#     for ranNum in ranNumList:
#         ranLiNum.append(ranNum.text)
#     ranIdList = ranList.select('span.bj_id')
#     for ranId in ranIdList:
#         ranUrl.append('https://bj.afreecatv.com/{0}'.format(ranId.text))
#
# # print(ranUrl)
# # rankAll.append([ranLiNm, ranLiNum, ranUrl])
# # print(rankAll)
# with open('AF_rank.txt', "wt", encoding="utf-8") as f:
#     for i in range(len(ranLiNm)):
#         f.write((str(['Rk: ', ranLiNum[i], ' | Nm: ', ranLiNm[i], ' | Url: ', ranUrl[i]])+'\n').replace("', '", ""))

