import smtplib, ssl
from flask import Flask, jsonify, request
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)


@app.route('/sendMail', methods=['POST'])
def sendMail():
    sender_email = request.json['sender_email'] # SENDER EMAIL
    receiver_email = request.json['reciever_email'] # RECIEVER EMAIL
    password = request.json['host_password'] # HOST PASSWORD


    message = MIMEMultipart("alternative") # MAIL BODY
    message["Subject"] = request.json['email_subject'] # MAIL SUBJECT
    message["From"] = sender_email
    message["To"] = receiver_email
    body = MIMEText(request.json['message'], "plain")

    message.attach(body)

    try:
        server = smtplib.SMTP_SSL(request.json['smtp_server'], request.json['smtp_port'], context=ssl.create_default_context()) #SMTP DETAILS
        # server.starttls()
        server.login(sender_email, password)
        print("Login success")
        server.sendmail(sender_email, receiver_email, message.as_string())
    except Exception as e:
        return jsonify({'response' : 'An error occured {}'.format(e)})
    
    return jsonify({'response' : 'Email sent to {}'.format(receiver_email)})




 


