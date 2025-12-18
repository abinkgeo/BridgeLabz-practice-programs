import random                                    

tails=0
heads=0
n=int(input("Enter the number of times to flip the coin"))
for i in range(n):
    random_number=random.random()
    if random_number<0.5:
        tails+=1
    else:
        heads+=1

print(f"Percentage of heads:{(heads/n)*100} %")
print(f"Percentage of Tails: {(tails/n)*100} %")