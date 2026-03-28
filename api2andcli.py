import requests
import sys
if len(sys.argv) > 1:
    category = sys.argv[1]
    url = f'http://official-joke-api.api.appspot.com/jokes/{category}/random'
else:
    url = 'http://official-joke-api.appspot.com/random_joke'
response = requests.get(url)
data = response.json()
if isinstance(data,list):
    data = data[0]
print(data['setup'])
print(data['punchline'])



