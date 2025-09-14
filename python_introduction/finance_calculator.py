#!/usr/bin/env python3

# Prompt user for monthly income and expenses
monthly_income = float(input('Enter your monthly income: '))
monthly_expenses = float(input('Enter your total monthly expenses: '))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Calculate projected annual savings with 5% interest
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Print results
print('Your monthly savings are ${}.'.format(int(monthly_savings)))
print('Projected savings after one year, with interest, is: ${}.'.format(int(projected_savings)))

