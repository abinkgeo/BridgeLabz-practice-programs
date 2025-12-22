def seat_allocation(requests):
    seats = 40
    for r in requests:
        if seats >= r:
            print("CONFIRMED")
            seats -= r
        else:
            print("WAITLISTED")

N = int(input("Enter the number of request"))
requests=[]
for i in range(N):
    r = int(input("Enter the number of seats: "))
    requests.append(r)

seat_allocation(requests)
