n = int(input('Podaj n:'))

silnia = 1

if n >= 1:
    for i in range (1,n+1):
        silnia = silnia * i

print(silnia)