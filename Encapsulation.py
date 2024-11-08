# Class company with constructor with private variable. With variable name as method. To access that variable. 
# Protected variable can access child class  ##private__(double__) ##Protected Access_(single_)
# class Company:
#     def __init__(self,name,revenue):
#         self.__name=name
#         self.__revenue=revenue
#     def __private_method(self):
#         # print("This is a private method")
#         print(self.__name)
#         print(self.__revenue)

# class Subsidiary(Company):
#     def get_revenue(self):
#         print("revenue")
# ojCompany=Company("Tech Corp",908888)
# ojCompany.__private_method()




# Create a base class called shape with method area that return 0. Create a derived class called rectangle
# that inherit from shape and overrides the 
# area method to calculate and return the area of a rectangle.



# class MyClass:###################################
#     def __init__(self, x):
#         self.x = x  # Public attribute

#     def public_method(self):
#         print("This is a public method")

# obj = MyClass(10)
# print(obj.x)        
# obj.public_method()  # Calling public



# class MyClass:##################################################
#     def __init__(self, x):
#         self.__x = x  # Private attribute

#     def __private_method(self):
#         print("This is a private method")

# obj = MyClass(10)
# print(obj.__x)         # This will cause an error
# obj.__private_method()  



# class MyClass:###########################################
#     def __init__(self, x):
#         self._x = x  # Protected attribute

#     def _protected_method(self):
#         print("This is a protected method")

# obj = MyClass(10)
# print(obj._x)        
# obj._protected_method()  






