import requests

audience = 'https://dev-cig7twm3fz4rokuh.us.auth0.com/api/v2/'
clientId = 'jSoY9dCrCTTPzllv1Ure3sS93C7dOPvw'
clientSecret = 'lI__jqrgSPzgVKeS3g2-hRHoqyZ2qCk_wi_829lEMSCcRoo4uXGuhAhIde0uXIYI'

# Define the URL for the API request
url = 'https://dev-cig7twm3fz4rokuh.us.auth0.com/oauth/token'

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
