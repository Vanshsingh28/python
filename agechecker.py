# 3. Age Checker
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote and drive.")
elif age >= 16:
    print("You are eligible to drive a two-wheeler (depending on your country), but not vote.")
else:
    print("You are not eligible to vote or drive.")
