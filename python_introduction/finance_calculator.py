monthly_income = int(input('Enter your monthly income: '))
monthly_expenses = int(input('Enter your total monthly expenses: '))
monthly_savings = income - expenses
Projected_Savings = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))
print(f'Your monthly savings are ${savings}.')
print(f'Projected savings after one year, with interest, is: ${Projected_Savings}.')
