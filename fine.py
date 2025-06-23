# 6. Library Fine Calculator
days = int(input("Enter number of overdue days: "))

if days <= 0:
    fine = 0
elif days <= 5:
    fine = days * 1
elif days <= 10:
    fine = 5 + (days - 5) * 2
else:
    fine = 5 + 10 + (days - 10) * 5

print("Your total fine is: ₹", fine)
