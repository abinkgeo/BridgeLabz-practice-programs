def divide_by_two_count(n):
    count = 0
    while n % 2 == 0:
        n //= 2
        count += 1
    return count

number = int(input("Enter the number"))
print(divide_by_two_count(number))
