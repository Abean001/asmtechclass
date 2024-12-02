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
        except requests.exceptions.RequestException as e:
            print("⚠️ Network error: Unable to fetch data. Please check your internet connection.")
            raise
        except ValueError as e:
            print(f"⚠️ Data error: {e}")
            raise
        except Exception as e:
            print(f"⚠️ Unexpected error occurred: {e}")
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
        if from_currency not in self.rates:
            raise ValueError(f"Currency '{from_currency}' is not supported.")
        if to_currency not in self.rates:
            raise ValueError(f"Currency '{to_currency}' is not supported.")
        if amount < 0:
            raise ValueError("Amount must be a positive number.")

        # Convert from the base currency (EUR) if necessary
        if from_currency != "EUR":
            amount = amount / self.rates[from_currency]

        # Convert to the target currency
        converted_amount = round(amount * self.rates[to_currency], 2)
        return converted_amount


def main():
    """
    Main function to handle user interaction and conversions.
    """
    YOUR_ACCESS_KEY = "005b2513d72ebe28d6569f0b2707b45b"
    url = f"http://data.fixer.io/api/latest?access_key={YOUR_ACCESS_KEY}"

    print("\nWelcome to Value_Convert!")
    print("This tool converts amounts from one currency to another.")

    while True:
        try:
            # Initialize the converter
            converter = CurrencyConverter(url)

            # Get the amount to convert
            while True:
                try:
                    amount = float(input("\nEnter the amount to convert: "))
                    if amount < 0:
                        print("⚠️ Amount must be positive. Please try again.")
                    else:
                        break
                except ValueError:
                    print("⚠️ Please enter a valid number.")

            # Get the source currency
            from_currency = input("Enter the currency code you are converting from (e.g., EUR): ").upper()
            # Get the target currency
            to_currency = input("Enter the currency code you are converting to (e.g., USD): ").upper()

            # Perform the conversion
            try:
                converted_amount = converter.convert(from_currency, to_currency, amount)
                print(f"\n✅ {amount} {from_currency} is approximately {converted_amount} {to_currency}.")
            except ValueError as ve:
                print(f"⚠️ Conversion error: {ve}")

            # Ask if the user wants to perform another conversion
            another = input("\nWould you like to make another conversion? (yes/no): ").strip().lower()
            if another != 'yes':
                print("Thank you for using Value_Convert! Goodbye!")
                break

        except Exception as e:
            print(f"⚠️ An unexpected error occurred: {e}")
            break


if __name__ == "__main__":
    main()
