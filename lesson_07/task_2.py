# Create a function which takes as input two dicts with structure mentioned below,
# then computes and returns the total price of stock.

stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}
prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}


def calculate_price(stock_: dict, prices_: dict) -> float:
    """Return the total price of the stock"""
    total_price = 0
    for value_stock, value_price in zip(stock_.values(), prices_.values()):
        total_price += value_stock * value_price
    return round(total_price, 2)

total = calculate_price(stock, prices)
print(f'The total price of the stock is ${total:.2f}')