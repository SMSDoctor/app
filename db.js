//include the line to use the functions in this function: var db = require('./db.js');

var firebase = require('firebase');

var db = firebase.initializeApp({
    apiKey: "AIzaSyBQW6ZNHg8837ojsDqqBdNlmsw_lVvMkws",
    authDomain: "sms-doctor.firebaseapp.com",
    databaseURL: "https://sms-doctor.firebaseio.com",
    storageBucket: "sms-doctor.appspot.com",
    messagingSenderId: "794541926112"
}, "Secondary");

function addRow(){
    db.database().ref('test_table/test_row4').set({
       test_column : 'test value'
    });
}

exports.addRow = addRow;
