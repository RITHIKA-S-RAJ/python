import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017")
# print(client.list_database_names())
db=client["class"]
collection=db["Details"]

# student_2={
#     "Name":"Rohit",
#     "Age":21,
#     "Adm_No":2
# }
# collection.insert_one(student_2)

# students=[{"Name":"Pooja",
#     "Age":22,
#     "Adm_No":3},
#           {"Name":"Kalyan",
#     "Age":22,
#     "Adm_No":4},
#           {"Name":"Gopika",
#     "Age":21,
#     "Adm_No":5},
#           ]
# collection.insert(students)

#print(client.list_database_names())
#print(collection.find_one())
for doc in collection.find({"Name":{"$regex":"^R"},"Age":{"$gt":20}}):
    print(doc)