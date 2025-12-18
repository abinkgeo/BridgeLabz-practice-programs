n=int(input("Enter the value of N"))
harmonic=0
if(n>0):
    for i in range(1,n+1):
        harmonic+=1/i
    
    print(f"{n}th Harmonic number is :{harmonic}")
else:
    print("Enter a positive value")    