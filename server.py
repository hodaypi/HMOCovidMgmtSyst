from flask import Flask
from flask import request
from flask import jsonify
import json
from flask import render_template, redirect

# connect to Firebase

import pyrebase

# from collections.abc import MutableMapping
# from pyrebase import initialize_app

# connect to firebase Databese:

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
# "1p": {"vaccineDose": "Booster1", "vaccineProducer": "Pfizer"},
# "2p": {"vaccineDose": "Booster2", "vaccineProducer": "Pfizer"},
# "3p": {"vaccineDose": "Booster3", "vaccineProducer": "Pfizer"},
# "4p": {"vaccineDose": "Booster4", "vaccineProducer": "Pfizer"},
# "1m": {"vaccineDose": "Booster1", "vaccineProducer": "Moderna"},
# "2m": {"vaccineDose": "Booster2", "vaccineProducer": "Moderna"},
# "3m": {"vaccineDose": "Booster3", "vaccineProducer": "Moderna"},
# "4m": {"vaccineDose": "Booster4", "vaccineProducer": "Moderna"},
# "1a": {"vaccineDose": "Booster1", "vaccineProducer": "AstraZeneca"},
# "2a": {"vaccineDose": "Booster2", "vaccineProducer": "AstraZeneca"},
# "3a": {"vaccineDose": "Booster3", "vaccineProducer": "AstraZeneca"},
# "4a": {"vaccineDose": "Booster4", "vaccineProducer": "AstraZeneca"}
# }
#
# for id, data in dictOfVaccines.items():
#     db.child("Covid's Vaccines").child(id).set(data)

#########################################



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

#######################
# client = db.child("Clients Details").child("123451231").get()
# clientID = client.key()
# clientD = client.val()
# print(clientID,clientD)
# had=db.child("Clients Details").child("123453241").child("positiveCovidDate").get()
# if had.val()==None:
#     getcovid="didnt get covid"
#     print(getcovid)
# else:
#     getcovid=had.val()
# health=db.child("Clients Details").child("123453241").child("covidRecoveryDate").get()
# if health.val()==None:
#     finishcovid="didnt heal covid"
#     print(finishcovid)
# else:
#     finishcovid=health.val()


# getvaccine=db.child("Clients Details").child("987654321").child("Vaccines").get()
# if getvaccine.val()==None:
#     vac="didnt get vac covid"
#     print(vac)
# else:
#     clientVaccine=getvaccine.val()
#     print(clientVaccine)
#     print(clientVaccine.values())
#     # check = 0
#     for i in clientVaccine.keys():
#         booster =db.child("Covid's Vaccines").child(i).child("vaccineDose").get()
#         print(booster.val())
#         producer = db.child("Covid's Vaccines").child(i).child("vaccineProducer").get()
#         print(producer.val())
#         date=db.child("Clients Details").child("987654321").child("Vaccines").child(i).child("vaccineDate").get()
#         print(date.val())


#
#         if request.form['get' + str(i)] == "Yes" and check == 0:
#                             vaccineDate = request.form['vaccineDate' + str(i)]
#                             if request.form['producer' + str(i)] == "Pfizer":
#                                 idOfVaccine = db.child("Covid's Vaccines").child('p' + str(i)).get()
#                             elif request.form['producer' + str(i)] == "Moderna":
#                                 idOfVaccine = db.child("Covid's Vaccines").child('m' + str(i)).get()
#                             else:
#                                 idOfVaccine = db.child("Covid's Vaccines").child('a' + str(i)).get()
#                             db.child("Clients Details").child(clientId).child("Vaccines").child(idOfVaccine.key()).set(
#                                 {"vaccineDate": vaccineDate})
#
# #
# #


app = Flask(__name__)


# func check if the field is empty or not
def fieldIsFull(detail):
    if detail != "":
        return True
    else:
        return False


# func check if the data is exist or not
def dataExist(val):
    if val is not None:
        return True
    else:
        return False


# main screen- this page shown first
@app.route('/', methods=['GET', 'POST'])
def welcomeScreen():
    try:
        if request.method == 'POST':
            # When the user chooses to add new client, it redirects to fit page
            if request.form['submit'] == 'Add':
                return render_template('addNewClient.html')
            # When the user chooses to get specific client details, it redirects to fit page
            elif request.form['submit'] == 'Search':
                return render_template('findClient.html')
    except:
        someError = "An error occurred. Check the connection"
        return render_template("welcomeScreen.html", failure=someError)
    return render_template("welcomeScreen.html")


