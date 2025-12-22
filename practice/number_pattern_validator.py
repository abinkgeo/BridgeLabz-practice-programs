def pattern(number):
    digits = str(number)
    for i in range(len(digits) - 1):
        if digits[i] >= digits[i + 1]:
            return "NO"
    return "YES"

number = input("Enter the number")
print(pattern(number))
