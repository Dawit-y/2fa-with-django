from twilio.rest import Client
from decouple import config

account_sid = config('account_sid')
auth_token = config('auth_token')
client = Client(account_sid, auth_token)

def send_sms(code, phone_number):
    message = client.messages.create(
    from_= config('from_'),
    body=f'Hey there here is test AUTH message and your code is {code}',
    to=f'{phone_number}'
    )

    print(message.sid)