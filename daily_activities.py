time = int(input("What time is it.? "))

if time < 12:
    maths = "study"
    print("It is morning")
    print("So you should", maths )
else:
    football = "play"
    print("It is afternoon")
    print("So you should", football)

is_homework = input("Do you have homework? ").lower()

if is_homework == "yes":
    print("Do your homework")
else:
    print("You can relax and play")

is_tired = input("Are you tired? ").lower()

if is_tired == "yes":
    print("Take a rest")
else:
    print("Keep going with your activities")

print("Have a great day!")