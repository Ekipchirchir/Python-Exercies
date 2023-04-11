def get_coin_value(coin):
    if coin == "50" or coin == "25" or coin == "0":
        return coin
    else:
        return 0 # a zero to indicate an ivalid coin

# Initialize the total amount to 0
total_amount = 0
while total_amount < 50:
    # Prompt the user to insert a coin and convert the input to an integer
    coin = input("Insert a coin (in cents): ")
    coin_value = get_coin_value(int(coin))
    if coin_value > 0:
        total_amount += coin_value
        print("Amount due:", 50 - total_amount, "cents")
    else:
        print("Invalid coin. Please insert a 25, 10, or 5 cent coin.")

change = total_amount - 50
print("Change due:", change, "cents")

    
