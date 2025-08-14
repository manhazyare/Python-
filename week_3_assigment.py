

def calculate_discount(price, discount_percent):
    # calculate the final price after applying a discount if it is 20% or higher
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# User input (OUTSIDE the function)
price = float(input("Enter the price of the product: "))
discount_percent = float(input("Enter discount percentage: "))

# Calculate the final price
final_price = calculate_discount(price, discount_percent)

# The result
if discount_percent >= 20:
    print(f"Final price after the discount: {final_price:.2f}")
else:
    print(f"No discount applied. Final price: {final_price:.2f}")