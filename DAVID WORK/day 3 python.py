#string method .capitalize
name = 'david'
print(name .capitalize() )

box = 'candle'
print(box.capitalize())

#.casefold()
box = 'CANDLE'
print(box.casefold())

#.center()
name = 'david'
print(name.center(20))
print(name.center(20,'*'))

#.count()
names = 'john, luke, john, andy, joy'
print(names.count('j'))

#.upper()
print(names.upper())
names2 = 'JOHN, LUKE, JOHN, ANDY, JOY'

#.replace()
names = 'john, luke, john, andy, joy'
print(names.replace('joy', 'tom'))
# removesuffix() and removepreffix

print(names.removeprefix('john')) # will take off an item from the left side.
print(names.removesuffix('joy')) # it takes an item from the right side.

#.title()
book = ' the tortoise and the snake'
print(book.title())

#len()
print(len(book))

#string format
'''string formatting also know as interpolation, which is the process
of inserting a variable of different value into somthing else'''
# %,{ }, concatenation

name = 'joey'
age = 13
print('your name is',name)

#% modulo operator
print(' i am %s and %d' %(name, age))

#format method
name1 =  'john'
name2 = 'yamal'
name3 = 'ruth'

print('{} call {} to inform {} that i am going home'.format(name1, name2, name3))
print("Let's {} and {} with instincthub".format('learn', 'upskill'))

#f string
name = 'mavis'
age = 30
print(f" i am {name} and i am {age} years old")




