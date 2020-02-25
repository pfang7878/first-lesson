
car = 'subaru'
if car.lower() == 'subaru':
	print('Is car == "subaru"? I predict True.')
	print('car == "subaru"')

if car.lower() != 'audi':
	print("\nIs car == 'audi'? I predict False.")
	print('car == subaru')


str1 = 'Audi'
str2 = 'audi'

print(str1 == str2)
print(str1 != str2)
print(str1.lower() == str2.lower())

number1 = 10
number2 = 20

print(number1 < number2)
print(number1 > number2)

str3 = 'i like python!'
if 'k' in str3:
	print('k is in the list!')
if 'm' not in str3:
	print('m is not in the list!')


#5-3

alien_color = ['green','yellow','red']

alien = 'green'

if alien == 'green':
	print('You got 5 points.')

if alien == 'green':
	print('You got 5 points')
if alien == 'yellow':
	print('You got 10 points')
if alien == 'red':
	print('You got 15 points')


if alien == 'green':
	print('You got 5 points')
elif alien == 'yellow':
	print('You got 10 points')
elif alien == 'red':
	print('You got 15 points')


age = 1

if age < 2:
	print('You are a baby!')
elif age < 4:
	print('You are learning how to walk!')
elif age < 13:
	print('You are a child!')
elif age < 20:
	print('You are a youth!')
elif age < 65:
	print('You are a adult person!')
else:
	print('You are an old person!')


favorite_fruits = ['apple','banana','orange','corn']

if 'banana' in favorite_fruits:
	print('You really like banana')
if 'orange' in favorite_fruits:
	print('You really like orange')
if 'corn' in favorite_fruits:
	print('You really like corn')
if 'apple' in favorite_fruits:
	print('You really like apple!')





#5-8
usernames = []
#usernames = ['john','don','kent','mike','alvin','admin']
if usernames:
	for username in usernames:
		if username.lower() == 'admin':
			print('Hello admin, would you like to see a status report?')
		else:
			print('Hello ' + username.title() + ',thank you for logging in again')
else:
	print('We need to find some users!')



current_users = ['jel','juvy','mel','stwart','srini']
new_users = ['jel','juvy','mateen','odessa','mane']

for new_user in new_users:
	if new_user.lower() in current_users:
		print(new_user + ' is existing yser, please entry new username')
	else:
		print(new_user + ' was created!')


numbers = list(range(1,10))
print(numbers)
for number in numbers:
	if number == 1:
		print('\n1st')
	elif number == 2:
		print('\n2nd')
	elif number == 3:
		print('\n3st')
	else:
		print('\n'+ str(number) + 'th')
