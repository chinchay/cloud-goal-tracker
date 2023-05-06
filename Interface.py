from Database import Database
import pandas as pd
from datetime import datetime
import plotext as plt
import os
from time import sleep

class Interface:
    """
    The Interface class makes a connection between the user and the Database
    class. It allows the user to perform updating, retrieving, and visualization
    tasks, and sends the appropriate commands for the cloud database.
    """
    def __init__(self):
        self.tableName = "sample_table_1"
        self._UpdatePandas()
        self._Prompt()
    #

    def _Prompt(self):
        """
        Presents Visualize, Put item, and Delete item operations to the user
        """
        PrintHead()
        print("1. Visualize goals history\n2. Add or modify item\n3. Delete item")
        option = input("Choose an option: ")
        match option:
            case "1":
                self._Visualize()
            case "2":
                self._PutItem()
            case "3":
                self._DeleteItem()
            case default:
                print("Wrong option.")
        #
    #

    def _UpdatePandas(self):
        """
        Retrieve and updated table and pandas dataframe from the cloud database
        """
        print("Getting information from cloud database ...")
        self.database = Database(self.tableName)
        self.df       = self.database.BuildPandas()

    def Build_first_table(self):
        """
        To be implemented in future developement.
        """
        pass
    #

    def _PromptToContinue(self):
        """
        Asks if the user wants to continue in the program
        """
        sleep(1)
        ans = input("\nDo you wish to continue?\n1. y (yes)\n2. n (no)\nAnswer: ")
        if (ans == "y"):
            self._Prompt()
        #

    def _Visualize(self):
        """
        Visualize the pandas dataframe built from the cloud database table on
        the terminal
        """
        self._UpdatePandas()
        print("")
        print(self.df)
        print("")
        
        # x = list(map(str, self.df.date.strftime("%Y-%m-%d")))
        x  = self.df.date.dt.strftime("%Y-%m-%d").tolist()
        y1 = list(map(int, self.df.wrote_journal))
        y2 = list(map(int, self.df.read_scriptures))

        plt.date_form('Y-m-d')
        plt.scatter(x, y1)
        plt.scatter(x, y2)
        plt.title("Cloud Goal Tracker")
        plt.plotsize(70, 10)
        plt.show()
        plt.clear_data() # to avoid drawing over old data
        
        sleep(1)
        self._PromptToContinue()   
    #

    def _GetDate(self):
        """
        Prompts the user for a date, asking if today is the date to use

        Returns
        -------
        date (string)
            A date string in the format YYYY-MM-DD
        """
        PrintHead()
        today = datetime.now().strftime("%Y-%m-%d")
        print("Is new item for today ", today, "?\n1. y (yes)\n2. n (no)")
        option = input("Choose an option: ")
        match option:
            case "y":
                date = today
            case "n":
                date = input("type the date: ")
            case default:
                print("Wrong option.")
                sleep(1)
                option = input("Choose an option: ")
        #
        return date
    #   

    def _PutItem(self):
        """
        Build the dictionary to be used for updating the table in the cloud
        database. It has the following format:

        `item = {
        "date"            : "2023-04-11",
        "read_scriptures" : True,
        "wrote_journal"   : False
        }`
        """
        date =  self._GetDate()
        PrintHead()
        print("Date is: ", date)
        print("==============================\n")

        list_col = self.df.drop(["date"], axis=1).columns
        list_val = [ input(f"{col} : ") for col in list_col ]
        item     = { col : val for (col, val) in zip(list_col, list_val) }
        item["date"] = date
        self.database.PutItem(item)
        
        self._PromptToContinue()        
    #

    def _DeleteItem(self):
        """
        Delete a row from the table in the cloud database using a date
        """
        columnName = "date"
        primaryKey = input("Enter the date to delete (format: YYYY-MM-DD): ")
        # primaryKey = "2023-04-11"
        self.database.DeleteItem(columnName, primaryKey)

        self._PromptToContinue()
    #
#

def PrintHead():
    """
    Print a head giving information about the application
    """
    os.system("clear")
    print("Wellcome to Cloud Goal Tracker")
    print("==============================\n")
#