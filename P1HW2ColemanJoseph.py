#
#June 12th,2022
#CTI-110 P1HW2 - Basic Math
#Joseph Coleman

ExpenseName = str(input('Name of Expense'))

ExpenseCost = float(input('Cost of Expense'))

MonthlyTotal = ExpenseCost * (6/100)
MonthlyCharge = MonthlyTotal+ExpenseCost
YearlyTotal = MonthlyTotal*12+MonthlyCharge
print('The monthly tax on your item', ExpenseName, 'is', MonthlyTotal)
print('Meaning, your monthly total equals', MonthlyCharge)
print('All together your annual charge would be', YearlyTotal)
