from pymongo import MongoClient 
import re
import datetime  
import requests
from bs4 import BeautifulSoup
import time

def insertStock(s_code,s_name,s_price,yyyymmdd_hhmm):
    connection = MongoClient("mongodb://localhost:27017/")
    db = connection.pyhon
    
    stock = db.stock
    
    
    doc = {"s_code":s_code, "s_name":s_name, "s_price":s_price, 'in_date':yyyymmdd_hhmm}
    stock.insert_one(doc)


for i in range(10):
    print("i",i)
    response = requests.get('https://www.sedaily.com/Stock/Quote/?mobile')
    text = response.text
    soup = BeautifulSoup(text,'html.parser')
    yyyymmdd_hhmm = datetime.datetime.now().strftime('%Y%m%d.%H%M')
    
    for info in soup.select('.tbody'):
        
        s_name = info.dt.text
        price = info.dd.span.text
        s_price = info.dd.span.text.replace(",","")
        s_code_text = info.dd['id']
        s_code = s_code_text[len(s_code_text)-6:len(s_code_text)] 
        insertStock(s_code, s_name, s_price,yyyymmdd_hhmm)
    time.sleep(60)
