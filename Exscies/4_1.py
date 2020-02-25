
pizzes = ['seefood','cheese','vegetable']
for pizz in pizzes:
	print(pizz)
	print('I like ' + pizz.title() + ' pizz')
print('I really like pizza!')


animals = ['dog','cat','chicken','duck']
for animal in animals:
	print(animal)
	print('A' + animal + 'would make a great pet')
print('Any of these animals would make a great pet!')

#4.3 create list

for value in range(1,5):
	print(value)

numbers = list(range(1,6))
print(numbers)


for i in range(1,21):
	print(i)

list1 = list(range(1,21))
for number in list1:
	print(number)

list2 = list(range(1,1000001))
print(min(list2))
print(max(list2))
print(sum(list2))

ood_numbers = list(range(1,20,2))
for ood_number in ood_numbers:
	print(ood_number)

three_numbers = list(range(3,31,3))
for three_number in three_numbers:
	print(three_number)

cube_numbers = [value**3 for value in range(1,11)]
print(cube_numbers)
for cube_number in cube_numbers:
	print(cube_number)

cube_numbers = []
for value in range(1,11):
	cube_numbers.append(value**3)
print(cube_numbers)

players = ['Charles','martina','michael','florence','eli']
print('The first three items in the list are:')
for name in players[:3]:
	print(name.title())
print('Three items from the middle of the list are:')
for name in players[1:4]:
	print(name.title())
print('The last three items in the list are:')
for name in players[-3:]:
	print(name.title())

friend_pizzas = pizzes[:]

pizzes.append('Salt')
friend_pizzas.append('chille')
print('My favorite pizzas are:')
for pizza in pizzes:
	print(pizza)
print('My friend favorite pizzas are:')
for pizza in friend_pizzas:
	print(pizza)


tuple_food = ('pizza','beer','beef','pasta','chiken')
for food in tuple_food:
	print(food)

tuple_food = ('pizza','beer','beef','ice cream','rice')
for food in tuple_food:
	print(food)
