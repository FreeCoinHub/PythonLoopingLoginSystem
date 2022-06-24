choice = input("'register' or 'login'")

if choice == "register":
    file = open("users.txt","r+")
    text = file.read().strip().split()
    register = True
    while register:
        username=input("Enter Username:") #Takes Their Username And Stores It As An Input
        if username == "":
            continue
        if username in text: #If The Username Can Be Found In users.txt
            print("This Username Is Taken, Please Try Another One")
        else: #If The Username Cannot Be Found
            print("Username Accepted")
            register = False
            register = True
            while register:
                password1=input("Please Enter Password: ")
                password2=input("Please Re-Enter Password: ")
                if password1 == password2:
                    if password2 in text:
                        print("Password is Too Frequently Used.. Please Try Another")
                    else:
                        print("Account Successfully Registered")
                        file.write("Username: " + username + " | Password: " + password1 + "\n")
                        file.close()
                        register = False
                else:
                    print("Passwords Do Not Match.. Try Again")                         
    file.close()


if choice == "login":
    counter = 0 
    register = True
    while register:
        print("\n \n Player 1:")
        username1=input("Username: ")
        password=input("Password: ")
        with open("users.txt","r") as username_finder:
            for line in username_finder:
                if ("Username: " + username1 + " | Password: " + password) == line.strip(): 
                    print("Logged In \n")
                    register = False
                    register = True
                    while register:
                        print("Player 2:")
                        username2=input("Username: ")
                        password=input("Password: ")
                        with open("users.txt","r") as username_finder:
                            for line in username_finder:
                                if ("Username: " + username2 + " | Password: " + password) == line.strip():
                                    print("Logged In \n \n")
                                    register = False
                                    # Your code here
