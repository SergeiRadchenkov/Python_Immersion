import random as rnd

START = -100
STOP = 1_000
STEP = 10
data = [2, 4, 6, 8, 42, 73]

print(f'{rnd.randint(START, STOP) = }')
print(f'{rnd.uniform(START, STOP) = }')
print(f'{rnd.choice(data) = }')
print(f'{rnd.randrange(START, STOP, STEP) = }')
