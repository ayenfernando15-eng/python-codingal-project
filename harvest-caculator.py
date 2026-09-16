field1 = 25
field2 = 30
field3 = 95
field4 = 40
field5 = 65
total = field1+field2+field3+field4+field5
average = total/5
print("the total harvest is: " ,total )
print("the average is " ,average )
price_per_kg = 15
earning = total * price_per_kg
print("the total earning is" ,earning)
no_bags = total // 25
remaining = total % 25
last_year = 100
print("number of bags" ,no_bags )
print("remaining number " ,remaining)
print("better than last year ?:" ,total>last_year)
print("same as last year? :" ,total==last_year )
print("at least as good as last year? :" ,total>=last_year )
total+=30
print("after bonus crop :" ,total )