#  Covid Managament System for HMO
Covid database management system for a large HMO. The system will present the members in the HMO, and will manage the entry of the records in a database. In addition, the system will store key information regarding the covid epidemic in the context of the members of the HMO. In the future, they will be able to turn to this database in order to carry out various retrievals. <br/>
The available system options:
* Entering a new client to the HMO (entering the personal details and details about the covid)
* Get details of a client that exists at the checkout

## Technologies:
* PyCharm 2019.2
* Firebase Realtime Database

## Languages:
Server side:
* Python
Client side:
* HTML
* CSS
* JavaScript

## Packages:
to run this project, install it locally using pip:
* pip install flask
* pip install pyrebase


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
 * Retrieving the details about the client is through the client's ID - the unique identifier.
 * A client can get sick with covid no more than once.
 * A client can receive a maximum of 4 vaccinations.
 * A client doesn't have to be vaccinated at all.
 * When displaying the user's details, all the personal details will be displayed.
 * When displaying user information, sick and recovery dates will not be displayed for clients who have not fallen ill.
 * When displaying the user details, the vaccination details will not be shown to the client who has not been vaccinated.


