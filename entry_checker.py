print("=== SWIMMING POOL ENTRY CHECKER ===")
print("Answer the questions to see if you can enter the pool.")

age = int(input("Enter your age: ").strip())
weather = input("Is the weather sunny or rainy? ").strip().lower()
swim = input("Can you swim? (Y/N) ").strip().upper()
shower = input("Have you had a shower? (Y/N) ").strip().upper()

print()
print("=== YOUR POOL CHECK ===")

if age < 5:
    print("You need an adult with you.")
elif age >= 5 and swim == "Y" and shower == "Y":
    print("You can enter the swimming pool!")
elif swim == "N" or shower == "N":
    print("You cannot enter yet.")
    print("Make sure you can swim and have had a shower.")
else:
    print("Please check your answers.")

if weather == "rainy":
    print("It is rainy, so check if the pool is open.")
elif weather == "sunny":
    print("It is sunny! Have fun swimming!")

if not (swim == "Y"):
    print("Remember to stay with an adult if you cannot swim.")

print()
print("=== HAVE FUN AT THE POOL! ===")