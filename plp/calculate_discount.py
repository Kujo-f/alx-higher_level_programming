def calculate_price():
    price = int(input("Enter the original price of the item: "))
    discount_percent = int(input("Enter the discount percentage: "))

    if discount_percent >= 20:

        discount = ((discount_percent/100) * price)
        final_price = price - discount
        print("The final price is: ", str(final_price))
    else:
        print("The price is: ", str(price))



calculate_price()
