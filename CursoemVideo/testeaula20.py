'''def l ():
    print('-=' *30)


l()
print('Curso em video')
l()
l()
print('Python is good')
l()
l()
print('Lucas Wilgner')
l()'''

'''def titulo(msg):
    print('-=' *30)
    print(msg)
    print('-=' *30)
    
    
titulo('Curso em video')
titulo('lucas lindo')'''

'''def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(s)


soma(b=1, a=2)
soma(535,420)'''


'''def contador(*num):
  tam = len(num)
  print(f'foram digitado os numeros {num} e ao todo são {tam} numeros')


contador(4, 5, 6)
contador(3, 6, 9)
contador(2, 10)'''

'''def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


lst = [1, 2, 3, 4, 5]
dobra(lst)
print(lst)
lst = [45, 10, 20, 30]
dobra(lst)
print(lst)'''


def soma (* valores):
    s = 0
    for num in valores:
        s += num
    print(f'somando os valores {valores} temos {s}')


soma(4, 5, 6)
soma(3, 2)



