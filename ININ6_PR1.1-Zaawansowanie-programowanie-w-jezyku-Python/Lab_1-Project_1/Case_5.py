"""
5. (2 pkt) Rekurencyjny Fibonacci:
• Należy napisać funkcję rekurencyjną, która policzy wartość ciągu
Fibonacciego dla podanego n.
• Pobrać n od użytkownika i wypisać na ekran fib(n).
"""


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


while True:
    try:
        n = int(input("Podaj liczbę n: "))
    except ValueError:
        n = 0

    if n <= 0:
       print("Podaj liczbę całkowitą wiekszą od zera")
    else:
        print(fib(n))
        break
