def is_armstrong(n):
    temp = n
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** 3
        temp //= 10
    if total==n:
        return "Yes"
    else:
        return"No"

number = int(input("Enter the number"))
print(is_armstrong(number))
