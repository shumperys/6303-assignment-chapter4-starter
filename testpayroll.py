# This app tests the calc_payroll_tax() function
# How to import a function from another file
# You may see an error on line 6 until you finish creating calc_payroll_tax() in payroll.py. That's ok.
# Notice calc_payroll_tax() is in payroll.py file, not the current app.py file
from payroll import calc_payroll_tax

calc_payroll_tax(100)
print("-" * 20)

calc_payroll_tax(400)
print("-" * 20)

calc_payroll_tax(2000)
print("-" * 20)