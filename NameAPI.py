import requests
class NameAPI:

    def __init__(self):
        '''
        Creats an instance variable and stores it as the api url,
        '''
        self.url = f'http://names.drycodes.com/1?nameOptions=boy_names'

    def get(self):
        '''
        Pulls the data from the API and returns it, also seperatres the name and only returns the first name
        '''

      
        r = requests.get(self.url)

        response = r.json()
        name = response[0]
        first_name = name.split("_")
      
        return first_name[0]
