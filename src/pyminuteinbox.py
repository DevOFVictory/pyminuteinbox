from configparser import NoOptionError
from enum import Enum
import json
import requests, string, random

base_url = 'https://www.minuteinbox.com/index'

class TempMailException(Exception):
    pass

class ExtendTime(Enum):
    MIN_10 = 4200
    HOUR = 3600
    DAY = 86400
    WEEK = 604800
    MONTH = 568523


def generate_address():

    access_token = ''.join([random.choice(string.ascii_lowercase[:21]) for _ in range(20)])

    headers = {
        'Accept': 'application/json',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'close',
        'Cookie': f'PHPSESSID={access_token}'
    }

    resp = requests.get(base_url + '/index', headers=headers)

    return resp.json()['email'], access_token


def fetch_mails(email, access_token):
    try:
        headers = {}
        headers["Accept"] = "application/json"
        headers["X-Requested-With"] = "XMLHttpRequest"
        headers["Connection"] = "close"
        headers["Cookie"] = f"PHPSESSID={access_token}; MI={email}"

        resp = requests.get(base_url + '/refresh', headers=headers)

        new_list = []
        for i in list(resp.json()):
            mail = {'id':i['id'], 'subject': i['predmet'], 'sender': i['od'], 'time':i['kdy'], 'content': i['akce']}
            new_list.append(mail)

        return new_list
    except(requests.JSONDecodeError):
        raise TempMailException('The mail inbox is invalid or expired.')

def force_extend_inbox(time: ExtendTime, email, access_token):
    try:
        headers = {}
        headers["Accept"] = "application/json"
        headers["X-Requested-With"] = "XMLHttpRequest"
        headers["Connection"] = "close"
        headers["Cookie"] = f"PHPSESSID={access_token}; MI={email}"

        requests.get(base_url + '/expirace/' + str(time.value), headers=headers)

    except(requests.JSONDecodeError):
        raise TempMailException('The mail inbox is invalid or expired.')

def fetch_timings(email, access_token):
    try:
        headers = {}
        headers["Accept"] = "application/json"
        headers["X-Requested-With"] = "XMLHttpRequest"
        headers["Connection"] = "close"
        headers["Cookie"] = f"PHPSESSID={access_token}; MI={email}"

        resp = requests.get(base_url + '/zivot', headers=headers).json()
        print('heyy:' + str(resp))

        return {'creation_time': resp['ted'], 'expire_time': resp['konec']}

    except(requests.JSONDecodeError):
        raise TempMailException('The mail inbox is invalid or expired.')


class TempMail():
    """Attributes: id, subject, sender_address, sender_name, content, time_sent"""
    id: int = None
    subject: str = None
    sender_address: str = None
    sender_name: str = None
    content: str = None
    time_sent: str = None

    def __repr__(self) -> str:
        return f'TempMail(id={self.id}, subject={self.subject}, sender={{name={self.sender_name}, address={self.sender_address}}}, time_sent={self.time_sent})'

class TempMailInbox():
    """
    Creates a temp mail inbox.

    It can either login into an existing inbox via entereing address and access_token parameters or create a completly fresh inbox.

    Parameters
    ----------
    address : string
        Optinal: Mail address of inbox
    access_token : str
        Optinal: Access token of inbox

    Returns
    -------
    TempMailInbox
        Object of TempMailInbox
    """

    address = None
    access_token = None

    def __repr__(self) -> str:
        """Srting representation of the inbox"""
        return f'TempMailInbox(address={self.address})'


    def __init__(self, address=None, access_token=None):

        if address == None or access_token == None:
            self.address, self.access_token = generate_address()
        else:
            self.address = address
            self.access_token = access_token

    def get_address(self) -> string:
        """Returns the mail address of the inbox"""
        return self.address

    def get_access_token(self) -> string:
        """Returns the access token of the inbox"""
        return self.access_token

    def get_all_mails(self) -> list[TempMail]:
        """Returns all the mails in inbox as TempMail object"""
        json_mails = fetch_mails(self.address, self.access_token)

        mails: list[TempMail] = []

        for json_mail in json_mails:
            temp_mail = TempMail()
            temp_mail.id = json_mail['id']
            temp_mail.subject = json_mail['subject']
            temp_mail.sender_address = json_mail['sender'].split('<')[1].replace('>', '')
            temp_mail.sender_name = json_mail['sender'].split('<')[0]
            temp_mail.content = json_mail['content']
            temp_mail.time_sent = json_mail['time']

            mails.append(temp_mail)
        return mails

    def get_latest_mail(self) -> TempMail:
        """Returns the latest mail in the inbox"""
        mails = self.get_all_mails()

        if len(mails) < 1:
            raise TempMailException('There are no mails in your inbox.')
        
        return mails[0]

    def get_mail_by_id(self, id: int) -> TempMail:
        """
        Returns mail by id

        Parameters
        ----------
        id : int
            The id of the mail

        Returns
        -------
        TempMail
            Object of TempMail
        
        Throws
        -------
        TempMailException if id was not found

    """
        mails = self.get_all_mails()

        for mail in mails:
            if mail.id == id:
                return mail
        raise TempMailException(f'The mail with id {id} was not found.')

    def extend(self, time: ExtendTime) -> None:
        force_extend_inbox(time, self.address, self.access_token)

        """
        Extends the duration of the inbox

        Specify the time of the extension

        Parameters
        ----------
        time : ExtendTime
            Time the inbox should extend

        Returns
        -------
        TempMailInbox
            Object of TempMailInbox
    """

    def get_timings(self) -> json:
        """Returns the creation and ending timestamps of the inbox"""
        return fetch_timings(self.address, self.access_token)
