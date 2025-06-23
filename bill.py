# 5. Electricity Bill Generator
units = int(input("Enter electricity units consumed: "))

if units <= 100:
    rate = 5
elif units <= 200:
    rate = 7
elif units <= 300:
    rate = 10
else:
    rate = 12

bill = units * rate
print("Your electricity bill is: ₹", bill)
