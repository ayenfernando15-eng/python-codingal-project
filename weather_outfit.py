temperature = int(input("Enter the temperature in celcicus"))
if temperature <= 20: 
    outfit = "jacket"
    print("it is cold today")
    print("So wear a" , outfit  )
else:
    outfit = "t-shirt"
    print("it is warm today")
    print("so wear a " ,outfit)

is_raining = input("is it raining").lower()
if is_raining == "yes": 
    print("carry an umbrella")



