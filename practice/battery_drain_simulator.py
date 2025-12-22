def battery_minutes(drain):
    battery = 100
    minutes = 0
    while battery > 0:
        battery -= drain
        minutes += 1
    return minutes

drain = int(input("Enter the drain"))
print(battery_minutes(drain))
