import pandas as pd
import matplotlib.pyplot as plt

# Defining the tiers with upper bounds and unit prices
tiers = [
    (100, 133),
    (500, 35),
    (1000, 30),
    (5000, 25),
    (10000, 10),
    (20000, 3),
    (float('inf'), 2)
]

# Function to calculate total price based on blended pricing
def calculate_total_price(units, tiers):
    total_price = 0
    remaining_units = units
    previous_upper_bound = 0
    
    for upper_bound, price_per_unit in tiers:
        if remaining_units > 0:
            units_in_tier = min(upper_bound - previous_upper_bound, remaining_units)
            total_price += units_in_tier * price_per_unit
            remaining_units -= units_in_tier
            previous_upper_bound = upper_bound
        else:
            break
    
    return f"{total_price:,.2f}"

# Initialize example units and calculate total price
example_units = [50, 100, 101, 450, 500, 501, 551, 1000, 1001, 1500, 2500, 4500, 5000, 5500, 7500, 9000, 9500, 10000, 12500, 15000, 17500, 20000, 20500, 22000, 24000, 30000]
example_prices = [calculate_total_price(units, tiers) for units in example_units]
print(example_prices)

# Create DataFrame for display
df_blended = pd.DataFrame({
    "Units": example_units,
    "Total Price (SEK)": example_prices
})
print(f"\n{df_blended.to_string(index=False)}")

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(df_blended["Units"], df_blended["Total Price (SEK)"], marker='o')
plt.title("Blended Pricing: Total Price vs Units")
plt.xlabel("Units")
plt.ylabel("Total Price (SEK)")
plt.grid(True)
plt.show()

