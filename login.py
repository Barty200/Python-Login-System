import base64
def login(path):
    while True:
        choose = input("Do you want to login or register: ").title()
        if choose == "Login":
            username = input("What is your username: ")
            try:
                login = open(path + username, "r")
                password = login.read()
                userpassword = input("What is your password: ").encode("utf-8")                if password == str(base64.b64encode(userpassword)):
                    break
                else:
                    print("Password doesn't match")
                login.close()
            except:
                print("Account doesn't exist")
        elif choose == "Register":
            while True:
                username = input("What username do you want: ")
                try:
                    tryopen = open(path + username, "r")
                    tryopen.close()
                    print("Account already exists")
                except:
                    create = open(path + username, "w")
                    password = input("What password do you want: ").encode("utf-8")
                    create.write(str(base64.b64encode(password)))
                    create.close()
                    break
            break
        else:
            print("Unknown command")
login("C:\\Users\\bartl\\Documents\\Python People Saves\\")
    
