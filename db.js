//include the line to use the functions in this function: var db = require('./db.js');
var firebase = require('firebase');

var db = firebase.initializeApp({
    apiKey: "AIzaSyBQW6ZNHg8837ojsDqqBdNlmsw_lVvMkws",
    authDomain: "sms-doctor.firebaseapp.com",
    databaseURL: "https://sms-doctor.firebaseio.com",
    storageBucket: "sms-doctor.appspot.com",
    messagingSenderId: "794541926112"
}, "Secondary");

//-----------------------


function addPatient(data_string){
    var data = JSON.parse(data_string);
    db.database().ref('patients/'+data.phone_number).set(data);
    return;
}

function addDoctor(data_string){
    var data = JSON.parse(data_string);
    db.database().ref('doctors/'+data.phone_number).set(data);
    return;
}

function setRecordStatusToDone(record_id){
  db.database().ref('medical_records/' + record_id).update({"done":"true"});
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
       symptoms   : data.symptoms,
       done       : "false"
    });
}

function editRecord(record_id, data_string){
  var data = JSON.parse(data_string);
  db.database().ref('medical_records/' + record_id).update(data);
}

//records will be returned in reverse chronological order (ie the first record to be returned would be the most recent record)
//start-end states the desired records (if start = 1 and end = 5, then the 5 most recent records will be returned)
function getPatientRecord(record_id){
  var ref = db.database().ref('medical_records/' + record_id);
  ref.once("value", function(snapshot){
    record = snapshot.val();
  }).then(function(){
    return record;
  });
}


exports.addRecord = addRecord;
exports.addPatient = addPatient;
exports.editRecord = editRecord;
exports.setRecordStatusToDone = setStatusToDone;
exports.getPatientRecord = getPatientRecord;
