import requests
email='angel@gmail.com'#email or username
password='angel'
response=requests.get(f'http://104.248.228.75:8080/login?email={email}&password={password}').text
print(response)
