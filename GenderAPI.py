import requests
class GenderAPI:

    def __init__(self, name):
        '''
        Creats an instance variable and stores it as the api url, also allows the url to be updated when name changes
        '''
        self.name = name
        self.url = f'https://api.genderize.io?name={self.name}'

    def get(self, name = " "):
        '''
        Pulls the data from the API and returns it
        '''

        r = requests.get(self.url)

        new_response = r.json()
        return new_response
 