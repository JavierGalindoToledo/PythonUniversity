from salaries.py import *
from tax.py import *
from electricity.py import *
from rent.py import *
from zoom.py import *
from internet.py import *

print("select method of education")
print("1. Offline")
print("2 .Online")

while True:
    choice = input("enter choice(1/2)")

    if choice == '1':
        print("Offline")
        a = print("the salary of your teachers is:", int(teacher_fixed_salary * 10))
        b = print("the salary of your accountants is:", int(accountant_fixed_salary * 2))
        c = print("the salary of your system administrator is:", int(system_administrator_fixed_salary))
        d = print("the salary of your security guard is:", int(segurity_guard_fixed_salary))
        e = print("the salary of your methologists is:", int(methodologist_fixed_salary * 2))
        f = print("the rent of building is:", int(rent_fixed_rate))
        g = print ("your internet payment is:", int(unlimited_internet_fixed_rate))
        