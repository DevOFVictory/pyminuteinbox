"""
Print out all incoming mails
"""

from pyminuteinbox import TempMailInbox, TempMail
import time

inbox = TempMailInbox()
print(f'Looged into inbox "{inbox.address}"!')

amount = len(inbox.get_all_mails())

while True:
    if len(inbox.get_all_mails()) > amount:
        amount = len(inbox.get_all_mails())

        mail: TempMail = inbox.get_latest_mail()

        print('-'*10)
        print('[ New mail recevied! ]')
        print('Subject: ' + mail.subject)
        print('Sender Name: ' + mail.sender_name)
        print('Sender Address: ' + mail.sender_address)
        print('Time: ' + mail.time_sent)
        print('Content: ' + mail.content)
        print('-'*10)

    time.sleep(1)