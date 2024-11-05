# Write a python program that asks the user to input a number and prints the reciprocal of that number. 
# Handle the exception if the user input zero
# try:
#     num=int(input("Enter a number:"))
#     reciprocal=1/num
#     print("The reciprocal of",num,"is",reciprocal)
# except ZeroDivisionError:
#    print("cannot divide by zero")   
# except ValueError:
#    print("please enter a valid number")    
   


# Write a program that reads a numberfrom the user and prints its square.
# Use the else clause to print a success message
# try:
#     num=int(input("Enter a number:"))
#     result=(num**2)
#     print("The result is:",result)
# except Exception as e:
#     print(e,"exception") 
# else:
#     print("success")




# Write a function that raises a ValueError if the input number is negative
# def check_positive(number):
#     if number<0:
#         raise ValueError("Input number must be positive")
#     return number
# try:
#     user_input=int(input("Enter a positive number:"))
#     check_positive(user_input)
#     print("you entered:",user_input)
# except ValueError as e:
#     print(e,"exception")    






# MOdify the above program to also handle the exception if the user inputs a non-numeric value 
# try:
#      a=int(input("Enter a number:"))
#      print(a)
  
# #except ValueError:
#    # print("please enter a valid number")    
   
# except Exception as e:
#     print("e,exception")




# Modify the program in Task 3 to include a finally clause that print a message
# regardless of whether an exception occurred or not
# try:
#     num=int(input("Enter a number:"))
#     result=(num**2)
#     print("The result is:",result)
# except ZeroDivisionError:
#     print("not allowed ny negative number")
# except Exception as e:
#      print(e,"exception") 
# else:
#     print("success")
# finally:
#     print("thank you") 
 

 
# Write a program that repeatedly asks the user for a number and handle exception.
# The program should continue asking untila valid number is entered
# while True:
#     try:
#         num=int(input("Enter a number:"))
#         print(num)
#         break
#     except ValueError:
#         print("invalid number Try again")
#     except Exception as e:
#         print(e,"exception")    
    
        
    

    


# try:
#     num1=int(input("enter a number:"))
#     num2=int(input("enter a number:"))
#     res=num1/num2
#     print(res)
# #except ZeroDivisionError:
#  #print("exception occur")
# except Exception as e:
#     print(e,"exception")    







    
  
    








