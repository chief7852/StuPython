from pymongo import MongoClient 
my_client = MongoClient("mongodb://localhost:27017/")

mydb = my_client['test'] 
mycol = mydb['customers'] 

my_query = {"address":"Dongjakgu, Seoul"}
my_doc = mycol.find()
# my_doc = mycol.find(my_query)
for x in my_doc:
    print(x)

