print("===smart school day planner===")
print("answer the three questions and then I will plan the day for you")

day = input("enter the day of the week (Monday Sunday)").strip().capitalize()
weather = input("enter the weather(sunny or rainy or cloudy)") .strip().lower()
homework = input("have you done your home work( Y/N)").strip().upper()

print()
print(f"===your plan for the {day}===")
print("_" * 35)

if day in("Saturday","Sunday"):
    print ("Weekend - enjoy your free time")
elif day == "Monday":
    print("First day of the week. Pack your weekly planner")
elif day == "Friday":
    print(" Last school day. Return library books today.")
elif  day in ("Tuesday","Wednesday","Thursday"):
    print("Regular school day. Stay focused")
else: 
    print("Day not recognised. Please check the spelling.")

