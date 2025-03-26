def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    return price

original_price = float(input("Enter the original price ($): "))
discount_percent = float(input("Enter the discount (%): "))

final_price = calculate_discount(original_price, discount_percent)
print(f"Final Price: ${final_price:.2f}")
