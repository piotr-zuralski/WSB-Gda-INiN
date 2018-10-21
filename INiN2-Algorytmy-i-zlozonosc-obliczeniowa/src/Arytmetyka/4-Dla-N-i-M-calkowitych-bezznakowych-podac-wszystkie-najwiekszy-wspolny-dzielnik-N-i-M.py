# 4. (5 pkt) Dla N i M całkowitych bezznakowych podać wszystkie największy wspólny dzielnik N i M

print('Program podaje wszystkie największe wspolne dzielniki (NWD) dla liczb N i M')

N = int(input('Proszę podać liczbę N: '))
M = int(input('Proszę podać liczbę M: '))

n = N
m = M

while n != m:
    if n > m:
        n = n - m
    else:
        m = m - n

print('Największy wspólny dzielnik (NWD) dla liczb N="{:d} i M="{:d} to: "{:d}"'.format(N, M, n))
