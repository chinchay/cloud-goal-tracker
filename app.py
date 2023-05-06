from Auth import Auth
from Interface import Interface
import Database as Database
import os

def prompt():
    """
    The login interface asks to enter a user and a password, and it will compare
    to the user and hashed password save locally. 

    After successfully being loged in, it will give control to an instance of
    the Interface class.
    """
    auth = Auth()

    os.system("clear")
    print("Wellcome to Cloud Goal Tracker")
    print("==============================")
    print("LOGIN INTERFACE")
    print("==============================\n")
    print("1. Log in\n2. Sign up\n3. Exit\n")
    option = input("Choose an option: ")
    match option:
        case "1":
            print("Log in...")
            isLogIn = auth.LogIn()
            if isLogIn:
                os.system("clear")
                interface = Interface()
            #
        #
        case "2":
            print("Sign up...")
            auth.SignUp()
        case "3":
            print("Exit ...")
        case default:
            print("Wrong option.")
    #
#

if __name__ == "__main__":
    prompt()