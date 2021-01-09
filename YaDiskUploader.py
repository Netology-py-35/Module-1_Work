import requests


class YaUploader:
    def __init__(self, token: str):
        self.url_requests = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        self.token = token
        self.headers = {"Authorization": f"OAuth {self.token}"}

    def get_upload_url(self, name:str):
        resp = requests.get(self.url_requests, headers=self.headers, params={
            'path': f'/{name}',
            'overwrite': 'true'
        })
        print(resp)
        resp.raise_for_status()
        return resp.json()['href']

    def upload_from_url(self, url, file_url):
        resp = requests.post(url, files={'url': file_url})
        resp.raise_for_status()
        return resp
