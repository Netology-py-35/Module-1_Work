import os
from dotenv import load_dotenv  # for python-dotenv method
from VkDownloader import VK
from YaDiskUploader import YaUploader

load_dotenv()

vk_access_token = os.environ.get('vk_access_token')
vk_api_version = os.environ.get('vk_api_version')
yandex_disk_token = os.environ.get('yandex_disk_token')


def get_url_photo():
    photo_url = []
    for photo in vk.get_photos()['response']['items']:
        size = photo['sizes'][-1:][0]['url']
        photo_url.append(size)
    return photo_url


def upload_to_yadisk(file_name, file_url):
    # upload_url = uploader.get_upload_url(file_name)
    # print(upload_url)
    result = uploader.upload_from_url(file_name, file_url)
    return result


if __name__ == '__main__':
    vk = VK(vk_access_token, vk_api_version)
    uploader = YaUploader(yandex_disk_token)
    print(get_url_photo())
    n = 0
    for photo_url in get_url_photo():
        print(upload_to_yadisk(f'demo{n}.png', photo_url))
        n += 1
