import pymongo

connection=pymongo.MongoClient("mongodb+srv://sutharanikannan:sutharani2024@cluster0.70icb.mongodb.net/")
db=connection.python1
col=db.learning

student=[{ "Name":"ram",
          "age":22,
          "course":"java"

         },
         { "name":"sutha",
            "age":23,
            "course":"python"
             
         },

         { "name":"rani",
            "age":24,
            "course":"c++"
             
         }]
#res=col.insert_many(student)
#print(res.inserted_ids)

#update
# previous_data={"age":24}
# present_data={"$set":{"age":25}}
# res=col.update_one(previous_data,present_data)

#quary
query={"name":"sutha"}
res=col.find(query)
for i in res:
    print(i)

