import requests

# GET request
response = requests.get('http://127.0.0.1:5000/api/users')
print("GET response:", response.json())

# POST request
new_user = {"name": "Charlie"}
response = requests.post('http://127.0.0.1:5000/api/users', json=new_user)
print("POST response:", response.json())
