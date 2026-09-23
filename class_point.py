student1 = 25
student2 = 30
student3 = 95
student4 = 40
student5 = 65

total = student1 + student2 + student3 + student4 + student5
average = total / 5

print("Total school points:", total)
print("Average points:", average)

bonus_points = 30
total += bonus_points

print("After bonus points:", total)

if total >= 200:
    print("Great job! Your school has earned lots of points!")
else:
    print("Keep going! You can earn more points!")