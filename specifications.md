# Classes definition
The *Cloud Goal Tracker* program will help you to achieve your goals through gamification (turning your goals into a game) throught the use AWS DynamoDB cloud database and Python libraries to connect to the database for updating and visualization purposes. At a starting point, the user should register or authenticate into the program to create a new table in the cloud database or retrieve data from a previouly created table, respectively.

## Auth

__Responsibility__:
* To authenticate user or to register new users

__Behaviors__:
* `SignUp()` : register new users by prompting for a username and password
* `LogIn()` : authenticate old users by checking username and password

__Attributes__:
`file_user_credentials` : A file where username and password will be saved when signing up


## Interface

__Responsibility__:
* To show and update goals

__Behaviors__:
* `_Prompt()`: The user can ask to visualize, add, modify, or delete items on the remote database
* `_UpdatePandas()`: Calls for Database class to make a conection the cloud database and build a pandas dataframe
* `_PromptToContinue()`: Whether or not to continue running the program
* `_Visualize()`: Display updated goals by retrieving information from cloud database
* `_GetDate()`: Asks the user for a date in which an item from the database will be modified
* `_PutItem()`: Add or modify an item to the remote database
* `_DeleteItem()`: Remove an item from the remote database

__Attributes__:
* `tableName`: Name of one of the tables from the remote database
* `database`: An instance of the Database class which will transform user prompts into actions in the cloud database
* `df`: The remote table converted into a pandas dataframe



## Database : to connect with cloud database

__Responsibility__:
* To connect with cloud database and modify its content according to the prompts in the interface

__Behaviors__:
* `_ConnectWithTable()`: The code stablishes a connection with the DynamoDB AWS database
* `BuildPandas()`: It builds a pandas dataframe by using information in the cloud database
* `_Retrieve()`: The class uses this private method to build visualizations
* `PutItem()`: User can add/modify a row from the table
* `DeleteItem()`: User can delete a row from the table

__Attributes__:
* `_table`: The connection to the remote database




# Basic flux

The main program calls `Auth` to authenticate the user. Different users can participate in the goal tracker. For each user, the program calls `Interface` to show the state of the goals and to allow updates. The `Database`class will allow those changes into the cloud database from the user's local device.