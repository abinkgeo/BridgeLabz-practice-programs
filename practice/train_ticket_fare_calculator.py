def calculate_fare(distance, age):
    fare = distance * 2
    if age >= 60:
        fare -= fare * 0.30
    elif age < 12:
        fare -= fare * 0.50
    return int(fare)

distance = int(input("Enter the distance"))
age = int(input("Enter the age"))
print(calculate_fare(distance, age))
