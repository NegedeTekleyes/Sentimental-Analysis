animals = ["cat", "dog", "rabbit", "horse", "lion", "tiger", "elephant"]
print(animals[0:3:1])  #Print only the first three animals using slicing.
print(animals[0:len(animals):2]) # Print every second animal in the list (skip one at a time).

animals.append("giraffe")
animals.pop(2)
animals.reverse()

for tuple in enumerate (animals):
    print(f'Animals: {tuple}')
leader, guardian, *other = animals
print(leader,guardian,other)