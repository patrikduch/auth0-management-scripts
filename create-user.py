import requests
import json

# Set your Auth0 domain and token
domain = 'your_domain.us.auth0.com'
token = 'your-valid-token'

# Set the user's information
user_info = {
    'email': 'patrik.duch@supermail.com',
    'password': 'superman-patrik-duch',
    'connection': 'Username-Password-Authentication',  # Change this to your connection name
}

# Convert the user information to JSON
user_info_json = json.dumps(user_info)

# Create the header for the request
headers = {
    'Authorization': f'Bearer {token}',
    'content-type': 'application/json'
}

# Send the POST request to the Auth0 API
response = requests.post(f'https://{domain}/api/v2/users', headers=headers, data=user_info_json)

# Check the response
if response.status_code == 201:
    print('User created successfully.')
else:
    print('Failed to create user. Status code:', response.status_code)
    print('Response:', response.json())
