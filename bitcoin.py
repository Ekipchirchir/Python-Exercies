import sys
import requests

# Check if the user specified the number of Bitcoins to buy as a command-line argument
if len(sys.argv) != 2:
    sys.exit("Usage: python bitcoin.py <number of Bitcoins to buy>")

# Try to convert the argument to a float
try:
    num_bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Error: The number of Bitcoins to buy must be a valid float.")

# Query the API for the current price of Bitcoin in USD
url = "https://api.coindesk.com/v1/bpi/currentprice.json"
try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    price_usd = data["bpi"]["USD"]["rate_float"]
except requests.RequestException:
    sys.exit("Error: Failed to get current Bitcoin price from the API.")

# Calculate the cost of the specified number of Bitcoins in USD
cost_usd = num_bitcoins * price_usd

# Format the cost as a string with four decimal places and a thousands separator
cost_str = "{:,.4f}".format(cost_usd)

# Print the cost to the user
print("{:.4f} Bitcoins = ${}".format(num_bitcoins, cost_str))
