import pymongo
import uuid
import datetime
client = pymongo.MongoClient("mongodb+srv://ramadhanisal:ramadhanisal@cluster0.vk2qhxu.mongodb.net/?retryWrites=true&w=majority")
db = client.faisal
collection = db.sunrise

def save_to_db(kecepatan,latitude,longitude) -> tuple:
    try:
        data = {
            "kecepatan": kecepatan,
            "latitude": latitude,
            "logitude": longitude,
             }

        results = collection.insert_many(kecepatan,latitude,longitude)
        print(results.inserted_ids)
        return True,None
    except Exception as e:
      return False,str(e)

save_to_db(20,20,20)