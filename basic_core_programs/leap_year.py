
year=(input("Enter the year"))
if(len(year)==4):
    year=int(year)
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
else:
    print("Enter a valid year")
    