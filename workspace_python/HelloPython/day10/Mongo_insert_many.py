from pymongo import MongoClient 
import pandas as pd 
my_client = MongoClient("mongodb://localhost:27017/") 
print(my_client.list_database_names()) 
mydb = my_client['test'] 
mycol = mydb['customers'] 
my_dict = [{"name":"PUTTY", "address":"SSH World, Network"}, 
           {"name":"donghyunjang", "address":"Seoul, Korea"}, 
           {"name":"Avengers", "address":"Avengers Team Building, USA"}] 
x = mycol.insert_many(my_dict) 
print(x.inserted_ids)
