#Meal Tip Tax Calculator
#6/19/22
#CTI-110 P2HW1 - Meal Tip Tax Calculator
#Joseph Coleman

food_charge = float(input('Enter Food Cost:'))
tip_charge = int(input('Enter Tip Percentage:'))
tip_percentage = tip_charge/100

tax_charge = food_charge * (6/100)


if tip_percentage == .15:
    tip_total = (food_charge * tip_percentage)
    true_total = food_charge + tip_total + tax_charge
    print(f'Your total is:{true_total:.2f}')
    print(f'Tax:{tax_charge:.2f}')
    print(f'Tip:{tip_total:.2f}')
elif tip_percentage == .18:
    tip_total = (food_charge * tip_percentage)
    true_total = food_charge + tip_total + tax_charge
    print(f'Your total is:{true_total:.2f}')
    print(f'Tax:{tax_charge:.2f}')
    print(f'Tip:{tip_total:.2f}')
elif tip_percentage == .20:
    tip_total = (food_charge * tip_percentage)
    true_total = food_charge + tip_total + tax_charge
    print(f'Your total is:{true_total:.2f}')
    print(f'Tax:{tax_charge:.2f}')
    print(f'Tip:{tip_total:.2f}')
else:
    print('Error: Invalid Input')



