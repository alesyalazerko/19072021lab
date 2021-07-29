# 10
n10 = 1
while n10 <= 20:
    print(2 ** n10, sep='☀️')
    n10 += 1

# 8
n8 = int(input('enter your number:'))
a8 = 1
step = 4
while a8 <= n8:
    a8 += step
    step += 1
print(a8)

# 7
a7 = int(input('please, enter your number: '))
sum7 = 0
for i in range(a7, 51):
    sum7 += i ** 2
print(sum7)

# 6
a6 = int(input('please, enter you number: '))
sum6 = 0
for x in range(201):
    sum6 += x
print('avg =', sum6 / (201 - 1))

# 5
a5 = int(input('please, enter your number: '))
b5 = int(input('please, enter your number: '))
sum5 = 0
for i in range(a5, b5):
    sum5 += i ** 2
print(sum5)
