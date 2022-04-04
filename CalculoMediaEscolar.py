nota1 = float(input('Digite a sua primeira nota '))
nota2 = float(input('Digite a sua segunda nota '))
nota3 = float(input('Digite a sua terceira nota '))
nota4 = float(input('Digite a sua quarta nota '))

media = (nota1 + nota2 + nota3 + nota4)/ 4

print('A sua media e ', media)

if media >= 7:
    print('Parabens voce foi aprovado')
elif media >=4:
    print('Voce esta de recuperacao')
else:
    print('Voce reprovou')
