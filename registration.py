import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017")
print("connected")
db = client["registration"]
collection = db["names"]


print(client.list_database_names())
user_data = client["users"]
user_collection = user_data["user_info"]
def user_registration():
    user_details ={ }
    user_name = input("Enter user name :")
    password = input("Enter password:")
    user_details['user_name']=user_name
    user_details['password']=password
    x = user_collection.insert_one( user_details)
    print(user_details)
user_registration()




   



 

#