
players = ['Charles','martina','michael','florence','eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

print('Here are the first three players on my team:')
for player in players[:3]:
	print(player.title())

scores = [100,200,50,1000,800,600]
scores1 = scores.sort(reverse=True)
print(scores)
for i in scores[:3]:
	print(i)
