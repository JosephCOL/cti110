#Meal Tip Tax Calculator
#6/19/22
#CTI-110 P2HW1 - Meal Tip Tax Calculator
#Joseph Coleman

food_charge = float(input('Enter Food Cost:'))

tip_charge = float(input('Enter Tip Percentage:'))
tip_percentage = tip_charge/100
tip_total = food_charge * tip_percentage
tax_charge = float(input('Enter Tax Percentage:'))
tax_percentage = tax_charge/100
tax_total = food_charge * tax_percentage
food_total = food_charge + tip_total + tax_total
print(f'Calculated Tip Percentage:',f'{tip_total:.2f}')
print(f'Calculated Tax:', f'{tax_total:.2f}')

print(f'Total cost including tip and tax', f'{food_total:.2f}')