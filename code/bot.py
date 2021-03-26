import requests
import json
import configparser as cfg

class Communist_bot():
    def __init__(self):
        self.token = self.read_token_from_config_file()
        self.base = "https://api.telegram.org/bot{}/".format(self.token)
        super().__init__()
    
    def get_updates(self,offset = None):
        base = "https://api.telegram.org/bot1723313591:AAFEqRwLck1K_xN-lrrx8j5UhQdwPeeE4Ic"
        url = base + "/getUpdates?timeout=1"
        if offset:
            url = url + "&offset={}".format(offset)
        response = requests.get(url)
        return json.loads(response.content)
    
    def send_message(self,msg,chat_id):
        url = self.base + "sendMessage?text={}&chat_id={}".format(msg,chat_id)
        if msg is not None:
            requests.get(url)
        
    def read_token_from_config_file(self):
        parser = cfg.ConfigParser()
        parser.read("config.cfg")
        return parser.get('creds','token')



