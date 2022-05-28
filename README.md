# PyMinuteInbox
> A simple python api wrapper libary for https://www.minuteinbox.com

### Installation
Run the following command to install
```bash
$ pip install pyminuteinbox
```


### Usage
```python
# Import the libary
from pyminuteinbox import TempMailInbox, TempMail

# Create new Temp Mail Inbox
inbox = TempMailInbox()

# Fetch the latest mail
mail: TempMail = inbox.get_latest_mail()

# Print the inbox amount
print(f'Currently {str(len(inbox_get_all_mails()))} mails in inbox.')


print(f'Mail {mail.subject} from {mail.sender} received.')
```
