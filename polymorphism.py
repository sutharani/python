
# Create a function which acts as  two arguments function and also three arguments function
# def add(x,y,z=0):
#     return x+y+z

# print(add(1,2,3))



# Create a base class called shape with method area that return 0.
# Create a derived class called rectangle that inherit from shape and overridws the area method to calculate and return the area of a rectangle.
# class Shape:
#     def area(self):
#         return 0
# class rectangle(Shape):
#     def __init__(self,width,height):
#         self.width=width 
#         self.height=height
#     def area(self):
#         print(self.width*self.height)
# rect=rectangle(2,2)
# rect.area()
           


# Create a base class called person with constructor that takes a name as a parameter.
# Create a derived called student that inherits from person has constructor that takes a parameter called grade.
# Write a method in student to display name and grade of student. Use super keywords to achieve this.
# class person:##########################################
#     def __init__(self,name):
#         self.name=name
# class student(person):
#     def __init__(self,name,grade):
#         super().__init__(name)
#         self.grade=grade

#     def display(self):
#      print(self.name)
#      print(self.grade)
# student=student("ram","b")
# student.display()    



# Create a base class called vehicle with a method start that print"vehicle started" create aderived class called car that inhetits
# from vehicle and overrides the start  method to print "car started".
# class vehicle:
#     def start(self):
#         print("vehicle started")
# class car(vehicle):
#     def start(self):
#         print("car started")
# vehicle=vehicle()
# vehicle.start() 
# car=car()
# car.start()  
# 
# 
# Create a base class called employee with properties name and salary. create a derived class called manager
# that inherit  from employee and adds a property department. Write a method in manager to
# display the name,salary and department of the manager. 
# class employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
# class manager(employee):
#     def __init__(self,name,salary,department):
#         super().__init__(name,salary)
#         self.department=department
#     def display_info(self):
#         print(self.name)
#         print(self.salary)
#         print(self.department) 
# manager=manager("ram",50000,"CS")
# manager.display_info()        





# Create a class called animal with a sound function that prints "Animal makes sounds". create a derived class called 
# dog that inherit from animals and overrides the sounds methods to print"dog barks".
# create a another function derived class bird that inherits from animal and overrides sound method to print"birds print".
# class animal:
#     def sound(self):
#         print("aniaml makes sound")
# class dog(animal):
#     def sound(self):
#         print("dog barks")
# class bird(dog):
#     def sound(self):
#         print("birds print")
# animal=animal()
# animal.sound()
# dog=dog()
# dog.sound()
# bird=bird()
# bird.sound()                        
 
 
 

  
 
 
 
 
 
 
 
 
 
            
 
 
 
  












