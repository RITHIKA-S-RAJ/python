users = {"user1":"pass"}
username = input("Enter a username:")
if username in users:
    password = input("Enter the password :")
    correctPassword = users[username]
    if correctPassword == password:
        print("Successfully login")
    else:
        print("Oops,Wrong password")
else:
    print("No such user exist!!")
