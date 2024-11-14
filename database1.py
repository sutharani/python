# import pymongo

# connection=pymongo.MongoClient("mongodb+srv://sutharanikannan:sutharani2024@cluster0.70icb.mongodb.net/")
# database1=connection.test
# col=database1.learning
# Employee=[{ "Name":"Employee1",
#             "Age":30,
#             "Salary":40000
#            },
#            { "Name":"Employee2",
#              "Age":32,
#              "Salary":45000
#             },
#             { "Name":"Employee3",
#               "Age":33,
#               "Salary":50000
#             }]
# res=col.insert_many(Employee)
# print(res.inserted_ids)




# update
# previous_data={"Salary":45000}
# present_data={"$set":{"Salary":60000}}
# res=col.update_one(previous_data,present_data)
# print(res)


# # query
# query={"Name":"Employee2"}
# res=col.find(query)
# for i in res:
#     print(i)


# #find
# x=col.find_one()
# print(x)


# # insert
# mydict={"Name":"Employee5","Age":40,"Slary":70000}
# x=col.insert_one(mydict)
# print(x)

# limit
# myresult=col.find().limit(2)
# for x in myresult:
#     print(x)














