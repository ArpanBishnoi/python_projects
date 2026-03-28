import requests
response = requests.get('http://official-joke-api.appspot.com/random_joke')
data = response.json()
print(data['setup'])
print(data['punchline'])