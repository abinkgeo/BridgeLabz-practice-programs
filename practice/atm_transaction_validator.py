def atm_transactions(balance, requests):
    for amount in requests:
        if amount % 100 == 0 and balance >= amount:
            print("SUCCESS")
            balance -= amount
        else:
            print("FAILED")
    return balance


balance = int(input("Enter the balance"))
N = int(input("Enter the number of request"))
requests=[]
for i in range(N):
    r=int(input("Enter the number"))
    requests.append(r)

final_balance = atm_transactions(balance, requests)
print(final_balance)
