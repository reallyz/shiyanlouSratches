from twilio.rest import Client

account_id='AC6971e3223d664040108e4ee6b1a3e49a'
auth_token='3d4aba19dc0b09d4f5cbba98fa794ddd'

client=Client(account_id,auth_token)
message=client.messages.create(
    to='+8619981555989',
    from_='+17159554647',
    body='Hello world'
)
print(message.sid)
message_id='SM73da60648e714ac28c9fbda5aaaa3429'