name = 'Alex'
age = None

a = 42
print(id(a))
a = 'Hello world'
print(id(a))
a = 3.14 / 3
print(id(a))

print(name, age, a, 456, 'text', sep=' (=^.^=) ', end='#')
print('Any text')
res = input('Print your text: ')
print('Ты написал:', res)

ADULT = 18
age = int(input('Сколько тебе лет? '))
how_old = age - ADULT
print(how_old, 'лет назад ты стал совершеннолетним')