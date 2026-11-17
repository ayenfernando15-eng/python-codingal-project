
print("====== Welcome to the Grocery Billing Queue System ======")

customers_served = 0
total_earnings = 0
serving = True

customer_queue = []

while serving:
    name = input("Enter customer name (or type 'done' to finish): ")

    if name.lower() == "done":
        break

    customer_queue.append(name)
    print(name, "has been added to the queue.")

print("\n====== STARTING BILLING ======")

while len(customer_queue) > 0:

    name = customer_queue.pop(0)

    print(f"\nNow serving: {name}")

    total = 0
    adding_items = True

    while adding_items:
        item = input("Enter grocery item name (or type 'done'): ")

        if item.lower() == "done":
            adding_items = False
        else:
            price = float(input("Enter item price: "))

            if price <= 0:
                print("Invalid price. Please enter a positive amount.")
                continue

            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Invalid quantity.")
                continue

            item_total = price * quantity
            total += item_total

            print(f"{quantity} x {item} = ${item_total:.2f}")

    print("\n====== CUSTOMER BILL ======")
    print("Customer:", name)
    print(f"Total bill: ${total:.2f}")
    print("==========================")

    customers_served += 1
    total_earnings += total

print("\n====== DAILY BILLING SUMMARY ======")
print("Customers served:", customers_served)
print(f"Total money earned: ${total_earnings:.2f}")
print("All customers have been served!")
print("Thank you for shopping!")
