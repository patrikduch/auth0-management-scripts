import requests

#audience = 'your_audience'
#clientId = 'your_client_id'
#clientSecret = 'your_client_secret'

domain = 'your_audience.us.auth0.com'
audience = f'https://{domain}/api/v2/'
clientId = 'your_client_id'
clientSecret = 'your_client_secret'


# Define the URL for the API request
url = f"https://{domain}/oauth/token"

# Define the payload for the API request
payload = {
    'grant_type': 'client_credentials',
    'client_id': clientId,
    'client_secret': clientSecret,
    'audience': audience
}

# Make the POST request
response = requests.post(url, json=payload)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response as JSON and print the access token
    data = response.json()
    access_token = data['access_token']
    print(access_token)
else:
    print(f"Failed to obtain access token: {response.content}")
