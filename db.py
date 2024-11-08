import pymongo

connection=pymongo.MongoClient("mongodb+srv://sutharanikannan:sutharani2024@cluster0.70icb.mongodb.net/")
db=connection.python
col=db.learning

student=[{"name":"dhibi",
     "age": 20,
     "course":"python"
        },
    {
    "name":"ram",
    "age":15,
    "course":"java"

    }]


# res=col.insert_many(student)
# print(res.inserted_ids)


def add(x,y,z=0):
    return x+y+z

print(add(1,2,3))

