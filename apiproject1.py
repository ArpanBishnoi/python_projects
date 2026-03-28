import requests
response = requests.get('http://wttr.in/Delhi?format=j1')
data = response.json()
print(data['current_condition'][0]['temp_C'])