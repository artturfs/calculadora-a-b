print('Você quer usar qual operação?')
print('A - Soma')
print('B - Subtração')
print('C - Multiplicação')
print('D - Divisão')
alternativa = (input())

if alternativa == 'a' or alternativa == 'A':
    print('Escolha um número para A')
    a = float(input())
    print('Escolha um número para B')
    b = float(input())  
    soma = a + b
    print('O resultado de', a, '+', b, 'é:', soma)

elif alternativa == 'b' or alternativa == 'B':
    print('Escolha um número para A')
    a = float(input())
    print('Escolha um número para B')
    b = float(input())
    sub = a - b
    print('O resultado de', a, '-', b, 'é:', sub)

elif alternativa == 'c' or alternativa == 'C':
    print('Escolha um número para A')
    a = float(input())
    print('Escolha um número para B')
    b = float(input())
    mult = a * b
    print('O resultado de', a, 'x', b, 'é:', mult)

elif alternativa == 'd' or alternativa == 'D':
    print('Escolha um número para A')
    a = float(input())
    print('Escolha um número para B')
    b = float(input())
    div = a / b
    print('O resultado de', a, '/', b, 'é:', div)

else:
    print('Alternativa inválida.')