from Auth import Auth
from Interface import Interface
import Database as Database
import os



def prompt():
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

def main():
    auth = Auth()
    authenticated, connection_to_database = auth.Authenticate()

    if authenticated:
        interface = Interface(connection_to_database)
        # interface.Update()
        # interface.Visualize()
        # interface.prompt()
        interface.Visualize()
        
        
        # interface.Update()
    #
#


if __name__ == "__main__":
    # main()
    prompt()