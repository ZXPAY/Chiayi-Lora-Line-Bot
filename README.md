# Line-bot
![alt tag](https://i.imgur.com/uibqf3M.jpg)

## 嘉義飛漁 Line-Bot說明
#### 此line-bot為一互動式聊天機器人，將嘉義大學室內和室外的資料呈現給使用者，讓使用者能用習慣的手機app-line，去得知目前的溫度、濕度、二氧化碳、空氣微粒等等資料。
![alt tag](https://i.imgur.com/w10BJAF.jpg)

### 我的 QRCODE
![alt tag](https://i.imgur.com/XE8TYCr.png)

### Github: https://github.com/ZXPAY

## 打招呼熱詞
#### 問候：'你好', '妳好','您好', 'hello', 'hi'
#### 安安：'安', '安安', 'how are you'
#### 早安：'早安', '早', 'morning'
#### 午安：'午安', 'good afternoon'
#### 晚安：'晚安', 'good evening', 'good night'
#### 誇獎：'棒', 'great', 'awesome', '強', '猛'
#### 隱藏版：使用者自行嘗試

## 指令索引資料說明
#### 索引結構:
#### 第一行：i(編號)參數
#### 第二行：參數,運算符號,數值
#### 第三行：…
#####  i是索引室內資料庫,o是索引室外資料庫
#####  編號為資料庫編號
#####  參數為使用者所要索引的目標,例如:溫度、濕度等
#####  運算符號為索引的方式,例如:<=,<=
#####  數值為使用想要的範圍
#### PS:結尾不能有","

### 範例1:
#### i1溫度
#### 溫度,>=,28
#### 溫度,<=,30
#### 索引室內資料庫一溫度介於28到30度的溫度數值和發生時間

### 範例2:
#### o2溫度
#### 時間,>=,2018-05-10 12:00:00
#### 時間,<=,2018-05-10 12:05:00
#### 索引室外資料庫二05/10 12:00~12:05分的溫度數值


##   Indoor:
#### Temperature         (TS) 溫度(°C)
#### Humidity            (HS) 濕度(%)
#### CO                  (CS) 一氧化碳(ppm)
#### CO2                 (IS) 二氧化碳(ppm)
#### LPG                 (LS) 液化石油氣(ppm)
#### PM                  (MS) 空氣微粒(μg/m³)

##    Outdoor:
#### Temperature         (TS) 溫度(°C)
#### Humidity            (HS) 濕度(%)
#### CO2                 (IS) 二氧化碳(ppm)
#### PM                  (MS) 空氣微粒(μg/m³)
#### Atmospheric Press   (AS) 大氣壓力(pa)
#### altitude, Longitude (DNS) (DNLIST) 經緯度

## Deploy
#### $git add .
#### $git commit -m "name"
#### $git push heroku master

## 刪除之前的檔案，重新上傳
#### $heroku plugins:install heroku-repo
#### $heroku repo:purge_cache -a APPNAME
