import pymongo
client = pymongo.MongoClient("mongodb+srv://mishraabhi12:Mongodb123@power.skqtjc1.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
