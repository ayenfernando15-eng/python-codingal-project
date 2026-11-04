total_chores = 4
original_count = total_chores 
print(f"you have{original_count}of chores to finish!\n") 

completed_count = 0
chore_num = 1 

while chore_num <= total_chores:

    if chore_num == 1:next_chore = "Make the bed  "
    elif chore_num == 2:next_chore = "feed the pet"
    elif chore_num == 3:next_chore = "take out the the trash "
    else:next_chore ="wash the dishes"
    answer = input(f"have you finished your chores{next_chore}? (yes/no):")
    if answer == "yes":
        completed_count += 1
        chore_num += 1
        print("great job you have completed your chore")
    else:
        print("do it and come back and check later")
    print("chores remaining:",total_chores-completed_count)
    print()

print("=====ALL CHORES COMPLETED======")
print("Chores assigned today:", original_count )
print("Chores completed:", completed_count)
print("Remaining chores:" ,total_chores-completed_count)
