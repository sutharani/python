# Filter out even numbers from a list
# def checkeven(numbers):
#     if numbers%2==0:
#         return True  
# numbers=[1,2,3,4,5,6,7,8,9,10]
# even =filter(checkeven,numbers)
# print(list(even) )   


# Filter out numbers greater than 10
# def greater(numbers):
#     if numbers>10:
#         return True
# numbers=[2,9,12,15,20]
# greater=filter(greater,numbers)
# print(list(greater))        


# Filter out numbers that are not divisible by 3
# def not_divisible(number):
#     if number%3!=0:
#         return True
# numbers=(1,2,3,4,5,6)
# not_divisible=filter(not_divisible,numbers)
# print(list(not_divisible))
#         

# Filter out negative numbers from a list
# numbers=[1,-5,2,8,-10,-15]
# print(list(filter(lambda x:x>0,numbers)))

# 
# Filter out words horter than 4 characters
# string="hello","hi","native"
# filtered_list=[x for x in string if len(x)<4]
# print(list(filtered_list))

# Filter out strings containing the letter "a" 
# string=["apple","banana","cherry","fig"]
# filtered_strings=[s for s in string if "a" not in string]
# print(filtered_strings)




# Square all numbers in a list
# def square(x):
#     return x*x
# numbers=[1,2,3,4,5]
# square=map(square,numbers)
# print(list(square))



# convert all string in a list to uppercase
# def upper_case(string):
#     return list(map(lambda x:x.upper(),string))
# print(upper_case(["all","is","well"]))


# Add 10 to each number in a list
# def add(list):
#     return list+10
# numbers=[1,2,3,4,5]
# print(list(map(add,numbers)))


# Double each number in a list
# def double(list):
#     return list*2
# x=[1,2,3,4,5]
# result=list(map(double,x))
# print(result)


#Capitalize the first letter of each string in a list
# def capitalize(string):
#   return string.capitalize()
# string=["hello"]
# print(list(map(capitalize,string)))

   
#Find the product of allnumbers in a list
# def prod(x,y):
#     return x*y
# list=[1,2,3,4,5]
# from functools import reduce
# print(reduce(prod,list))



# Find the maximum number in a list
# from functools import reduce
# numbers=[1,2,3,4,5]
# max=reduce(lambda x,y:x if x>y else y,numbers)
# print(max)




# Compute the sum of square of number in a list
# from functools import reduce
# def sum_square(x,y):
#     return(x*x +y*y)
# mylist=[1,2,3,4,5]
# print(reduce(sum_square,mylist))



# Compute the factorial of a number using reduce
# from functools import reduce
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return reduce(lambda x,y:x*y,range(1,n+1))
# print(factorial(3))   
# 
# 
# 
##### RANDOM
# import random
# n=random.randrange(1,5)
# guess=int(input("Enter a number:")) 
# if guess <n:
#         print("your guessing wrong:")
#         guess=int(input("enter number again:"))
# elif guess>n:
#         print("too high try again:")
#         guess=int(input("enter number again:"))
# else:
#  print("you guessed  right") 
 
 
 

# import random
# mylist=[1,2,3,4,5]
# while True:
#     correct_number=random.choice(mylist)
#     print("Try to guess it")
#     while True:
#         user_input=input("Guess a number from 1to 5:")
#         if user_input.isdigit():
#             user_input=int(user_input)
#             if user_input==correct_number:
#                 print("Your guessing is correct!")
#                 break
#             else:
#                 print("your guessing is wrong.try again")
#         else:
#             print("please enter a valid number")
#             play_again=input("Do you want to play again?(yes/no)").strip().lower()
#             if play_again!="yes":
#                 print("Thanks for playing!")
#                 break















          

                
            






    



















