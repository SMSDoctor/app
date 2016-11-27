//include the line to use the functions in this function: var db = require('./db.js');

var firebase = require('firebase');

var db = firebase.initializeApp({
    apiKey: "AIzaSyBQW6ZNHg8837ojsDqqBdNlmsw_lVvMkws",
    authDomain: "sms-doctor.firebaseapp.com",
    databaseURL: "https://sms-doctor.firebaseio.com",
    storageBucket: "sms-doctor.appspot.com",
    messagingSenderId: "794541926112"
}, "Secondary");

function findPatientByPhone(phone_number){
    //TODO: write actual code
    return 12
}

function addRecord(caller_num, symptms){
    //from phone number, determine the id of the patient
    var id = findPatientByPhone(caller_num);

    //record date/time of record as current date/time
    var date = new Date();
    var formatted_time = date.getHours() + ":" + date.getMinutes();
    var formatted_date = date.getDate() + "-" + ( date.getMonth() + 1 ) + "-" + date.getFullYear();

    db.database().ref('medical_records/24-10-2113_' + id).set({
       patient_id : id,
       time       : formatted_time,
       date       : formatted_date,
       symptoms   : symptms
    });
}

exports.addRecord = addRecord;
