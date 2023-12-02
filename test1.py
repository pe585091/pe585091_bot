import requests
from bs4 import BeautifulSoup
import time

stock = ["00929","2618","2330"] #要爬股票
for i in range(len(stock)): #迴圈
  stockid = stock[i] #把股票塞入 0>1
  url = "https://tw.stock.yahoo.com/quote/"+stockid+".TW" #上市
  r = requests.get(url) #爬HTML
  soup= BeautifulSoup(r.text, 'html.parser') #解析HTML
  price = soup.find("span", class_=["Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)",
                                    "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)",
                                    "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)"
                                   ]
                    )   #根據Tag,Class取得股價
                   
 
  time.sleep(0.5)
  if price == None: #如果找不到資料
    url = "https://tw.stock.yahoo.com/quote/"+stockid+".TWO" #上櫃
    r = requests.get(url)
    soup= BeautifulSoup(r.text, 'html.parser')
    price = soup.find("span", class_=["Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)",
                                      "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)",
                                      "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)"
                                     ]
                     
                      )
  price = price.getText() #轉成文本
  
  message = "股票" +stockid + "的價格為: " + price #回傳得訊息
  token = "6533554806:AAEH45JruGFyxmf24_ZpsBBhfK_wIJ0Q7Zc" #bot token
  chat_id = "6910898574" #使用者id
  url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}" #發送訊息
  requests.get(url)
  time.sleep(3)
