# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACa3620873dc357410bcbabd1ece40e08c'
auth_token = '1fc7c7a7c4cbe0201a8124d6d0051528'
client = Client(account_sid, auth_token)

# message = client.messages \
#                 .create(
#                      body="Join Earth's mightiest heroes. Like Kevin Bacon.",
#                      from_='+15017122661',
#                      to='+919970533440'
#                  )
message = client.messages.create(
                              from_='whatsapp:+14155238886',
                              body='Hello PetoCare User, You there!',
                              to='whatsapp:+917620695473'
                          )
print(message)
print(message.sid)
