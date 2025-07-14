
# finance_calculator.py

# Get inputs
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

# Monthly and annual savings
monthly_savings = income - expenses
annual_savings = monthly_savings * 12
interest = annual_savings * 0.05
projected_savings = annual_savings + interest

# Output
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
