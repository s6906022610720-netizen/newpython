heroes = ['Ironman', 'Thor', 'Hilk', 'Superman', 'Spiderman']
h2 = ['dr. Strane', 'Cpt. America', 'Black Panther', 'Ant Man']
      
heroes.insert(0, h2[0])
print(heroes.index('Thor'))
heroes.insert(heroes.index('thor'), h2[1])
print(heroes)
heroes.remove('Superman')
heroes.append('Ant Man')
print(heroes)
heroes.sort()
print(heroes)
heroes.reverse()
print(heroes)
newheroes = heroes
newheroes[0] = 'Wonder Women'
print(heroes)
copyheroes = [] + heroes
print(copyheroes)
copyheroes[0] = 'Hanuman'
print(heroes)
print(copyheroes)