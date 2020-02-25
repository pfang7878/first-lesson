names = ['ethan','kouzhun','andy li','Guo']
print(names[0])
print(names[1])
print(names[2])
print(names[-1])

message = ',Welcome to Python!'
print(names[0].title() + message)
print(names[1].title() + message)
print(names[2].title() + message)
print(names[-1].title() + message)

bikes = ['Honda','Halei']
print('I would like to own a ' + bikes[1] + 'bike')


names = ['zhao','qian','sun','li']
print('Hello,',names[0].title(),'can we have a dinner')
print(names[-1].title(),'cant make it')
names.remove('li')
names.append('zhou')
print(names[-1].title() + ' ' + 'can join')

names.insert(0,'wu')
print(names)
test = len(names)
print(test)
names.insert(int(test/2),'zheng')
print(names)
names.append('wang')
print(names)

print('sorry,' + names.pop() + ', you cant join')
print('sorry,' + names.pop() + ' you cant join')
print('sorry,' + names.pop() + ' you cant join')
print('sorry,' + names.pop().title() + ' you cant join')
print(len(names))
print('sorry,' + names.pop().title() + ' you cant join')
print(names[0] + ' see you later')
print(names[-1] + ' see you later')
del names[0]
del names[0]
print(names)

#3-8

places = ['NZ','Ice Island','Russe','US','Spine']
print(places)
print(sorted(places))
print(places)
print(sorted(places,reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

print(len(names))




