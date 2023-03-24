This project requires a **config.ini** file which contains the API Key of openexchangerates API:

The file should follow this structure:

    [openexchangerates]
    app_id = api_key

To run the program just execute:

    py main.py

This program uses the countries and codes found in openexchangerates API https://openexchangerates.org/. You can check the values of countries names and currencies running the program:

    py country_currency.py