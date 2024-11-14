# import re
# regex=re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
# def emailValid(email):
#     if re.fullmatch(regex,email):
#         print("The given mail is valid")
#     else:
#         print("The given mail is invalid") 
# emailValid("dhibi@gmail.com") 
 
 
      

import re
text="This mailid gmail missing dhibi123@.com or sutharanikannan@gmail.com is correct my mailid."
email_pattern=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
emails=re.findall(email_pattern,text)
print("Email addresses :",emails)



