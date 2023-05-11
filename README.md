#  Covid Managament System for HMO


## Technologies:
* PyCharm 2019.2
* Firebase Realtime Database

## languages:
* Python
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
