
print("GROCERY COST COMPARISON TOOL")

item = input("Enter the grocery item: ")

price1 = float(input("Enter the price at Store 1: "))
price2 = float(input("Enter the price at Store 2: "))

if price1 < price2:
    print(item, "is cheaper at Store 1")
    print("You save $", round(price2 - price1, 2))

elif price2 < price1:
    print(item, "is cheaper at Store 2")
    print("You save $", round(price1 - price2, 2))

else:
    print("Both stores have the same price")

print("Thank you for using the tool!")
