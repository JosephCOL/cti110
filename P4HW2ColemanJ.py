#CTI-110
#P4HW2 - EXPENSES
#Joseph Coleman
#7/3/2022
start_amount = int(input('Enter starting amount in account: $'))
user_char = 'y'
expense_count = 0
expense_amount = 0
while user_char == 'y':
    expense_count = expense_count + 1
    expense_amount = int(input(f'Enter expense {expense_count}:')) + expense_amount
    user_char = input('Do you want to enter another expense? (y/n)')
total_expense = start_amount - expense_amount   

print(f'Amount in account before expenses subtracted: ${start_amount:.1f}')
print(f'Number of expenses entered: {expense_count}')
print(f'Amount in account after expenses subtracted is: ${total_expense:.1f}')