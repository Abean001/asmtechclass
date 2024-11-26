# Python program to convert the currency
# of one country to that of another country

# Import the modules needed
import requests


class CurrencyConverter:
    """
    A class to convert currency using exchange rates from an API.
    """

    def __init__(self, url):
        """
        Initialize the CurrencyConverter with exchange rates from the API.

        Args:
        url (str): The API endpoint to fetch the rates.
        """
        self.rates = {}
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            data = response.json()
            # Ensure the response has the "rates" key
            if "rates" in data:
                self.rates = data["rates"]
            else:
                raise ValueError("Invalid API response: 'rates' not found.")
        except Exception as e:
            print(f"Error fetching data from API: {e}")
            raise

    def convert(self, from_currency, to_currency, amount):
        """
        Convert an amount from one currency to another.

        Args:
        from_currency (str): The currency code to convert from.
        to_currency (str): The currency code to convert to.
        amount (float): The amount to be converted.

        Returns:
        float: The converted amount.
        """
        if from_currency not in self.rates or to_currency not in self.rates:
            raise ValueError("Invalid currency code provided.")

        # Convert from the base currency (EUR) if necessary
        if from_currency != "EUR":
            amount = amount / self.rates[from_currency]

        # Convert to the target currency
        converted_amount = round(amount * self.rates[to_currency], 2)
        return converted_amount


if __name__ == "__main__":
    # Replace with your actual access key
    YOUR_ACCESS_KEY = "005b2513d72ebe28d6569f0b2707b45b"
    url = f"http://data.fixer.io/api/latest?access_key={YOUR_ACCESS_KEY}"

    try:
        converter = CurrencyConverter(url)
        print("Version: 0.1")
        print("Currency Code Examples:")
        print("Afghani = AFN")
        print("US Dollar = USD")
        print("Euro = EUR")
        print("Pound Scots = GBP")
        print("Yen = JPY")

        from_currency = input("From Currency (code): ").strip().upper()
        to_currency = input("To Currency (code): ").strip().upper()
        amount = float(input("Amount to convert: "))

        result = converter.convert(from_currency, to_currency, amount)
        print(f"{amount} {from_currency} = {result} {to_currency}")
    except Exception as e:
        print(f"An error occurred: {e}")

    print("Thank you for using our service!")
    print("Come again soon!")
