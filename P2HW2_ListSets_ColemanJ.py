#CTI-110
#P2HW2 - List and Sets
#Joseph Coleman
#6/19/22

num1 = int(input('Enter First Integer: '))
num2 = int(input('Enter Second Integer: '))
num3 = int(input('Enter Third Integer: '))
num4 = int(input('Enter Fourth Integer: '))
num5 = int(input('Enter Fifth Integer: '))
num6 = int(input('Enter Sixth Integer: '))

list_sum = [num1, num2, num3, num4, num5, num6]

smallest_number = min(list_sum)
biggest_number = max(list_sum)
sum_number = sum(list_sum)
avg_number = sum(list_sum)/6

print('Created List:', list_sum)
print('Smallest number in list', smallest_number)
print('Biggest number in list', biggest_number)
print('Sum of Numbers in List', sum_number)
print(f'Average of Numbers in List',f'{avg_number:.2}')
list_set = set(list_sum)
print(list_set)