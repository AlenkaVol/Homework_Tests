import os
import requests
from dotenv import load_dotenv

load_dotenv()

name_folder = 'test_folder'

#функция для создания папки на Яндекс диске
def folder_creation_ydisk(name_folder):
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    params = {"path": name_folder}
    headers = {"Authorization": "OAuth " + os.getenv('tokenYandex')}
    response = requests.put(url, headers=headers, params=params)
    return response.status_code


# print(folder_creation_ydisk(name_folder))


def get_info_file_ydisk(path_to_file):
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    params = {"path": path_to_file}
    headers = {"Authorization": "OAuth " + os.getenv('tokenYandex')}
    response = requests.get(url, headers=headers, params=params)
    return response.status_code

# print(get_info_file_ydisk(name_folder))

