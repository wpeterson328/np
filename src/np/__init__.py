import requests
import yaml
from pprint import pprint as pp
import json

class Creds():
    def __init__(self,creds_file="creds.yml"):
        self.creds_file = creds_file
        self.load()

    def load(self):
        with open(self.creds_file) as creds_fd:
            creds = yaml.load(creds_fd, Loader=yaml.FullLoader)
        self.alias = creds["alias"]
        self.password = creds["password"]
        self.auth = creds["auth"]


    def _build_dict(self):
        return dict(
            alias=self.alias,
            password=self.password,
            auth=self.auth
        )


    def dump(self):
        with open(self.creds_file, 'w') as outfile:
            yaml.dump(self._build_dict(), outfile)


    def __repr__(self):
        return str(self._build_dict())


class NeptuneAPI():
    def __init__(self, creds, domain="np.ironhelmet.com"):
        self.domain = domain
        self.creds = creds

    def login(self):
        path = "/arequest/login"
        url = "https://{0}{1}".format(self.domain, path)

        payload = {
            "type": "login",
            "alias": self.creds.alias,
            "password": self.creds.password 
        }

        r = requests.post(url, data=payload)
        self.creds.auth = r.cookies["auth"]

    def order(self):
        path = "/trequest/order"
        url = "https://{0}{1}".format(self.domain, path)

        payload = dict(
            type="order",
            order="full_universe_report",
            version="",
            game_number="4848663437508608"
        )

        cookies = {'enwiki_session': '17ab96bd8ffbe8ca58a78657a918558'}
        cookies = dict(
            auth=self.creds.auth
        )

        r = requests.post(url, data=payload, cookies=cookies)
        return r.text


def main():
    creds = Creds()
    api = NeptuneAPI(creds)
    api.login()
    print api.order()
