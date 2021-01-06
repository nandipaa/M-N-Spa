from twilio.rest import Client
import math, random
from django.core.mail import EmailMessage


def send_sms(account_sid, auth_token, body, from_, to_):
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body=body,
        from_=from_,
        to=to_,
    )


def generateOTP():

    digits = "0123456789"
    OTP = ""

    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]

    return OTP


def send_email(body, to, from_email):

    email = EmailMessage(
        body=body,
        to=to,
        from_email=from_email,
    )



