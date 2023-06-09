#  Covid Managament System for HMO
Covid database management system for a large HMO. The system will present the members in the HMO, and will manage the entry of the records in a database. In addition, the system will store key information regarding the covid epidemic in the context of the members of the HMO. In the future, they will be able to turn to this database in order to carry out various retrievals. <br/>
The available system options:
* Entering a new client to the HMO (entering the personal details and details about the covid)
* Get details of a client that exists at the checkout

## Technologies:
* Firebase Realtime Database
  * Establishing a database for the system.
* PyCharm 2019.2
  * Setting up a local flask server in Python.
  * Connecting the database to the server in Python.
  * Establishing a client side - for a user-friendly user interface using HTML, CSS, JavaScript.
 
## Languages:
### Server side:
* Python
### Client side:
* HTML
* CSS
* JavaScript

## Setup:
to run the system <br />
* Install Pycharm or any other software where you can run Python software
* Open a project
* Install the required libraries locally using pip:
  * pip install flask
  * pip install pyrebase
* Download the server.py file and the templates folder
* Make sure the templates folder has 4 files:
  * welcomeScreen.html
  * addNewClient.html
  * findClient.html
  * clientDetails.html
* Run the server.py file
* Click on the local flask server that was build and the website will be presented. <br />
## Mock Up:
By clicking on the domain, a main screen will be displayed
![welcome](https://github.com/hodaypi/HMOCovidMgmtSyst/assets/62617707/3d0b3cc1-8063-4904-a2df-7f79d8512aff) 
<br />
Clicking on "Add a new client" will redirect you to the "Add a new client" screen <br />
![add](https://github.com/hodaypi/HMOCovidMgmtSyst/assets/62617707/8a70de84-39b0-443f-969f-5b61fe9c4226)
<br />
Clicking on "submit" will add the new client to the database (if the form is filled out as required) and redirect the user to the main screen.<br />
![welcome](https://github.com/hodaypi/HMOCovidMgmtSyst/assets/62617707/a4db18dd-eeae-48aa-9214-e0b8bfc31e91)
<br />
Clicking on the "Search Client" button will redirect you to the "Search Client" page <br />
![search](https://github.com/hodaypi/HMOCovidMgmtSyst/assets/62617707/4a2ca766-6e0d-4c2d-95f5-6b6e56933d26) 
<br />
Clicking the "search" button will redirect you to the "client details" page (if the client exists in the system)
<br />
![client](https://github.com/hodaypi/HMOCovidMgmtSyst/assets/62617707/4794a65f-9e50-42f4-96bf-5896a0679ed1)





## Assumptions:
* There are 3 covid vaccine producers :
  * Pfizer
  * Moderna
  * AstraZeneca
* Each vaccine producer has 4 types of doses:
  * booster 1
  * booster 2
  * booster 3
  * booster 4
 * Adding a new client to the system will create a record where the unique key of the record is the client's ID.
 * A client can get sick with covid no more than once.
 * There should be at least 7 days between positive date and the recovery date.
 * A client can receive a maximum of 4 vaccinations.
 * A client doesn't have to be vaccinated at all.
 * Receiving the first vaccine is no less than six months after birth.
 * Receiving the second vaccine is no less than a month after receiving the first vaccine.
 * Receiving the third vaccine is no less than 5 months after receiving the second vaccine.
 * Receiving the fourth vaccine is no less than 4 months after receiving the third vaccine.
 * Retrieving the details about the client is through the client's ID - the unique identifier.
 * When displaying the user's details, all the personal details will be displayed.
 * When displaying user information, sick and recovery dates will not be displayed for clients who have not fallen ill.
 * When displaying the user details, the vaccination details will not be shown to the client who has not been vaccinated.


