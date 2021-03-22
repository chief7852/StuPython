from pymongo import MongoClient 
import pandas as pd

my_client = MongoClient("mongodb://localhost:27017/")

print(my_client.list_database_names())
mydb = my_client['test'] 
mycol = mydb['customers'] 
x = mycol.update({"address":"col013"}) 
print(x.update_id)
