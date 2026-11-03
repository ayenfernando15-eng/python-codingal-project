number = int(input("Enter your number: "))
power = int(input("Enter the power: "))

answer = 1

for i in range(power):
    answer = answer * number

print("The original number is:", number)
print("The power is:", power)
print("The answer is:", answer)