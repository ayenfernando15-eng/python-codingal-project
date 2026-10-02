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


if weather == "rainy" or weather == "cloudy":
    print("Weather tip : Pack your umbrella - it may get wet outside.")

# Topic 4 -- NOT operator: homework NOT done
if not (homework == "yes"):
    print("Homework    : Not done yet. Finish it before going out!")

# Topic 5 -- Combining AND + OR + NOT together
if weather == "rainy" and not (homework == "yes"):
    print("Best plan   : Stay in, finish homework, then watch your favourite show.")
elif weather == "sunny" and homework == "yes" and not (day in ("Saturday", "Sunday")):
    print("Best plan   : All set for a great school day - you are prepared!")
elif day in ("Saturday", "Sunday") and weather == "sunny":
    print("Best plan   : Perfect weekend weather - head outside and have fun!")
else:
    print("Best plan   : Take it one step at a time - you have got this!")

print()
print("Plan complete! Have a wonderful day!")
