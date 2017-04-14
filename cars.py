showroom = {'Nissan Rogue','Nissan Leaf','Honda Accord','Ford Taurus'}

print(len(showroom))

# showroom.append('Ford Taurus')    can't append a set
# print(showroom)

new_showroom = {'Ford Escort','Nissan Juke'}
showroom.update(new_showroom)
# print(showroom)

showroom.discard('Nissan Leaf')
print(showroom)

junkyard = {'Porsche 911','Porsche 944','Ford Taurus','Ferrari Testarossa','Honda Accord','Tesla X'}
print(junkyard)

exist_in_both = showroom.intersection(junkyard)
print(exist_in_both)

showroom_plus_junkyard = showroom.union(junkyard)
print(showroom_plus_junkyard)

#remove any cars that you acquired from the junkyard that you want in your showroom.
for car in showroom_plus_junkyard:
    if car in junkyard:
        junkyard.discard(car)
print("The junkyard is now empty: {}".format(junkyard))