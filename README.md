# Password-Locker
## Author

[Ahmed Mohamed](https://github.com/Ahmed-moringa)

## Description

This project is a python application that manages login and signup credentials of a person for various accounts i.e. username and passwords for each account. 

## Screenshot

[![Screenshot-2021-12-07-at-02-13-27.png](https://i.postimg.cc/s2bM1wFx/Screenshot-2021-12-07-at-02-13-27.png)](https://postimg.cc/gwqzTy2b)

## User Stories
The user would like to.... :
1. To create a password locker account with my details, a login username and password.
2. To store my already existing account credentials in the application.
3. To create new account credentials in the application.   
4. To have the option of putting in a password that I want to use for the new credential account. 
5. To delete a credentials account that I no longer need in the application.


## Installation / Setup instruction

#### The application requires the following installations to operate 
* python3
* pip
* pyperclip

#### Cloning

* Open Terminal {Ctrl+Alt+T}

* git clone ```https://github.com/Ahmed-moringa/Password-locker.git```

* cd Password-Locker

* open folder based on the text editor you have.

### Running the Application
* To run the application, open the cloned file in terminal and run the following commands:

        $ chmod +x interface.py
        $ ./interface.py
* To run test for the application
        $ python3 locker_test.py

## Behaviour Driven Development
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
|Open the application on the terminal | Run the command ```$ ./run.py```|Hello Welcome to your Accounts Password Safe... <br>* CA ---  Create New Account * LI ---  Have An Account |
|Select  CA| input username and password| Hello ```username```, Your account has been created succesfully! Your password is: ```password```|
|Select LI  | Enter your password and username you signed up with| Abbreviations menu to help you navigate through the application|
|Store a new credential in the application| Enter ```CC```|Enter Account, username, password<br>choose ```tp``` to enter your password or ```gp``` for the application to generate a password for you |
|Display all stored credentials | Enter ```DC```|A list of all credentials that has been stored or ```You don't have any credentials saved yet``` |
|Find a stored credential based on account name|Enter ```FC```| Enter the Account Name you want to search for and returns the account details|
|Delete an existing credential that you don't want anymore|Enter ```D```|Enter the account name of the Credentials you want to delete and returns true if the account has been deleted and false if the account doesn't exixt|
|Exit the application| Enter ```D```| The application exits|

## Technologies Used

* python3

## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug

## License
* *MIT License:*
* Copyright (c) 2021 **Ahmed Mohamed**
