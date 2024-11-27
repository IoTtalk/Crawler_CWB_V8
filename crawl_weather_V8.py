# coding: utf-8
from bs4 import BeautifulSoup
from selenium import webdriver
import datetime

date = []
temp = []
weather = []
wind_direction = []
wind_speed = []
gust_wind = []
visible = []
hum = []
pre = []
rain = []
sunlight = []

region = 'Tainan'
#台南測站觀測資料
url = 'https://www.cwa.gov.tw/V8/C/W/OBS_Station.html?ID=46741'

#啟動模擬瀏覽器
driver = webdriver.Chrome()
#driver = webdriver.Chrome(executable_path=r"實際chromedriver所在位置，例如C:\Chrome\chromedriver.exe")

#取得網頁代碼
driver.get(url)
open(region+'.html','wb').write(driver.page_source.encode('utf-8'))


#指定 lxml 作為解析器
soup = BeautifulSoup(driver.page_source, features='lxml')

# <tbody id='obstime'> 抓過去24小時資料
tbody = soup.find('tbody',{'id':'obstime'})

# <tbody>内所有<tr>標籤
trs = tbody.find_all('tr')

# 使用datetime取得時間年分
year = str(datetime.datetime.now().year)

# #對list中的每一項 <tr>
for tr in trs:
#   取時間, <tr>內的<th>, <th>內為時間 月/日<br>時:分
    d = tr.th.text
    d = year + d
#   字串轉為datetime格式
    date.append(datetime.datetime.strptime(d, '%Y%m/%d %H:%M'))
    temp.append(tr.find('td',{'headers':'temp'}).text)
    w_img=tr.find('td',{'headers':'weather'}).find('img')
    if w_img: weather.append(w_img['title'])  
    else: weather.append('-')      
    wind_direction.append(tr.find('td',{'headers':'w-1'}).text)
    wind_speed.append(tr.find('td',{'headers':'w-2'}).text)
    gust_wind.append(tr.find('td',{'headers':'w-3'}).text)
    visible.append(tr.find('td',{'headers':'visible-1'}).text)
    hum.append(tr.find('td',{'headers':'hum'}).text)
    pre.append(tr.find('td',{'headers':'pre'}).text)
    rain.append(tr.find('td',{'headers':'rain'}).text)
    sunlight.append(tr.find('td',{'headers':'sunlight'}).text)

#關閉模擬瀏覽器       
driver.quit()
# ---------------------------------------------------------------
import pandas as pd

table = {
"觀測時間":date,
"溫度(°C)":temp,
"天氣":weather,
"風向":wind_direction,
"風力 (m/s)":wind_speed,
"陣風 (m/s)":gust_wind,
"能見度(公里)":visible,
"相對溼度(%)":hum,
"海平面氣壓(百帕)":pre,
"當日累積雨量(毫米)":rain,
"日照時數(小時)":sunlight
}

df = pd.DataFrame(table)
df = df.reset_index(drop=True)    
df.to_csv(( region + '.csv'), encoding = 'utf-8')
