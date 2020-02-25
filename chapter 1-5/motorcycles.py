motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles[0] = 'honda'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
print(motorcycles)
motorcycles.append('Honda')
motorcycles.append('Yamaha')
motorcycles.append('Suzuki')
print(motorcycles)

motorcycles.insert(0,'Ducati')
print(motorcycles)


del motorcycles[0]
print(motorcycles)

motorcycles.insert(1,'Ducati')
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles.remove('Yamaha')
print(motorcycles)
