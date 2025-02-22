# Assignment-2-Python
#Counting gross pay depend on various inputs
basic_pay=int(input("basic pay of an employee="))
da=int(basic_pay*0.40)
hra=int(basic_pay*0.10)
gross_pay=int(da+hra+basic_pay)
print("Dearness allowance is RS",da)
print("House rent allowance is RS",hra)
print("Gross pay is RS",gross_pay)


basic_pay=int(input("basic pay of an employee="))
da=float(input("percentage of dearness allowance="))
hra=float(input("percentage of house rent allowance="))
da_amount=float(basic_pay*0.4)
hra_amount=float(basic_pay*0.1)
print("The basic pay of an employee is RS",basic_pay,"on which 40% dearness allowane is RS",da_amount,"with the 10% house rent allowance id RS",hra_amount)
gross_pay=float(basic_pay+da_amount+hra_amount)
print("The gross pay of an employee =",gross_pay)


def countgrosspay():

 basic_pay=int(input("Enter the amount of basic pay of the employee="))
 da=float(input("Enter percentage of dearness allowance="))
 hra=float(input("Enter the percentage of house rene allowance"))
 da_amount=basic_pay*da
 hra_amount=basic_pay*hra
 print("The gross pay of an employee is",basic_pay+da_amount+hra_amount)

countgrosspay()
