# Variables and calculations practice

print("=== Financial Calculator ===")
print()

# Investment scenario
initial_investment = 1000
annual_return = 0.10  # 10%
years = 8  # Until I'm 26

print(f"If I invest €{initial_investment} today at {annual_return*100}% annually")
print(f"For {years} years (until I start my quant job)")
print()

# Calculate year by year
current_value = initial_investment
for year in range(1, years + 1):
    current_value = current_value * (1 + annual_return)
    print(f"Year {year}: €{current_value:.2f}")

print()
print(f"Final value: €{current_value:.2f}")
print(f"Profit: €{current_value - initial_investment:.2f}")
print()

# Career calculations
starting_salary = 120000  # pounds
london_tax_rate = 0.42
net_salary = starting_salary * (1 - london_tax_rate)
monthly_net = net_salary / 12

print("=== Career Projections ===")
print(f"Starting salary: £{starting_salary:,}")
print(f"After tax ({london_tax_rate*100}%): £{net_salary:,.0f}")
print(f"Monthly take-home: £{monthly_net:,.0f}")
print()

# If I save 50%
monthly_savings = monthly_net * 0.5
yearly_savings = monthly_savings * 12

print(f"If I save 50% of net income:")
print(f"Monthly savings: £{monthly_savings:,.0f}")
print(f"Yearly savings: £{yearly_savings:,.0f}")
print()

# After 3 years in London
years_working = 3
total_saved = yearly_savings * years_working

print(f"After {years_working} years of saving:")
print(f"Total saved: £{total_saved:,.0f}")
print()
print("This is why I'm doing this.")
