req_service = str(input('Enter desired auto service:\n'))

oil_change = 'Oil change'
tire_rotation = 'Tire rotation'
car_wash ='Car wash'

if req_service == oil_change:
    print('You entered: Oil change')
    print('Cost of oil change: $35')
elif req_service == tire_rotation:
    print('You entered: Tire rotation')
    print('Cost of tire rotation: $19')
elif req_service == car_wash:
    print('You entered: Car wash')
    print('Cost of car wash: $7')
else:
    print('You entered:', req_service)
    print('Error: Requested service is not recognized')