//include the line to use the functions in this function: var db = require('./db.js');
var firebase = require('firebase');

var db = firebase.initializeApp({
    apiKey: "AIzaSyBQW6ZNHg8837ojsDqqBdNlmsw_lVvMkws",
    authDomain: "sms-doctor.firebaseapp.com",
    databaseURL: "https://sms-doctor.firebaseio.com",
    storageBucket: "sms-doctor.appspot.com",
    messagingSenderId: "794541926112"
}, "Secondary");

function addPatient(data_string){
    var data = JSON.parse(data_string);
    db.database().ref('patients/'+data.phone_number).set(data);
    return;
}

function addRecord(data_string){
    var data = JSON.parse(data_string);

    //record date/time of record as current date/time
    var date = new Date();
    var formatted_time = date.getHours() + ":" + date.getMinutes();
    var formatted_date = date.getDate() + "-" + ( date.getMonth() + 1 ) + "-" + date.getFullYear();

    db.database().ref('medical_records').push({
       patient_id : data.caller_num,
       time       : formatted_time,
       date       : formatted_date,
       symptoms   : data.symptoms
    });
}

function editRecord(record_id, data_string){
  var data = JSON.parse(data_string);
  db.database().ref('medical_records/' + record_id).update(data);
}

exports.addRecord = addRecord;
exports.addPatient = addPatient;
exports.editRecord = editRecord;
