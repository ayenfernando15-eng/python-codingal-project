print("======Welcome to the ATM Cash Dispenser=====/n")
total_100=total_50=total_20=total_10=total_5=total_1=0
customers_served=0
total_dispensed=0
serving=True
while serving:
    name=input("enter customer name.")
    amount=int(input(f"hello {name } enter the amount you would like to withdraw"))
    if amount <=0 :
        print("ivailid amountplease enetr a positive number")
        continue 
    print(f"/n dispensing {amount} giving units to {name}")
    remaining=amount
    idx=1
    while idx<=6:
        if idx == 1:value= 100
        elif idx == 2:value= 50
        elif idx == 3:value= 20
        elif idx == 4:value= 10
        elif idx == 5:value= 5
        else:value= 1
        count= remaining // value
        if count >0 :
            print(f"{count} x {value} unit notes(s)={count * value} ")
            remaining -= value* count
            if value== 100: total_100+= count
            elif value== 50: total_50+= count
            elif value== 20: total_20+= count
            elif value== 10: total_10+= count
            elif value== 5: total_5+= count
            elif value == 1: total_1= count
        idx+=1 
    customers_served +=1 
    total_dispensed += amount
    again=input("next customer (yes/no):").strip().lower()
    if again != "yes":
        serving = False


                        
                


