print("=====Welcome to Ride Builder=====")

print("which vechicle would you like to choose")
print("1.car")
print("2.bike")

choice= int(input("enter 1 or 2"))
if choice==1 :
    print("you have chosen a car ")
    print("choose your type of car")
    print("1. Lamborgini")
    print("2. ferrari")
    car=int(input("enter 1 or 2"))
    if car==1 :
        print("you have chosen lamborgini")
    elif car==2:
        print("you have chosen ferrari")


elif choice==2:
    print("you have chosen a bike")
    print("choose your type of bike")
    print("1 motorcycle")
    print("2 scooter")
    bike=int(input("enter 1 or 2"))
    if bike==1 :
        print("you have chosen motorcycle")
    elif bike==2:
        print("you have chosen the scooter")

else:
    print("wrong input")

