# Print 10 to 1
# def display(n):
#     if n>0:
#         print(n)
#         display(n-1)
# display(10)            


# Print 1 to 10
# def display(n):
#     if n>0:
#         display(n-1)
#         print(n)
# display(10)


# Fibonacci
# def fibrec(a):
#     if a<=1:
#         return a
#     else:
#         return(fibrec(a-1)+fibrec(a-2))
# x=int(input("Enter a number:"))
# print("fibonacci sequence:")
# for z in range(x):
#       print(fibrec(z))  
# 
 
# Sum of list
# def sum_list(lst):
#     if not lst:
#         return 0
#     else:
#      return lst[0]+sum_list(lst[1:])
# numbers=[1,2,3,4]
# print(sum_list(numbers))