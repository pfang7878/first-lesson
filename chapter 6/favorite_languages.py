
favorite_languages = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
}

print("Sarah's favorite language is " + 
	favorite_languages['sarah'].title() + '.')

for name,language in favorite_languages.items():
	print(name.title() + "'s favorite language is " +
		language.title())

for name in favorite_languages.keys():
	print(name.title())

for name in favorite_languages:
	print(name)


friends = ['phil','sarah']
for name in favorite_languages:
	print(name.title())

	if name in friends:
		print(' Hi ' + name.title() +
			',I see your favorite language is ' +
			favorite_languages[name].title())
