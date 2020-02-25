
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

cars = ['bmw','audi','toyota','subaru']
print('Here is the original list:')
print(cars)

print('\nHere is the sorted list:')
print(sorted(cars))

print('\nHere is the orginal list again:')
print(cars)

print('\nHere is the reversed list:')
print(sorted(cars,reverse=True))
print(cars)
cars.reverse()
print('\nHere is the reversed list:')
print(cars)

print(len(cars))

print(cars)
cars.append('Bmw')
for car in cars:
	if car == 'bmw' or 'Bmw':
		print(car.upper())
	else:
		print(car.title())

