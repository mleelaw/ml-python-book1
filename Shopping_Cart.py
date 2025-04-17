shopping_cart_items = []


def average_price(cart_items):
    try:
        average = 0

        for item in cart_items:
            average += item.price

        average = average / len(cart_items)

        return average
    except ZeroDivisionError:
        return 0


average_price_of_cart_items = average_price(shopping_cart_items)
print(f"Your average cart item price is {average_price_of_cart_items} dollars")
