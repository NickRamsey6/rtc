from O365 import Account

# Access Account
credentials = ('client_id', 'client_secret')
account = Account(credentials)

# Send Email
def send_email(send_to_address, subject, body):
    m = account.new_message()
    m.to_add(send_to_address)
    m.subject = subject
    m.body = body
    m.send()

# Retrieve Email
