from flask import Flask
from flask import request
from flask import jsonify
import json
from flask import render_template, redirect

# connect to Firebase

import pyrebase

# from collections.abc import MutableMapping
# from pyrebase import initialize_app

config = {
    "apiKey": "AIzaSyD_LSxNAWSX0wn0NXFVFi-W6mwfqj7HhzM",
    "authDomain": "hmocovidmgmtsyst.firebaseapp.com",
    "databaseURL": "https://hmocovidmgmtsyst-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "hmocovidmgmtsyst",
    "storageBucket": "hmocovidmgmtsyst.appspot.com",
    "messagingSenderId": "696678208500",
    "appId": "1:696678208500:web:68571b0e2162e0f188dfa1"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

# data = {"ID": "123456789", "firstName": "Dan", "lastName": "Tal"}
# # add new client
# id = "1234"
# db.child("try").child(id).set(data)

# update client details
# db.child("clientsDetails").child("names").update({"lastName":"yona"})


# users = db.child("clientsDetails").child("lastName").get()
# users = db.child("clientsDetails").get()
# print(users.key())
# print(users.val())

#########################################

# # Add the Vaccines to the database:
# dictOfVaccines = {
# "p1": {"vaccineDose": "Booster1", "vaccineProducer": "Pfizer"},
# "p2": {"vaccineDose": "Booster2", "vaccineProducer": "Pfizer"},
# "p3": {"vaccineDose": "Booster3", "vaccineProducer": "Pfizer"},
# "p4": {"vaccineDose": "Booster4", "vaccineProducer": "Pfizer"},
# "m1": {"vaccineDose": "Booster1", "vaccineProducer": "Moderna"},
# "m2": {"vaccineDose": "Booster2", "vaccineProducer": "Moderna"},
# "m3": {"vaccineDose": "Booster3", "vaccineProducer": "Moderna"},
# "m4": {"vaccineDose": "Booster4", "vaccineProducer": "Moderna"},
# "a1": {"vaccineDose": "Booster1", "vaccineProducer": "AstraZeneca"},
# "a2": {"vaccineDose": "Booster2", "vaccineProducer": "AstraZeneca"},
# "a3": {"vaccineDose": "Booster3", "vaccineProducer": "AstraZeneca"},
# "a4": {"vaccineDose": "Booster4", "vaccineProducer": "AstraZeneca"}
# }
#
# for id, data in dictOfVaccines.items():
#     db.child("Covid's Vaccines").child(id).set(data)

#########################################

# option 1: but no unique key..
# with open('vaccines.json') as response:
#     data = json.load(response)
# db.set(data)
##########
#
##########
# Read client by his id:
# looking for the client that the HMO employee earch by client id

# clients = db.child("Clients Details").child("-NUmUTa-zhVIBLJ1rTio").get()
#
#
# print(clients.val())
#
# for client in clients.each():
#     # print(client.val())
#     # print(client.key())
#     if client.val()["id"] == "123456":
#         print(client.val())

# first try: it is not smart:
# clients = db.child("Clients Details").get()
#             stop = 0
#             for client in clients.each():
#                 if client.val()["id"] == idOfClient and stop == 0:
#                     print(client.val())
#                     findClient = client.val()
#                     stop = 1
#                     return render_template('findClient.html', t=findClient.values())
#             else:
#                 noClient = "there is no client"
#                 return render_template('findClient.html', s=noClient)
###################
# add new client
# firstName = request.form['fname']
#                 lastName = request.form['lname']
#                 birthday = request.form['bday']
#                 address = request.form['street'] + " " + request.form['number'] + ", " + request.form['city']
#                 telephone = request.form['tel']
#                 cellPhone = request.form['phone']
###############
########################
# check if exist in database:
# check= db.child("Clients Details").child("7").get().val()
# if check!=None:
#     print(check)
# else:
#     print("no one")
#######################
# enter the id of the vaccine to the vaccine list per client:
# vaccine=db.child("Covid's Vaccines").child("p3").get()
# idOfVaccine=vaccine.key()
# db.child("Clients Details").child("123456").child("vaccines").set({"id":idOfVaccine})
# print(idOfVaccine)

#########
# for i in range(1, 5):
#     if request.form['get' + str(i)] == "Yes":
#         print(request.form['producer'+str(i)])
#         idOfvaccine = db.child("Covid's Vaccines").child('p' + str(i)).get()
#         print(idOfvaccine.key())
#         # print()

##########
# idOfVaccine=db.child("Vaccine").get()
# "vacinnes": [
#
# idOfVaccive: {"typeOfVaccine": "p1",
#      "vaccineDate": vaccineDate},
#     {"typeOfVaccine": "p2",
#      "vaccineDate": vaccineDate},
#     {"typeOfVaccine": "p3",
#      "vaccineDate": vaccineDate},
#     {"typeOfVaccine": "p4",
#      "vaccineDate": vaccineDate}],})
#######################


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def welcomeScreen():
    if request.method == 'POST':
        if request.form['submit'] == 'Add':
            return render_template('addNewClient.html')
        elif request.form['submit'] == 'Search':
            return render_template('findClient.html')
    return render_template("welcomeScreen.html")

# //addNewClient
@app.route('/addNewClient', methods=['GET', 'POST'])
def addNewClient():
    # print("func of adding new client")
    if request.method == 'POST':
        if request.form['submit'] == 'add':
            clientId = request.form['id']
            # client already exist id.val != None
            if db.child("Clients Details").child(clientId).get().val() is not None:
                # print("This client already exist")
                existClient = "The client already exists in the system, try to enter another ID"
                return render_template('addNewClient.html', failure=existClient)
            else:
                db.child("Clients Details").child(clientId).set(
                    {
                        "firstName":  request.form['fname'],
                        "lastName": request.form['lname'],
                        "birthday": request.form['bday'],
                        "address": request.form['street'] + " " + request.form['number'] + ", " + request.form['city'],
                        "telephone":  request.form['tel'],
                        "cellPhone": request.form['phone']})
                if request.form['positiveDate'] != "":
                    db.child("Clients Details").child(clientId).update({"positiveCovidDate": request.form['positiveDate']})
                if request.form['recoveryDate'] != "":
                    db.child("Clients Details").child(clientId).update({"covidRecoveryDate": request.form['recoveryDate']})

                check = 0
                for i in range(1, 5):
                    if request.form['get' + str(i)] == "Yes" and check == 0:
                        vaccineDate = request.form['vaccineDate' + str(i)]
                        if request.form['producer' + str(i)] == "Pfizer":
                            idOfVaccine = db.child("Covid's Vaccines").child('p' + str(i)).get()
                        elif request.form['producer' + str(i)] == "Moderna":
                            idOfVaccine = db.child("Covid's Vaccines").child('m' + str(i)).get()
                        else:
                            idOfVaccine = db.child("Covid's Vaccines").child('a' + str(i)).get()
                        db.child("Clients Details").child(clientId).child("Vaccines").child(idOfVaccine.key()).set(
                            {"vaccineDate": vaccineDate})
                    # #  אם לא עשה את הראשון אז מן הסתם שלא עשה את השאר
                    else:
                        check = 1
                return render_template('welcomeScreen.html')
    return render_template('addNewClient.html')


#  //clientDetails
@app.route('/findClient', methods=['GET', 'POST'])
def findClient():
    # print("func of find a client")
    if request.method == 'POST':
        if request.form['submit'] == 'Search':
            idOfClient = request.form['id']
            try:
                client = db.child("Clients Details").child(idOfClient).get()
                theid= client.key()
                theClient = client.val()
                return render_template('ClientDetails.html', success=theClient.items())
            except:
                noClient = "The client is not exist in the system. Try to enter another ID"
                return render_template('findClient.html', failure=noClient)
        return render_template('findClient.html')
    return render_template('findClient.html')


if __name__ == '__main__':
    app.run(debug=True)
