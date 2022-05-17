import os
from datetime import datetime, timedelta
from Config.config import Config


class delete_log:
    def __init__(self):
        self.path = self.get_path()
        self.sdate = datetime.now() - timedelta(days=self.get_day())

    @staticmethod
    def get_path():
        return Config().get_config("path")

    @staticmethod
    def get_day():
        return Config().get_config("day")

    def delete_log(self):
        os.chdir(self.path)

        for file in next(os.walk(self.path))[2]:
            if self.sdate > datetime.fromtimestamp(os.path.getmtime(file)):
                try:
                    os.remove(file)
                except FileNotFoundError:
                    continue


if __name__ == '__main__':
    delete_log().delete_log()
