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
    # Replace YOUR_ACCESS_KEY with your Fixer.io access key
    YOUR_ACCESS_KEY = "005b2513d72ebe28d6569f0b2707b45b"
    url = f"http://data.fixer.io/api/latest?access_key={YOUR_ACCESS_KEY}"

    try:
        converter = CurrencyConverter(url)

        print("Welcome to Value_Convert!")
        print("This tool converts Euros (EUR) into other currencies.")

        amount_in_euros = float(input("Enter the amount in Euros (EUR): "))

        # Define the target currencies
        target_currencies = ["USD", "GBP", "JPY", "AUD", "CAD"]

        print(f"\nConverting {amount_in_euros} EUR into:")
        for currency in target_currencies:
            try:
                converted_amount = converter.convert("EUR", currency, amount_in_euros)
                print(f"  {currency}: {converted_amount}")
            except ValueError as ve:
                print(f"  {currency}: Conversion error ({ve})")

    except Exception as e:
        print(f"An error occurred: {e}")

    print("\nThank you for using Value_Convert!")
