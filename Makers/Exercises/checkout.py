class SupermarketCheckout:
    def __init__(self):
        self.prices = {
            'A': 50,
            'B': 30,
            'C': 20,
            'D': 15
        }

        self.offers = {
            'A': (3, 130),
            'B': (2, 45)
        }

    def checkout(self, items):
        if not isinstance(items, str) or not items.isalpha() or not items.isupper():
            return -1

        item_count = {}
        for item in items:
            if item in self.prices:
                if item not in item_count:
                    item_count[item] = 0
                item_count[item] += 1
            else:
                return -1

        total = 0
        for item, count in item_count.items():
            if item in self.offers:
                offer_count, offer_price = self.offers[item]
                num_offers = count // offer_count
                num_non_offer = count % offer_count
                total += (num_offers * offer_price) + \
                    (num_non_offer * self.prices[item])
            else:
                total += count * self.prices[item]

        return total


shop = SupermarketCheckout()

print("shop.checkout('aBc'): ", shop.checkout('aBc'))  # => -1
print("shop.checkout('-B8x'): ", shop.checkout('-B8x'))  # => -1
print("shop.checkout(18): ", shop.checkout(18))  # => -1
print("shop.checkout('AA'): ", shop.checkout('AA'))  # => 100
print("shop.checkout('ABCD'): ", shop.checkout('ABCD'))  # => 115
print("shop.checkout('AAA'): ", shop.checkout('AAA'))  # => 130
print("shop.checkout('AAAAAA'): ", shop.checkout('AAAAAA'))  # => 260
