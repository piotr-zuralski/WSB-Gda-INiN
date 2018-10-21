# 3. (5 pkt) Dla N i M całkowitych bezznakowych podać wszystkie wspólne dzielniki N i M

print('Program podaje wszystkie wspólne dzielniki N i M')

N = int(input('Proszę podać liczbę N: '))
M = int(input('Proszę podać liczbę M: '))

liczba_max = N
if M > N:
    liczba_max = M

wszystkie_dzielniki = ''
for i in range(liczba_max+1, 1, -1):
    if N % i == 0 and M % i == 0:
        wszystkie_dzielniki += '{},'.format(i)
del i

wszystkie_dzielniki = wszystkie_dzielniki.strip(',')
print('Wszystkie wspólne dzielniki N="{:d}" i M="{:d}" to: "{}"'.format(N, M, wszystkie_dzielniki))
