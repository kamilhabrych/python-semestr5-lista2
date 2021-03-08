n = int(input('Podaj n:'))
m = int(input('Podaj m:'))

potega = 1
y = m

if n == 0 and m == 0:
    print(n,'do potęgi',m,'równa się',1)
elif n == 0:
    print(n,'do potęgi',m,'równa się',0)
elif m == 0:
    print(n,'do potęgi',m,'równa się',1)
else:
    while y > 0:
        potega = potega * n
        y = y - 1

print(n,'do potęgi',m,'równa się',potega)