n = s = q = 0
while True:
    n = int(input('Digite um numero:'))
    if n == 999: #ponto de parada fica antes da soma!
          break
    s += n
    q += 1
print(f'você digitou {q} e a soma entre eles foi {s}.')

