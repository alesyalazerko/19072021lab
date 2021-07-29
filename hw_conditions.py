# 1
a1, b1, c1 = map(int, input(f'please enter you numbers separated with  " ":').split())
print(min(a1, b1, c1))

# 3
year = int(input('please, enter your year: '))
if year % 100 == 0:
    if year % 400 == 0:
        print('366 days')
    else:
        print('365 days')
else:
    if year % 4 == 0:
        print('366 days')
    else:
        print('365 days')

from math import *

# 5
a5, b5, c5, d5 = map(int, input(f'please enter you numbers separated with  " ":').split())
min = min(a5, b5, c5, d5)
print(cos(min))

#6
a6, b6, c6, d6 = map(int, input(f'please enter you numbers separated with  " ":').split())
max = max(a6, b6, c6, d6)
print(sin(max))

# 9
x9, y9, z9 = map(int, input(f'please enter you numbers separated with  " ":').split())
if x9 ** 2 + y9 ** 2 == z9 ** 2:
    print('The triangle exists', (x9 * y9) / 2)
else:
    print('The triangle does not exist')

