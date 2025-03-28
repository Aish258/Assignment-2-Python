"""#Q1
basic_pay=int(input("basic pay of an employee="))
da=int(basic_pay*0.40)
hra=int(basic_pay*0.10)
gross_pay=int(da+hra+basic_pay)
print("Dearness allowance is RS",da)
print("House rent allowance is RS",hra)
print("Gross pay is RS",gross_pay)
"""
'''#Q1-a
basic_pay=int(input("basic pay of an employee="))
da=float(input("percentage of dearness allowance="))
hra=float(input("percentage of house rent allowance="))
da_amount=float(basic_pay*0.4)
hra_amount=float(basic_pay*0.1)
print("The basic pay of an employee is RS",basic_pay,"on which 40% dearness allowane is RS",da_amount,"with the 10% house rent allowance id RS",hra_amount)
gross_pay=float(basic_pay+da_amount+hra_amount)
print("The gross pay of an employee =",gross_pay)
'''
"""#Q1-b
def countgrosspay():

 basic_pay=int(input("Enter the amount of basic pay of the employee="))
 da=float(input("Enter percentage of dearness allowance="))
 hra=float(input("Enter the percentage of house rene allowance"))
 da_amount=basic_pay*da
 hra_amount=basic_pay*hra
 print("The gross pay of an employee is",basic_pay+da_amount+hra_amount)

countgrosspay()

"""
'''#Q2
monthly_income=1100
rent=500
food=300
electricity=40
phone=60
cable_tv=30
monthly_expenses=rent+food+electricity+phone+cable_tv
remainder=monthly_income-monthly_expenses
print("The monthly expenses are",monthly_expenses,"and remainder is",remainder,".")
'''
'''#Q2-a

monthly_income=int(input("Enter the amount of monthly income="))
rent=int(input("Enter the amount of rent="))
food=int(input("Enter the amount of food="))
electricity=int(input("Enter the amount of electricity="))
phone=int(input("Enter the amount of phone="))
cable_tv=int(input("Enter the amount of cable TV="))
print("The total monthly expense is RS",rent+food+electricity+phone+cable_tv)

'''


'''Q2-b

def checksavingorborrow():
    monthly_income = int(input("Enter the amount of monthly income="))
    rent = int(input("Enter the amount of rent="))
    food = int(input("Enter the amount of food="))
    electricity = int(input("Enter the amount of electricity="))
    phone = int(input("Enter the amount of phone="))
    cable_tv = int(input("Enter the amount of cable TV="))
    monthly_expenses=rent + food + electricity + phone + cable_tv
    remainder=monthly_income-monthly_expenses
    print("Total monthly expenses are RS",monthly_expenses)
    print("remainder is RS",remainder)
    if remainder>=1:
         print("You have saving of RS",remainder,"!")
    else:
         print("You have to borrow money!")
checksavingorborrow()
'''

#Q3
'''
basic_price=int(input("Enter the basic price of vehicle="))
weight=float(input("Enter the weight of vehicle in kilograms="))
type_of_vehicle=input("Enter the type of vehicle=")
if type_of_vehicle=="P":
    vehicle_tax=basic_price*0.05
    weight_tax=weight*0.01
    insurance_premium=basic_price*0.01
    print("The on road price of vehicle is=",basic_price+vehicle_tax+weight_tax+insurance_premium)
elif type_of_vehicle=='B':
    vehicle_tax=basic_price*0.1
    weight_tax=weight*0.03
    insurance_premium=basic_price*0.02
    print("The on road price of vehicle is=",basic_price+vehicle_tax+weight_tax+insurance_premium)
'''

#Q3-a
'''

basic_price=int(input("Enter the basic price of vehicle="))
weight=float(input("Enter the weight of vehicle in kilograms="))
type_of_vehicle=input("Enter the type of vehicle=")
if type_of_vehicle=="P":
    vehicle_tax=basic_price*0.05
    weight_tax=weight*0.01
    insurance_premium=basic_price*0.01
    onroad_price=basic_price+vehicle_tax+weight_tax+insurance_premium
elif type_of_vehicle=='B':
    vehicle_tax=basic_price*0.1
    weight_tax=weight*0.03
    insurance_premium=basic_price*0.02
    onroad_price = basic_price + vehicle_tax + weight_tax + insurance_premium

d1={"Type":type_of_vehicle,"Weight":weight,"Basic price":basic_price,"Vehicle tax":vehicle_tax,"Weight tax":weight_tax,"Insurance":insurance_premium,"On road price":onroad_price}
print(d1)
'''

#Q3-b,c,d

n=int(input("Enter number of vehicles:"))
vehicles=[]
for i in range(n):
    basic_price=float(input(f"Enter basic price of vehicle{i+1}="))
    weight = float(input(f"Enter weight of vehicle{i+1}="))
    type_of_vehicle= (input(f"Enter type of vehicle{i+1}(P/B)="))
    if type_of_vehicle=="P":
     vehicle_tax=basic_price*0.05
     weight_tax=weight*0.01
     insurance_premium=basic_price*0.01
     onroad_price=basic_price+vehicle_tax+weight_tax+insurance_premium
    elif type_of_vehicle=="B":
     vehicle_tax=basic_price*0.1
     weight_tax=weight*0.03
     insurance_premium=basic_price*0.02
     onroad_price = basic_price + vehicle_tax + weight_tax + insurance_premium
    d1={"Type":type_of_vehicle,"Weight":weight,"Basic price":basic_price,"Vehicle tax":vehicle_tax,"Weight tax":weight_tax,"Insurance":insurance_premium,"On road price":onroad_price}
    vehicles.append(d1)
print(vehicles)

highest_on_road_price=max(d1[onroad_price]for d1 in vehicles)
highest_vehicles=[d1 for d1 in vehicles if d1[onroad_price]==highest_on_road_price]
least_weight=min(d1[weight]for d1 in vehicles)
least_weight_vehicle=next(d1 for d1 in vehicles if d1[weight]==least_weight)
print("vehicle with highest onroad price=")
for d1 in highest_vehicles:
 print(d1)
print("vehicle with least weight=")
print(least_weight_vehicle)

average_on_road_price = sum(d1["On-Road Price"] for d1 in vehicles) / len(vehicles)

higher_than_average = sum(d1 for d1 in vehicles if d1["On-Road Price"] > average_on_road_price)

weight_above = int(input("Enter weight value: "))
count_weight_above = sum(1 for d1 in vehicles if d1["Weight"] > weight_above)

budget = float(input("Enter budget: "))
count_within_budget = sum(1 for d1 in vehicles if d1["On-Road Price"] <= budget)

print("Average on-road price:", average_on_road_price)
print("Count of vehicles with on-road price higher than average:", higher_than_average)
print("Count of vehicles with weight above", weight_above, ":", count_weight_above)
print("Count of vehicles with on-road price less than or equal to budget:", count_within_budget)
