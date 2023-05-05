# Classes definition
The *Cloud Goal Tracker* program will help you to achieve your goals through gamification (turning your goals into a game) throught the use AWS DynamoDB cloud database and Python libraries to connect to the database for updating and visualization purposes. At a starting point, the user should register or authenticate into the program to create a new table in the cloud database or retrieve data from a previouly created table, respectively.

## Auth

__Responsibility__:
* To authenticate user or to register new users

__Behaviors__:
* `Register()` : register new users by prompting for a username and password
* `Authenticate()` : authenticate old users by checking username and password

__Attributes__:



## Interface

__Responsibility__:
* To show and update goals

__Behaviors__:
* `Interface()` : constructor. Call Build_first_table() for new users. Then call `Visualize()`
* `Build_first_table()`: Help new user to set up goals
* `Visualize()` : Display updated goals by retrieving information from cloud database
* `Update()`    : The user will receive prompts to insert, modify, delete information by calling functions from the DB class

__Attributes__:



## Database : to connect with cloud database

__Responsibility__:
* To connect with cloud database and modify its content according to the prompts in the interface

__Behaviors__:
* `Insert()`   : user can insert new goal, the program will insert data from local device into the cloud database
* `Modify()`   : user can update a goal if he forgot to do that in a previous day
* `Delete()`   : user can delete a goal
* `Retrieve()` : the program will retrieve data to plot/show on screen

__Attributes__:





# Basic flux

The main program calls `Auth` to authenticate the user. Different users can participate in the goal tracker. For each user, the program calls `Interface` to show the state of the goals and to allow updates. The `Database`class will allow those changes into the cloud database from the user's local device.