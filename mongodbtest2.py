import pymongo
client = pymongo.MongoClient("mongodb+srv://mishraabhi12:Mongodb123@power.skqtjc1.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


d={
    "name": "abinash",
    "email": "me2isb2@gmail.com",
    "surname":"mishra",
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)