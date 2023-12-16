import requests
from bs4 import BeautifulSoup
import time

stock = ["00919", "3147", "2330"]  # 要爬股票
for i in range(len(stock)):  # 迴圈
    stockid = stock[i]  # 把股票塞入 0>1
    url = "https://tw.stock.yahoo.com/quote/" + stockid + ".TW"  # 上市
    r = requests.get(url)  # 爬HTML
    soup = BeautifulSoup(r.text, 'html.parser')  # 解析HTML
    
    # 根據Tag,Class取得股票名稱
    name_element = soup.find('h1', class_='C($c-link-text) Fw(b) Fz(24px) Mend(8px)')

    name = name_element.text if name_element else "無法取得名稱"
    
    # 根據Tag,Class取得股價
    price_element = soup.find("span", class_=["Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)",
                                              "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)",
                                              "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)"
                                              ])
    
    time.sleep(0.5)
    
    if price_element is None:  # 如果找不到資料
        url = "https://tw.stock.yahoo.com/quote/" + stockid + ".TWO"  # 上櫃
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        price_element = soup.find("span", class_=["Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)",
                                                  "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)",
                                                  "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)"
                                                  ])
    
    price = price_element.text if price_element else "無法取得價格"  # 轉成文本

    message = f"{name} {stockid}的價格為: {price}"  # 回傳得訊息
    print(message)

    token = "MTE4NTUyODYyODE0NzEyNjMyMg.GeusqA.CgrOnMIfF55h33PkrXXSHTq0s4GCbTBZ0EpV6A" #bot token
    chat_id = "1185528628147126322" #使用者id
    #url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}" #發送訊息
    url = f"https://discord.com/api/webhooks/{chat_id}/{token}"
    requests.get(url)
    time.sleep(3)

