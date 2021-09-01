# Product Store

# Write a class Product that has three attributes:
# * type
# * name
# * price

# Then create a class ProductStore, which will have some Products and will operate with all products in the store. 
# All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.

# Tips: Use aggregation/composition concepts while implementing the ProductStore class. 
# You can also implement additional classes to operate on a certain type of product, etc.

# Also, the ProductStore class must have the following methods:

# * add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your store(30 percent)
# * set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by input identifiers (type or name). 
# The discount must be specified in percentage
# * sell_product(product_name, amount) - removes a particular amount of products from the store if available, in other case raises an error. 
# It also increments income if the sell_product method succeeds.
# * get_income() - returns amount of many earned by ProductStore instance.
# * get_all_products() - returns information about all available products in the store.
# * get_product_info(product_name) - returns a tuple with product name and amount of items in the store.


class Product:

    def __init__(self, type_: str, name: str, price: float) -> None:
        self.type_ = type_
        self.name = name
        self.price = price
    
    def __repr__(self) -> str:
        return self.name

    def info(self) -> str:
        """Returns info by listing object atributes"""
        return f'Name: {self.name}, type: {self.type_}, price: {self.price}'
    

class ProductsStore:

    def __init__(self) -> None:
        self.shelf = {}
        self.income: float = 0

    def add(self, other: object, amount: int) -> None:
        """Adds a specified quantity of a single product with a predefined price premium for your store(30 percent)"""
        other.price = other.price + other.price * 0.3
        self.shelf.update({other: amount})
        print(f'{amount} {other.name}-s have been added to the Store')

    def set_discount(self, identifier: str, percent: int, identifier_type='name'):
        """Sets a discount on the particular product or type of products"""
        if identifier_type == 'type':
            for product in self.shelf.keys():
                if product.type_ == identifier:
                    product.price = product.price - product.price * (percent / 100)
        else:
            product = [product_ for product_ in list(self.shelf.keys()) if product_.name == identifier][0]
            product.price = product.price - product.price * (percent / 100)

    def sell_product(self, product_name: object, amount: int) -> None:
        """Removes a particular amount of products from the store if available, in other case raises an error.
        It also increments income if the sell_product method succeeds."""
        if amount > self.shelf.get(product_name):
            print(f'Not enough {product_name} in the store')
        else:
            self.shelf[product_name] -= amount
            self.income += product_name.price * amount
            print(f'Operation successfull: {amount} {product_name} for {round(product_name.price * amount, 2)}')

    def get_income(self) -> str:
        """Returns amount of many earned by ProductStore instance."""
        return f'The income is {round(self.income, 2)}'

    def get_all_products(self) -> list:
        """Returns information about all available products in the store."""
        available_products = [product.name for product in self.shelf.keys() if self.shelf.get(product) > 0]
        return available_products

    def get_product_info(self, product_name: object) -> tuple:
        """Returns a tuple with product name and amount of items in the store."""
        product_amount = self.shelf.get(product_name)
        return product_name, product_amount


if __name__ == '__main__':
    
    # Products
    potato = Product('vegetable', 'potato', 10)
    tomato = Product('vegetable', 'tomato', 30)
    onion = Product('vegetable', 'onion', 30)

    strawberry = Product('berry', 'strawberry', 50)
    blackberry = Product('berry', 'blackberry', 70)
    blueberry = Product('berry', 'blueberry', 80)

    apple = Product('fruit', 'apple', 15)
    peach = Product('fruit', 'peach', 30)
    pear = Product('fruit', 'pear', 15)

    # Store
    store = ProductsStore() # initialize store
    store.add(potato, 20) # -> 20 potato-s have been added to the Store
    store.add(onion, 10) # -> 10 onion-s have been added to the Store
    store.add(apple, 20) # -> 20 apple-s have been added to the Store
    print(store.get_all_products()) # -> ['potato', 'onion', 'apple']
    print(store.get_income()) # -> 'The income is 0'
    store.sell_product(potato, 10) # -> Operation successfull: 10 potato for 130.0
    store.set_discount('potato', 50)
    store.sell_product(potato, 10) # -> Operation successfull: 10 potato for 65.0
    print(store.get_income()) # -> The income is 195.0
    print(store.get_product_info(potato)) # -> (potato, 0)
    store.sell_product(apple, 10) # -> Operation successfull: 10 apple for 195.0
    store.set_discount('fruit', 40, 'type')
    store.sell_product(apple, 10) # -> Operation successfull: 10 apple for 117.0
    print(store.get_income()) # -> The income is 507.0