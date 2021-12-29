import requests


class YAFolder:
    def __init__(self, token):
        self.token = token

    def new_folder(self, folder_name):
        HEADERS = {"Authorization": f'OAuth {self.token}'}
        URL = "https://cloud-api.yandex.net/v1/disk/resources"
        res = requests.put(URL, params={"path": '/' + folder_name}, headers=HEADERS)
        return res

    def delete_folder(self, folder_name):
        HEADERS = {"Authorization": f'OAuth {self.token}'}
        URL = "https://cloud-api.yandex.net/v1/disk/resources"
        res = requests.delete(URL, params={"path": '/' + folder_name}, headers=HEADERS)
        return res