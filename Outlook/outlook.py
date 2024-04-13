from O365 import Account

credentials = ('client_id', 'client_secret')

account = Account(credentials)
m = account.new_message()
m.to_add('to_email@example.com')
m.subject = 'Test!'
m.body = "This is a test message"
m.send()