total_homework = 4
original_count = total_homework

print(f"You have {original_count} homework tasks to finish!\n")

completed_count = 0
homework_num = 1

while homework_num <= total_homework:

    if homework_num == 1:
        next_homework = "Maths"
    elif homework_num == 2:
        next_homework = "English"
    elif homework_num == 3:
        next_homework = "Science"
    else:
        next_homework = "Social Studies"

    answer = input(f"Have you finished your {next_homework} homework? (yes/no): ")

    if answer == "yes":
        completed_count += 1
        homework_num += 1
        print("Great job! You have completed your homework!")

    else:
        print("Keep working on it and come back later!")

    print("Homework remaining:", total_homework - completed_count)
    print()


print("====== ALL HOMEWORK COMPLETED ======")
print("Homework assigned today:", original_count)
print("Homework completed:", completed_count)
print("Remaining homework:", total_homework - completed_count)