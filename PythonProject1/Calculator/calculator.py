from salaries import *
from tax import *
from electricity import *
from rent import *
from internet import *

print("select method of education")
print("1. Offline")
print("2 .Online")

while True:
    choice = input("enter choice(1/2)")

    if choice == '1':
        print("Offline")
        a1 = print("the salary of your teachers is:", int(teacher_fixed_salary * 10))
        b1 = print("the salary of your accountants is:", int(accountant_fixed_salary * 2))
        c1 = print("the salary of your system administrator is:", int(system_administrator_fixed_salary))
        d1 = print("the salary of your security guard is:", int(segurity_guard_fixed_salary))
        e1 = print("the salary of your methologists is:", int(methodologist_fixed_salary * 2))
        tax1 = print("your salary tax is:", (a + b + c + d + e) * 0.301)
        f1 = print("the rent of building is:", int(rent_fixed_rate))
        g1 = print ("your internet payment is:", int(unlimited_internet_fixed_rate))
        h1 = units
        j1 = print("your total is:", a1 + b1 + c1 + d1 + e1 + tax1 + f1 + g1 + h1 + j1)

    elif choice == '2':
        a2 = print("the salary of your teachers is:", int(teacher_fixed_salary * 10))
        b2 = print("the salary of your accountants is:", int(accountant_fixed_salary * 2))
        c2 = print("the salary of your system administrator is:", int(system_administrator_fixed_salary))
        d2 = print("the salary of your security guard is:", int(segurity_guard_fixed_salary))
        e2 = print("the salary of your methologists is:", int(methodologist_fixed_salary * 2))
        tax2 = print("your salary tax is:", (a + b + c + d + e) * 0.301)
        f2 = print ("your zoom annual subscription is:", zoom_annual_fee)
        g2 = print("your total is:", a2 + b2 + c2 + d2 + e2 + tax2 + f2 + g2)

    
    else:
        print ("Invalid Input")
