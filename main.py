import GenderAPI
import NameAPI

def main():
  '''
  Creates objects of the APIs and uses the result of the name API to generate the gender API and provide facts about the name
  '''

  name_obj = NameAPI.NameAPI()
  name_result = name_obj.get()

  gender_obj = GenderAPI.GenderAPI(name_result)
  gender_result = gender_obj.get()
  
  print(gender_result)
  
main()