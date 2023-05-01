from Auth import Auth
from Interface import Interface
import Database as Database

def main():
    auth = Auth()
    authenticated, connection_to_database = auth.Authenticate()

    if authenticated:
        interface = Interface(connection_to_database)
    #
#


if __name__ == "__main__":
    main()