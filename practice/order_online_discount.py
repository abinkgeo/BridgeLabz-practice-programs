def calculate_payable(amount):
    if amount >= 5000:
        amount -= amount * 0.20
    elif amount >= 3000:
        amount -= amount * 0.10
    elif amount >= 1000:
        amount -= amount * 0.05
    return int(amount)

amount = int(input("Enter the amount"))
print(calculate_payable(amount))
