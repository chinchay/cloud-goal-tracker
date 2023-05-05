import hashlib
from getpass import getpass
from time import sleep

class Auth:
    def __init__(self):
        self.file_user_credentials = ".user_credentials.txt"
    #

    def SignUp(self):
        username = input("Username: ")
        password = getpass()
        confirm_password = getpass()

        if confirm_password == password:
            hash1 = getHash(password)
            writeCredentials(username, hash1, self.file_user_credentials)
        else:
            print("Passwords do not match. Try again.")
        #
    #

    def LogIn(self):
        username2 = input("Username: ")
        password2 = getpass()
        hash2     = getHash(password2)

        username1, hash1 = readFromCredentials(self.file_user_credentials)

        if (hash1 != False):
            if ((username1 == username2) and (hash1 == hash2)):
                print("Logged in Successfully!")
                sleep(1)
                return True
            else:
                print("error in credentials")
            #
        #
        return False
    #
#


def getHash(text):
    return hashlib.md5( text.encode() ).hexdigest()

def writeCredentials(username, hash1, filename):
    f = open(filename, "w")
    f.write(username + "\n")
    f.write(hash1)
    f.close()
#

def readFromCredentials(filename):
    try:
        f = open(filename, "r")
        lines = f.readlines()
        f.close()
        return lines[0].strip(), lines[1].strip()
    except:
        print("You should sign up first.")
    #
    return False, False
#
