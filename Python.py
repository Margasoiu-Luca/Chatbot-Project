import requests # Get and Post methods for api access
import openapi_client as Client # ? -------
import json # More control over JSON objects, unused for now
from openapi_client.rest import ApiException # In case of an exeption(error), this function detects it
configuration = Client.Configuration() # ? --------
header={
    "X-API-KEY":"77cc619e368bf68df41c416dc27f455e" # In the header we put the key that the api gives us
}


configuration.api_key['X-API-KEY'] = '77cc619e368bf68df41c416dc27f455e' # ? ---------
api_instance = Client.AdminApi(Client.ApiClient(configuration)) # ? -------
Sentence=input("Hello! My name is PyBot Chatbot! What is your name?") #
Words=Sentence.split() # Splitting
for i in range(len(Words)): #Check all the words for a first name
    if i==0: #First is skipped when not
        continue
    if Words[i][0].isupper(): #If the first letter is capital then it means it's a name
        try: #We try to fetch the data
            response = requests.request("GET", "https://v2.namsor.com/NamSorAPIv2/api2/json/gender/"+Words[i]+"/"+Words[i+1],headers=header)#Making the request to the api to get the data
            Data=response.json() # Transform the response into JSON object
            if(Data['likelyGender']=='male'): # Check for male or female, information which was sent in the response
                print("Nice to meet you "+Words[i]+"! How old are you man?")
            else:
                print("Nice to meet you "+Words[i]+"! How old are you girl?")
        except ApiException as e:
            print("An error occurred:"+e)
        break