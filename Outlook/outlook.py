from O365 import Account

# Access Account
credentials = ('client_id', 'client_secret')
account = Account(credentials)

# Send Email
m = account.new_message()
m.to_add('to_email@example.com')
m.subject = 'Test!'
m.body = "This is a test message"
m.send()

# Retrieve Email
