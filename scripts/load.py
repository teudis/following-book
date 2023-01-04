import requests


value = 'health'
apikey = 'AIzaSyD_mV_JDpR_EmXEEjnfceEt6-Xxflg-rV4'
params = {'q': value, 'key': apikey}
URL_API = f"https://www.googleapis.com/books/v1/volumes?q={value}&key={apikey}&=max-results=5"
response = requests.get(URL_API)
bookapi = response.json()
print(bookapi)

parms = {"q":value, 'key':apikey}
r = requests.get(url="https://www.googleapis.com/books/v1/volumes", params=parms)
print (r.url)