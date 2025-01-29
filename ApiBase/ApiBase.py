import requests


class ApiBase:
    def __init__(self, base_url):
        #base_url  The base URL for the API.
        #default_headers  The default headers to be used for all requests.
        self.base_url = base_url
        self.default_headers = {
            "accept": "application/json",
            "Content-Type": "application/json"
        }
    #get method
    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        headers = self.default_headers
        response = requests.get(url, headers=headers, params=params)
        return response

    # post method
    def post(self, endpoint, data, headers=None):
        url = f"{self.base_url}{endpoint}"
        headers = headers or self.default_headers
        response = requests.post(url, json=data, headers=headers)
        return response
    #put method
    def put(self, endpoint, data):
        url = f"{self.base_url}{endpoint}"
        headers = self.default_headers
        response = requests.put(url, json=data, headers=headers)
        return response
    #delete method
    def delete(self, endpoint,  headers=None):
        url = f"{self.base_url}{endpoint}"
        headers = headers or self.default_headers
        response = requests.delete(url, headers=headers)
        return response

