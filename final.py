#!/usr/bin/env python2
#encoding: UTF-8
#!/usr/bin/env python
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from flask import Flask, request, redirect
import twilio.twiml
import codecs
from flask import Flask
from twilio.rest import TwilioRestClient
import twilio.twiml
from twilio.rest import TwilioRestClient
 
 #create twilio rest client
client = TwilioRestClient('AC42d04385a40c693a15db59dbe607f5cf','65790381838a7f995e8617ad6b2926e3')
 
#save contents of file to string variable data and encode them to recognize special characters
with open('trans.txt', encoding='utf-8') as f:
    for line in f:
        string=(repr(line))
        #remove BOM character from beginning of text
        data = string.replace("ufeff", "")

        #send sms 
client.messages.create(from_='(226)790 3907',
                       to='(519)573 7527',
                       body=data)

#twilio account credentials
account_sid = "AC42d04385a40c693a15db59dbe607f5cf"
auth_token = "65790381838a7f995e8617ad6b2926e3"
client = TwilioRestClient(account_sid, auth_token)

#read in and decode file with phonetic translation (default voice does not pronouce well, so mp3 file was used instead)
#with open('translate.txt', encoding='utf-8') as f:
 #   for line in f:
  #      test=(repr(line))

#twilio calls and speaks bengali translation of notification/update  
app = Flask(__name__)
  
call = client.calls.create(to="+15195737527", # Any phone number
                           from_="+12267903907", # Must be a valid Twilio number
                           url="https://drive.google.com/uc?export=download&id=0B72pHJgClYFbYU1DT1ZWby10Y3c")
print(call.sid)

if __name__ == "__main__":
    app.run(debug=True)
    
    #various sound files
    #https://drive.google.com/file/d/0B72pHJgClYFbdDd1cFZubFlYVGM/view?usp=sharing
    #https://drive.google.com/file/d/0B72pHJgClYFbdDd1cFZubFlYVGM/view.mp3
    #https://drive.google.com/uc?export=download&id=0B72pHJgClYFbdDd1cFZubFlYVGM
    #https://drive.google.com/uc?export=download&id=0B72pHJgClYFbdDd1cFZubFlYVGM
	#https://drive.google.com/uc?export=download&id=0B72pHJgClYFbYU1DT1ZWby10Y3c
    
   