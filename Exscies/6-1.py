
my_friend = {'first_name':'zhiwen','last_name':'Hao','age':41,'city':'zhuozhou'}

print(my_friend['last_name'].title() + ' ' + my_friend['first_name'] +
	' is ' + str(my_friend['age']) + ' and stay in ' + my_friend['city'].title()+ '.')

numbers = {'Andy':3,'john':5,'lucas':6,'steve':2,'don':'7'}
print('Andy likes number: ' + str(numbers['Andy']))
print('\nJohn likes number: ' + str(numbers['john']))
print('\nLucas likes number: ' + str(numbers['lucas']))
print('\nSteve likes number: ' + str(numbers['steve']))
print('\nDon likes number: ' + str(numbers['don']))


words = {
	'python':'a kind of lanage',
	'list':'a kind of var',
	'tulpe':'a kind of list',
	'for':'a loop to check list',
	'if':'check false and true'
}

print('Python: ' + words['python'])
print('List: ' + words['list'])
print('Tulpe: ' + words['tulpe'])
print('for: ' + words['for'])
print('if: ' + words['if'])

for key,value in words.items():
	print(key +': ' + value)
