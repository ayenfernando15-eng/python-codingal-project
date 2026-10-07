m1=100
m2=100
m3=100

total=m1+m2+m3
avg= int(total/3)
print(avg)

if(avg not in range(0,100)):
    print("invalid")
elif (avg in range(91,100)):
    print("A+")

elif (avg in range(81,90)):
    print("A")

elif (avg in range(71,80)):
    print("B+")

elif (avg in range(61,70)):
    print("B")

elif (avg in range(51,61)):
    print("C")

else:
    print("fail")
