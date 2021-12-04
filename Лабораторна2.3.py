from random import randint
a = [randint(1, 100) for i in range(7)]
print(*a)
print(*sorted(a)[:5])