import requests
import unittest
from YaDisk import YAFolder



class TestYandexDiskAPI(unittest.TestCase):
    def setUp(self):
        self.uploader = YAFolder('xxxxxxxxx')  # подставить в параметр токен

    def test_create_folder(self):
        test_folder = 'test folder2'
        self.assertEqual(self.uploader.new_folder(test_folder).status_code, 201)
        folders_resp = requests.get("https://cloud-api.yandex.net/v1/disk/resources",
                                    params={"path": '/'},
                                    headers={"Authorization": f'OAuth {self.uploader.token}'})

        folders_list = [f['name'] for f in folders_resp.json().get('_embedded').get('items') if f['type'] == 'dir']
        self.assertIn(test_folder, folders_list)

    def test_create_folder_already_exist(self):
        test_folder = 'test folder2'
        self.assertEqual(self.uploader.new_folder(test_folder).status_code, 409)

        self.uploader.delete_folder(test_folder)
        folders_resp = requests.get("https://cloud-api.yandex.net/v1/disk/resources",
                                    params={"path": '/'},
                                    headers={"Authorization": f'OAuth {self.uploader.token}'})
        folders_list = [f['name'] for f in folders_resp.json().get('_embedded').get('items') if f['type'] == 'dir']
        self.assertNotIn(test_folder, folders_list)


    def tearDown(self):
        del self.uploader