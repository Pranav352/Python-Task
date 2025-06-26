     
# Ask the user to input the purchase amount
amount = float(input("Enter the total purchase amount: "))

# Initialize discount rate
discount_rate = 0

# Determine discount based on the amount
if amount < 5000:
    discount_rate = 0  # No discount
elif 5000 <= amount < 10000:
    discount_rate = 0.05  # 5% discount
elif 10000 <= amount < 20000:
    discount_rate = 0.10  # 10% discount
elif 20000 <= amount < 50000:
    discount_rate = 0.15  # 15% discount
else:
    discount_rate = 0.20  # 20% discount for purchases >= 50000

# Calculate discount amount
discount_amount = amount * discount_rate

# Calculate final amount after applying the discount
final_price = amount - discount_amount

# Display results
print("Original Amount: ₹", amount)
print("Discount Percentage:", discount_rate * 100, "%")
print("Discount Amount: ₹", discount_amount)
print("Final Amount after Discount: ₹", final_price)
