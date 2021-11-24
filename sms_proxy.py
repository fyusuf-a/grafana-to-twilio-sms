from flask import Flask, request
import json
import os
import dotenv
import twilio.rest

dotenv.load_dotenv()

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
number_from = os.environ['TWILIO_NUMBER_FROM']
number_to = os.environ['TWILIO_NUMBER_TO']

client = twilio.rest.Client(account_sid, auth_token)

app = Flask(__name__)

@app.route('/sms', methods=['POST'])
def home():
    message = client.messages.create(
        body='Problem with project ' + request.args['project'],
        from_=number_from,
        to=number_to
    )
    print(message)
    return 'OK'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
