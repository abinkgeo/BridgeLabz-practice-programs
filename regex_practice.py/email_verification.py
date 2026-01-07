import re

email=input("Enter the email")

pattern=r'^[a-z,A-Z,0-9,_,]+@[a-z,A-Z]+\.[a-zA-z]{2,}$'

if re.match(pattern,email):
    print("Valid email")

else:
    print("Invalid mail")