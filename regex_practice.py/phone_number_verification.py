
import re

phone_number=input("Enter the number")

pattern=r'^\+91\-[6-9]\d{9}$'

if re.match(pattern,phone_number):
    print("Valid number")

else:
    print("Invalid")