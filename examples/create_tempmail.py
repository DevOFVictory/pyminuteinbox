"""Create a new inbox and login into an existing one"""
from pyminuteinbox import TempMailInbox

# Create new Inbox
inbox1 = TempMailInbox()

print('Address: ' + inbox1.address)
print('Access Code: ' + inbox1.access_token)

# Login into existing inbox
inbox2 = TempMailInbox(address='jonathon.zakiah@ironflys.com', access_token='npjfifirhbbkgnpbirdu')

print('Address: ' + inbox2.address)
print('Access Code: ' + inbox2.access_token)