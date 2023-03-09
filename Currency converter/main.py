import requests
import configparser
import pycountry


def get_countries_codes():
    # Ask the user for the currency code
    # base_country_name = input('Enter a country name: ')
    base_country_name = input('Enter the base country name: ')
    destiny_country_name = input('Enter the country name to convert: ')

    ###
    # countries = list(pycountry.countries)
    # country_names = [country.name for country in countries]
    # print(country_names)

    # Look up the currency code using the country name
    try:
        base_country = pycountry.countries.get(name=base_country_name)
        destiny_country = pycountry.countries.get(name=destiny_country_name)

        return (pycountry.currencies.get(numeric=base_country.numeric).alpha_3,
                pycountry.currencies.get(numeric=destiny_country.numeric).alpha_3)
    except:
        print(
            f'Could not find a country that uses {base_country_name} or {destiny_country_name}')


def read_api_Key():
    # Read the app ID from config.ini
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openexchangerates']['app_id']


def get_rates(app_id, currencies):
    # Set up the API endpoint URL and parameters
    url = 'https://openexchangerates.org/api/latest.json'
    params = {'app_id': app_id, 'base': currencies[0]}

    # Make the API call using the Requests library
    response = requests.get(url, params=params)

    # Check the response status code
    if response.status_code == 200:
        # Get the exchange rate data from the response JSON
        exchange_rates = response.json()['rates']
        return exchange_rates
    else:
        print('Error: Unable to retrieve exchange rates.')


def get_currencies_rate(currencies_codes, data):
    # Filter the data by currency_code to get the rate
    if currencies_codes[1] in data:
        return data[currencies_codes[1]]
    else:
        print(f'Could not find a rate for {currencies_codes[1]}')


def calculate_amount_to_convert(rate):
    # Ask the user for the amount to convert
    amount = input('Enter the amount to covert: ')

    # return the amount and the convert amount into destiny country currency
    return amount, float(rate)*float(amount)


if __name__ == "__main__":
    try:
        app_id = read_api_Key()
        currencies_codes = get_countries_codes()
        data = get_rates(app_id, currencies_codes)
        rate = get_currencies_rate(currencies_codes, data)
        final_quantity = calculate_amount_to_convert(rate)
        print(
            f'Exchange rate for {currencies_codes[0]} to {currencies_codes[1]} is {rate}')
        print(
            f'{final_quantity[0]}{currencies_codes[0]} in {currencies_codes[1]} are {final_quantity[1]}')
    except:
        print(
            f'There was an error getting the information. Please check the names of the countries.')
