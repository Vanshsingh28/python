# 4. Bus Ticket Fare Calculator
base_fare = 100
age = int(input("Enter your age: "))

if age <= 5:
    fare = 0
elif age <= 12:
    fare = base_fare * 0.5
elif age >= 60:
    fare = base_fare * 0.7
else:
    fare = base_fare

print("Your ticket fare is: ₹", fare)
