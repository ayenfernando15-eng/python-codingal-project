
print("===== Welcome to Holiday Planner =====")

print("Where would you like to go?")
print("1. Beach")
print("2. Mountains")
print("3. City")

choice = int(input("Enter 1, 2 or 3: "))

if choice == 1:
    print("You have chosen the beach!")
    print("Choose your beach activity")
    print("1. Swimming")
    print("2. Surfing")

    activity = int(input("Enter 1 or 2: "))

    if activity == 1:
        print("You have chosen swimming!")
    elif activity == 2:
        print("You have chosen surfing!")
    else:
        print("Wrong input")

elif choice == 2:
    print("You have chosen the mountains!")
    print("Choose your mountain activity")
    print("1. Hiking")
    print("2. Camping")

    activity = int(input("Enter 1 or 2: "))

    if activity == 1:
        print("You have chosen hiking!")
    elif activity == 2:
        print("You have chosen camping!")
    else:
        print("Wrong input")

elif choice == 3:
    print("You have chosen the city!")
    print("Choose your city activity")
    print("1. Shopping")
    print("2. Sightseeing")

    activity = int(input("Enter 1 or 2: "))

    if activity == 1:
        print("You have chosen shopping!")
    elif activity == 2:
        print("You have chosen sightseeing!")
    else:
        print("Wrong input")

else:
    print("Wrong input")

print("===== Enjoy your holiday! =====")
