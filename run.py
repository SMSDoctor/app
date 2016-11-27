from flask import Flask, request, redirect
import twilio.twiml
import json

app = Flask(__name__)

callers = {
    "+14158675309": "Curious George",
    "+14158675310": "Boots",
    "+15195737527": "Knajwa",
    "+15197299126": "Marcel"
}

with open('ivrsData.json') as data_file:    
    data = json.load(data_file)
kys=data[0].keys()
kys1=data
itern = 0
ch1 = 0
ch2 =0


@app.route("/", methods=['GET', 'POST'])

def hello_monkey():
    from_number = request.values.get('From', None)
    f = open('workfile.txt', 'w+')
    f.write("{\"caller_num\" : \""+ from_number+ "\", \"symptoms\" :[ ")
    f.close()

    if from_number in callers:
        caller = callers[from_number]
    else:
        caller = "Monkey"

    resp = twilio.twiml.Response()
    # Greet the caller by name
    resp.say("Hello " + caller)
    # Play an mp3
    #resp.play("http://demo.twilio.com/hellomonkey/monkey.mp3")

    # Say a command, and listen for the caller to press a key. When they press
    # a key, redirect them to /handle-key.
    with resp.gather(numDigits=1, action="/handle-key", method="POST") as g:
        g.say("What are the symptoms of the patient? For respiratory distress, press 1. For sudden loss of consciousness , press 2.")

    return str(resp)
    
    
@app.route("/handle-key", methods=['GET', 'POST'])

def handle_key():
    """Handle key press from a user."""

    # Get the digit pressed by the user
    digit_pressed = request.values.get('Digits', None)
       
    global itern
    global ch1
    global ch2

    itern=itern+1
    if (itern == 1): 
            ch1 = int(digit_pressed)
    if(itern == 2):
            ch2 = int(digit_pressed)

    print(itern)
    if (itern == 1):
        if (digit_pressed == "1"): 
            f = open('workfile.txt', 'a+')
            f.write("\"respiratory distress \", ")
            f.close()

            resp = twilio.twiml.Response()

            with resp.gather(numDigits=1, action="/handle-key", method="POST") as g:
                g.say("What are the symptoms? For not breathing, press 1. For a bluish color, press 2. For fast breathing, press 3")
            return str(resp)

        if (digit_pressed == "2"): 
            f = open('workfile.txt', 'a+')
            f.write("\"loss of consciousness\", ")
            f.close()


            resp = twilio.twiml.Response()
       
            with resp.gather(numDigits=1, action="/handle-key", method="POST") as g:
                g.say("What are the symptoms? For no convusions, press 1. For uncontrolled, jerky movements of the limbs, or stiffening of the limbs, press 2.")
            return str(resp)

        return redirect("/")

    if (itern == 2):
        if(ch1 == 1):
            if (digit_pressed  == "1"): 
                f = open('workfile.txt', 'a+')
                f.write("\"not breathing\"]} ")
                f.close()

                resp = twilio.twiml.Response()
        
                with resp.gather(numDigits=1, action="/handle-key", method="POST") as g:
                    g.say("If the airway appears obstructed, open the airway by tilting the head back slightly")
                return str(resp)
            if (digit_pressed  == "2"): 
                f = open('workfile.txt', 'a+')
                f.write("\"bluish color\"]} ")
                f.close()

                resp = twilio.twiml.Response()

                with resp.gather(numDigits=1, action="/handle-key", method="POST") as g:
                    g.say("If the airway appears obstructed, open the airway by tilting the head back slightly")
                return str(resp)
            if (digit_pressed  == "3"): 
                f = open('workfile.txt', 'a+')
                f.write("\"fast breathing\"]} ")
                f.close()

                resp = twilio.twiml.Response()

                with resp.gather(numDigits=1, action="/handle-key", method="POST") as g:
                    g.say("If possible, refer to hospital. Give fluids and give oxygen if available. Dose with paracetamol every 6 hours if the child has a fever. Keep child warm, dry and well wrapped")
                return str(resp)
            return redirect("/")

        if(ch1 == 2):
            if (digit_pressed  == "1"): 
                f = open('workfile.txt', 'a+')
                f.write("\"no convulsions\"]} ")
                f.close()

                resp = twilio.twiml.Response()
        
                with resp.gather(numDigits=1, action="/handle-key", method="POST") as g:
                    g.say("In case of trauma, stabilize neck first so that it does not move. If the airway appears obstructed, open the airway by tilting the head back slightly")
                return str(resp)
            if (digit_pressed  == "2"): 
                f = open('workfile.txt', 'a+')
                f.write("\"convulsions\"]} ")
                f.close()

                resp = twilio.twiml.Response()

                with resp.gather(numDigits=1, action="/handle-key", method="POST") as g:
                    g.say("Ensure the mouth and airway are clear, but do not insert anything into the mouth to keep it open. Turn the child on his or her side to avoid aspiration.")
                return str(resp)
            return redirect("/")    
   

        return redirect("/")

    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)
