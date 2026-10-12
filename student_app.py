
print("SCHOOL STUDENT APP ACCESS MANAGER")
print("---------------------------------")

name = input("Enter your name: ")
year = int(input("Enter your school year (1-13): "))

print("\nHello", name, "!")
print("Choose an app to access:")
print("1. Homework App")
print("2. Learning App")
print("3. School Library")
print("4. Student Portal")

choice = input("Enter your choice (1-4): ")

if choice == "1":
    print("Access granted to Homework App!")
elif choice == "2":
    print("Access granted to Learning App!")
elif choice == "3":
    print("Access granted to School Library!")
elif choice == "4":
    if year >= 7:
        print("Access granted to Student Portal!")
    else:
        print("Access denied. This app is for Year 7 and above.")
else:
    print("Invalid choice. Please try again.")

print("\nThank you for using the School Student App Access Manager!")
