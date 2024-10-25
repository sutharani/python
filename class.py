# Create student class and possible function and attributes. 
# Using constructor func,set and get function
# class student:
#     def __init__(self,name,subject,rank):
#         self.name=name
#         self.subject=subject
#         self.rank=rank
#     def get_function(self):
#         print("name:",self.name) 
#         print("subject:",self.subject)
#         print("rank:",self.rank)

#     def set_subject_function(self,subject):
#         self.subject=subject
        


# student1= student("g1","maths",1)
# student2= student("g2","english",2)
# student3= student("g3","computer",3) 


# #student1.get_function() 
# student3.set_subject_function("tamil")
# student3.get_function()



# Create a class called laptop.Create a following variables and function.
# variable=price,proccssor,ram Create object as Lenovo, HP,Dell
class Laptop:
    def __init__(self,price,processor,ram):
       self.price=price
       self.processor=processor
       self.ram=ram
    def get_function(self):
       print("price:",self.price)
       print("processor:",self.processor)
       print("ram:",self.ram)
Lenovo=Laptop(500,"intel i7",16)
HP=Laptop(600,"amd",8)
Dell=Laptop(900,"intel",10)  
Lenovo.get_function()
HP.get_function()
Dell.get_function()





# Create class kodaikanal and create all the possible variable and function





