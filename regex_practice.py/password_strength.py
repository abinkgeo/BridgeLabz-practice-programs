import re


password=input("Enter the password")

pattern=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$'

if re.match(pattern,password):
    print("Valid password")

else:
    print("Invalid password")