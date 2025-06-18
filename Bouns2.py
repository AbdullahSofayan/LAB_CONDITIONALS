

name = input("Enter your name: ")
email = input("Enter your email (must be gmail): ")


if len(name) > 2 :
    if email.endswith("@gmail.com") and len(email) > len("@gmail.com"):
        print(f"welcome, {name}, you registered with the email {email}")
    else:
        print("The email is not valid , please provide a valid email .")
else:
    print("The name length must be more than 2 characters, please provide a valid name.")






