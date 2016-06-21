'''임의의 요소 뽑기'''

import random

values = [1, 2, 3, 4, 5, 6]
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))

print(random.sample(values, 2))
print(random.sample(values, 2))
print(random.sample(values, 3))
print(random.sample(values, 3))

print(random.shuffle(values))
print(values)
print(random.shuffle(values))
print(values)

print(random.randint(0, 10))
print(random.randint(0, 10))
print(random.randint(0, 10))
print(random.randint(0, 10))
print(random.randint(0, 10))
print(random.randint(0, 10))

print(random.random())
print(random.random())
print(random.random())

print(random.getrandbits(200))

random.seed()
random.seed(12345)
random.seed(b'bytedata')

import ssl

print(ssl.RAND_bytes(1))
