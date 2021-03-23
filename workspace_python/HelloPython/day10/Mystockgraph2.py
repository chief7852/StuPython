from pymongo import MongoClient 
import pymongo

def getPrices(s_name):
    arr = []
    connection = pymongo.MongoClient("mongodb://localhost:27017/")
    db = connection.test
    stock = db.stock
    
    rows = stock.find({'s_name':s_name}).sort('in_date',1)
    first_price = rows[0]['s_price']
    for r in rows:
        int_s_price = int(r['s_price'])/int(first_price)
        arr.append(int_s_price)
        return arr
    
if __name__ == '__main__':
    arr = getPrices('계룡건설')
    print(arr)