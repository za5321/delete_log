import json


class Config:
    def __init__(self):
        with open('Config\\config.json', 'r', encoding='UTF-8') as file:
            self.conf = json.load(file)

    def get_config(self, flag: str):
        return self.conf[flag]
