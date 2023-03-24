import requests
import configparser

# Set up the API endpoint and access key
endpoint = 'https://openexchangerates.org/api/currencies.json'

config = configparser.ConfigParser()
config.read('config.ini')
access_key = config['openexchangerates']['app_id']

# Make a request to the API and get the response
response = requests.get(f'{endpoint}?app_id={access_key}')

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Get a list of country names and currencies
    countries = [f'{name} ({currency})' for currency, name in data.items()]
    # Print the list of countries and currencies
    print('\n'.join(countries))
else:
    # Print an error message if the request failed
    print(f'Error: {response.status_code}')
