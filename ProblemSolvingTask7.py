"""
Author : G Gopi Kumar
Date : 16/10/2024

Program 1 : Using the URL https://restcountries.com/v3.1/all write a Python program which will do the
following :-

1.) Using the OOPS concept for the following task.
2.) Use the Class Constructor for taking input the above mentioned URL for the task.
3.) Create a Method that will Fetch all the JSON data from the URL mentioned above.
4.) Create a Method that will display the name of countries, currencies & currency symbols.
5.) Create a Method that will display all those countries which have DOLLAR as its currency.
6.) Create a Method that will display all those countries which have EURO as its currency.

"""
import requests

class CountryData:
    def __init__(self, url):
        self.url = url
        self.countries_data = []

    # Method to fetch all JSON data from the URL
    def fetch_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.countries_data = response.json()
            print("Data successfully fetched.")
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")

    # Method to display the name of countries, currencies, and currency symbols
    def display_countries_and_currencies(self):
        for country in self.countries_data:
            country_name = country.get('name', {}).get('common', 'N/A')
            currencies = country.get('currencies', {})
            for currency_code, currency_info in currencies.items():
                currency_name = currency_info.get('name', 'N/A')
                currency_symbol = currency_info.get('symbol', 'N/A')
                print(f"Country: {country_name}, Currency: {currency_name}, Symbol: {currency_symbol}")

    # Method to display countries that use DOLLAR as a currency
    def display_countries_using_dollar(self):
        print("\nCountries using DOLLAR:")
        for country in self.countries_data:
            currencies = country.get('currencies', {})
            for currency_code, currency_info in currencies.items():
                # Check if 'Dollar' appears in the currency name
                if 'dollar' in currency_info.get('name', '').lower():
                    country_name = country.get('name', {}).get('common', 'N/A')
                    print(f"Country: {country_name}, Currency: {currency_info.get('name')}")

    # Method to display countries that use EURO as a currency
    def display_countries_using_euro(self):
        print("\nCountries using EURO:")
        for country in self.countries_data:
            currencies = country.get('currencies', {})
            for currency_code, currency_info in currencies.items():
                if currency_info.get('name', '') == 'Euro':
                    country_name = country.get('name', {}).get('common', 'N/A')
                    print(f"Country: {country_name}, Currency: {currency_info.get('name')}")


# Create an instance of the CountryData class and fetch the data
url = 'https://restcountries.com/v3.1/all'
country_data = CountryData(url)
country_data.fetch_data()

# Display the name of countries, currencies, and currency symbols
country_data.display_countries_and_currencies()

# Display countries using DOLLAR as currency
country_data.display_countries_using_dollar()

# Display countries using EURO as currency
country_data.display_countries_using_euro()

"""
Author : G Gopi Kumar
Date : 16/10/2024

Program 2 : Visit the URL https://www.openbrewerydb.org/ write a Python script which will do the following :-

1.) List the names of all breweries present in the states of Alaska, Maine and New York.
2.) What is the count of breweries in each of the states mentioned above?
3.) Count the number of types of breweries present in individual cities of the state
mentioned above
4.) Count and list how many breweries have websites in the states of Alaska, Maine and
New York.

"""

import requests


class BreweryData:
    def __init__(self, url):
        self.url = url
        self.breweries_data = []

    # Method to fetch all JSON data from the API
    def fetch_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.breweries_data = response.json()
            print("Brewery data successfully fetched.")
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")

    # Method to list breweries in the specified states
    def list_breweries_in_states(self, states):
        print("\nBreweries in the specified states:")
        breweries_by_state = {}
        for brewery in self.breweries_data:
            state = brewery.get('state', '')
            if state in states:
                if state not in breweries_by_state:
                    breweries_by_state[state] = []
                breweries_by_state[state].append(brewery.get('name', 'N/A'))

        for state, breweries in breweries_by_state.items():
            print(f"\nState: {state}")
            for brewery in breweries:
                print(brewery)

    # Method to count breweries in each state
    def count_breweries_in_states(self, states):
        print("\nCount of breweries in each state:")
        brewery_count = {state: 0 for state in states}
        for brewery in self.breweries_data:
            state = brewery.get('state', '')
            if state in states:
                brewery_count[state] += 1

        for state, count in brewery_count.items():
            print(f"{state}: {count} breweries")

    # Method to count types of breweries in cities
    def count_brewery_types_by_city(self, state):
        print(f"\nBrewery types in cities of {state}:")
        city_brewery_types = {}
        for brewery in self.breweries_data:
            if brewery.get('state', '') == state:
                city = brewery.get('city', 'Unknown')
                brewery_type = brewery.get('brewery_type', 'Unknown')
                if city not in city_brewery_types:
                    city_brewery_types[city] = {}
                if brewery_type not in city_brewery_types[city]:
                    city_brewery_types[city][brewery_type] = 0
                city_brewery_types[city][brewery_type] += 1

        for city, types in city_brewery_types.items():
            print(f"\nCity: {city}")
            for brewery_type, count in types.items():
                print(f"{brewery_type}: {count}")

    # Method to list breweries with websites
    def list_breweries_with_websites(self, states):
        print("\nBreweries with websites:")
        brewery_with_websites = {}
        for brewery in self.breweries_data:
            state = brewery.get('state', '')
            if state in states and brewery.get('website_url'):
                if state not in brewery_with_websites:
                    brewery_with_websites[state] = []
                brewery_with_websites[state].append(brewery.get('name', 'N/A'))

        for state, breweries in brewery_with_websites.items():
            print(f"\nState: {state}")
            for brewery in breweries:
                print(brewery)


# Create an instance of the BreweryData class and fetch the data
brewery_url = 'https://api.openbrewerydb.org/breweries'
brewery_data = BreweryData(brewery_url)
brewery_data.fetch_data()

# List the breweries in Alaska, Maine, and New York
states = ['Alaska', 'Maine', 'New York']
brewery_data.list_breweries_in_states(states)

# Count breweries in Alaska, Maine, and New York
brewery_data.count_breweries_in_states(states)

# Count types of breweries in the cities of a state (e.g., New York)
brewery_data.count_brewery_types_by_city('New York')

# List breweries with websites in Alaska, Maine, and New York
brewery_data.list_breweries_with_websites(states)

