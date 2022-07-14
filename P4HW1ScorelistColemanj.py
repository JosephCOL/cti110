#CTI-110
#P4HW1 - Score List
#Joseph Coleman
#7/14/22
#

numbers = []

print("Enter 10 numbers: ")

for i in range(10):

    num = int(input("Enter number " + str(i + 1) + ": "))
    
    numbers.append(num)

largest = numbers[0]

second_largest = None 

for i in range(1, 10):
    if numbers[i] >= largest:
    
        second_largest = largest
        
        largest = numbers[i]
        
    elif second_largest == None or second_largest < numbers[i]:
        second_largest = numbers[i]
print("Largest number: ", largest)
print("Second Largest number: ", second_largest)