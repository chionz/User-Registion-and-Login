#this is me building a users registration/login system
USER_DETAILS_FILEPATH = "allusers.txt"

def option():
    print("1. Register\n2. Login\n3. Exit\n")
    action = input("Select an action ")
    if action == "1":
        registration()
    elif action == "2":
        login()
    elif action == "3":
        return
    else:
        print("Invalid choice.")
        option()

def selectusername():
    username = input("Choose a User name ")
    if user_exists(username) == True:
        print("Username already exist choose")
        selectusername()
    else:
        pwd = input("Choose your password ")
        save_user(username, pwd, FirstName, LastName)

def registration():
    global FirstName
    FirstName= input("Your First name? ")
    global LastName
    LastName= input("Your Last Name? ")
    selectusername()

def save_user(username, pwd, Firstname, LastName):
    """Save user-details to the users detail file"""
    with open(USER_DETAILS_FILEPATH, "a") as f:
        f.write(f"{username} {pwd} {Firstname} {LastName}\n")
        print("Account created successfully!\n")
    return login()

def user_exists(username):
    try:
        with open(USER_DETAILS_FILEPATH,"r") as f:
            for line in f:
                parts = line.split()
                if parts[0] == username: 
                    return True
    except FileNotFoundError as fl_err:
        fl_err = "User not Found!"
        print(fl_err)

def auth(username, lpwd):
    with open(USER_DETAILS_FILEPATH, "r") as f:
        for line in f:
            parts = line.split()
        if parts[0]== username and lpwd == parts[1]:
                return True
        else:
             return False
        

def login():
    print("Now Login with your credentials")
    username = input("Enter Username ")
    if not user_exists(username):
        print("User does not exist.")
        return option()
    lpwd = input("Password? ")
    if auth(username, lpwd) == False:
        print("Incorrect Details.\n")
        option()
    if auth(username, lpwd) == True:
        print("Logged in Successfully")

with open(USER_DETAILS_FILEPATH, "r") as f:
    print(f)
option()