# When the user chooses to add a new client, it redirects to this page and activates addNewClient() func
# //addNewClient
@app.route('/addNewClient', methods=['GET', 'POST'])
def addNewClient():
    try:
        if request.method == 'POST':
            if request.form['submit'] == 'add':
                clientId = request.form['id']
                # client already exist id.val != None
                if dataExist(db.child("Clients Details").child(clientId).get().val()):
                    existClient = "The client already exists in the system, try to enter another ID"
                    return render_template('addNewClient.html', failure=existClient)
                else:
                    # insert personal details, and set the ID as unique key
                    db.child("Clients Details").child(clientId).set(
                        {
                            "firstName": request.form['fname'],
                            "lastName": request.form['lname'],
                            "birthday": request.form['bday'],
                            "address": request.form['street'] + " " + request.form['number'] + ", " + request.form['city'],
                            "telephone": request.form['tel'],
                            "cellPhone": request.form['phone']})
                    # insert the date of the illness with Covid and the date of recovery if they exist
                    if fieldIsFull(request.form['positiveDate']):
                        db.child("Clients Details").child(clientId).update(
                            {"positiveCovidDate": request.form['positiveDate']})
                        if fieldIsFull(request.form['recoveryDate']):
                            db.child("Clients Details").child(clientId).update(
                                {"covidRecoveryDate": request.form['recoveryDate']})
                    # insert the date of getting covid's vaccines if exist
                    check = 0
                    # Client can get a maximum of 4 vaccines
                    for i in range(1, 4):
                        if request.form['get' + str(i)] == "Yes" and check == 0:
                            vaccineDate = request.form['vaccineDate' + str(i)]
                            if request.form['producer' + str(i)] == "Pfizer":
                                idOfVaccine = db.child("Covid's Vaccines").child(str(i) + 'p').get()
                            elif request.form['producer' + str(i)] == "Moderna":
                                idOfVaccine = db.child("Covid's Vaccines").child(str(i) + 'm').get()
                            else:
                                idOfVaccine = db.child("Covid's Vaccines").child(str(i) + 'a').get()
                            db.child("Clients Details").child(clientId).child("Vaccines").child(idOfVaccine.key()).set(
                                {"vaccineDate": vaccineDate})
                        # If client didn't get the first vaccine- he didn't get the next ones either
                        else:
                            check = 1
                    # if success return to main screen
                    return render_template('welcomeScreen.html')
    # If there is a problem adding the user to the database/ there is a problem with the data
    except:
        error = "An error occurred, check the database/server connection and try again"
        return render_template('addNewClient.html', failure=error)
    return render_template('addNewClient.html')


# When the user chooses to get specific client details, it redirects to this page and activates findClient() func
#  //clientDetails
@app.route('/findClient', methods=['GET', 'POST'])
def findClient():
    # print("func of find a client")
    if request.method == 'POST':
        if request.form['submit'] == 'Search':
            idOfClient = request.form['id']
            try:
                client = db.child("Clients Details").child(idOfClient).get()
                clientID = client.key()
                clientD = client.val()
                personalDetails = [clientD["firstName"] + " " + clientD["lastName"],
                                   clientID,
                                   clientD["address"],
                                   clientD["birthday"],
                                   clientD["telephone"],
                                   clientD["cellPhone"]]

                gotCovid = db.child("Clients Details").child(idOfClient).child("positiveCovidDate").get()
                if not dataExist(gotCovid.val()):
                    getCovid = "The client doesn't have covid"
                else:
                    getCovid = gotCovid.val()

                finishCovid = db.child("Clients Details").child(idOfClient).child("covidRecoveryDate").get()
                if not dataExist(finishCovid.val()):
                    recoverCovid = "The client doesn't recovered from covid"
                else:
                    recoverCovid = finishCovid.val()

                getVaccine = db.child("Clients Details").child(idOfClient).child("Vaccines").get()
                if not dataExist(getVaccine.val()):
                    vaccineCovid = "The client hasn't received covid vaccine"
                    vaccineList = []
                else:
                    vaccineCovid = "The client received:"
                    clientVaccine = getVaccine.val()
                    vaccineList = []
                    for i in clientVaccine.keys():
                        vList = []
                        booster = db.child("Covid's Vaccines").child(i).child("vaccineDose").get()
                        vList.append(booster.val())

                        producer = db.child("Covid's Vaccines").child(i).child("vaccineProducer").get()
                        vList.append(producer.val())

                        date = db.child("Clients Details").child(idOfClient).child("Vaccines").child(i).child(
                            "vaccineDate").get()
                        vList.append(date.val())

                        vaccineList.append(vList)
                # if success redirect to ClientDetails page that shown the client card
                return render_template('ClientDetails.html',
                                       personal=personalDetails,
                                       sick=getCovid,
                                       healthy=recoverCovid,
                                       vaccine=vaccineCovid,
                                       listOfVaccine=vaccineList)
            # If the client does not exist / there is a problem and cannot bring details
            except:
                noClient = "The client is not exist in the system. Try to enter another ID"
                return render_template('findClient.html', failure=noClient)
        return render_template('findClient.html')
    return render_template('findClient.html')


if __name__ == '__main__':
    app.run(debug=True)
