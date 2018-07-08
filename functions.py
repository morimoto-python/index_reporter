# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 08:58:26 2018

@author: morim
"""

#各指標をウェブスクレイピングして値を返す関数群

import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import os
import datetime

os.chdir(os.path.abspath("."))

def nikkei_stock_average():
    #日経平均株価
    html = urlopen("https://indexes.nikkei.co.jp/nkave/archives/data")
    data = html.read()
    html = data.decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    date = soup.find_all("td",class_="col-xs-12 col-sm-2 list-row-dashed list-date") 
    price = soup.find_all("td", class_="col-xs-6 col-sm-2_5 list-row-dashed list-value")
    a= "日経平均株価（{0}）：".format(date[-1].string.replace(".","/"))
    return("{0:<25}{1}".format(a, float(price[-1].string.replace(',', ""))))
    

def n_day_before():
    #日経前日比
    html = urlopen("https://indexes.nikkei.co.jp/nkave/archives/data")
    data = html.read()
    html = data.decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    date = soup.find_all("td",class_="col-xs-12 col-sm-2 list-row-dashed list-date") 
    price = soup.find_all("td", class_="col-xs-6 col-sm-2_5 list-row-dashed list-value")
    b= "日経平均前日比："
    day_before= float(price[-1].string.replace(',', "")) - float(price[-5].string.replace(',', ""))
    
    if day_before > 0:
        return("{0:<25}+{1:.2f}".format(b, float(price[-1].string.replace(',', "")) - float(price[-5].string.replace(',', ""))))
    else:
        return("{0:<25}▲{1:.2f}".format(b, float(price[-5].string.replace(',', "")) - float(price[-1].string.replace(',', ""))))

"""
#月初
def n_day_before():
    
    last_price= 22201.82
    
    html = urlopen("https://indexes.nikkei.co.jp/nkave/archives/data")
    data = html.read()
    html = data.decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    date = soup.find_all("td",class_="col-xs-12 col-sm-2 list-row-dashed list-date") 
    price = soup.find_all("td", class_="col-xs-6 col-sm-2_5 list-row-dashed list-value")
    b= "日経平均前日比："
    day_before= float(price[-1].string.replace(',', "")) - last_price
    
    if day_before > 0:
        return("{0:<25}+{1:.2f}".format(b, float(price[-1].string.replace(',', "")) - last_price))
    else:
        return("{0:<25}▲{1:.2f}".format(b, float(price[-1].string.replace(',', "")) - last_price))
"""

def oil_price():
    #ドバイ原油価格
    html = urlopen("https://www.nikkei.com/markets/shohin/page/?uah=DF_SEC8_C4_110")
    data = html.read()
    html = data.decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    oil_price = soup.find_all("span",class_="cmnc-middle") 
    oil_date = soup.find_all("div", class_="l-miH02_date")
    
    title= oil_price[0].text
    
    a= title.split(" ")
    
    if len(a)==1:
        b= a[0].split("\u3000")
        #text= b[0].replace("ドル前後","")
        text= b[1].replace("ドル前後","")
    
    else:
        text= a[1].replace("ドル前後","")
        
    result= "ドバイ原油（{}）：".format(oil_date[0].text.replace("2018年","").replace("月","/").replace("日","/"))
    return("{0:<25}{1}".format(result, text))

def f_stock():
    #FFG株価
    html = urlopen("https://stocks.finance.yahoo.co.jp/stocks/detail/?code=8354")
    data = html.read()
    html = data.decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    f_price = soup.find_all("dd",class_="ymuiEditLink mar0") 
    f_date = soup.find_all("span", class_="date yjSt")

    strong = f_price[0].find("strong")
    text = strong.text
    a= "ふくおかFG株価{}：".format(f_date[0].text)
    return("{0:<25}{1} 円".format(a, text.strip()))
    #証券取引所は土日休みなので、土日は変化なし

def reit():
    #東証REIT指数
    html = urlopen("https://quote.jpx.co.jp/jpx/template/quote.cgi?F=tmp/real_index&QCODE=155")
    data = html.read()
    html = data.decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    reit = soup.find_all("td",class_="a-center va-middle tb-separated") 
    reit2= []
    for p in reit:
        reit2.append(p.text)
    a= "東証REIT指数（{}）：".format(reit2[0].strip())
    return("{0:<25}{1}".format(a, reit2[4].replace("(15:00)","").strip()))

def interest_rate():
    #長期金利
    html = urlopen("https://www.nikkei.com/markets/worldidx/")
    data = html.read()
    html = data.decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    rate = soup.find_all("table", class_ ="cmn-table_style1")
    
    
    a= "長期金利（{}）：".format(rate[3].find_all("td")[2].text.strip())
    return("{0:<25}{1}".format(a, rate[3].find("td").text.strip()))

def exchange():
    #ドル円為替相場
    html = urlopen("https://www.nikkei.com/markets/kawase/")
    data = html.read()
    html = data.decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    rate = soup.find_all("div",class_= "mkc-stock_prices")
    a= "ドル円相場（{}）：".format("今日")
    return("{0:<25}  {1} 円".format(a, rate[0].text))    