# 7. Simple Login System
correct_username = "admin"
correct_password = "1234"
attempts = 3

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login Successful!")
        break
    else:
        attempts -= 1
        print("Incorrect credentials. Attempts left:", attempts)

if attempts == 0:
    print("Account locked. Too many failed attempts.")
