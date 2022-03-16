# Escreva um programa que pergunte o salário de um funcionário e calcule o
# valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Digite seu salário atual:'))
print('Seu salário atual é de R$: {:.2f}'.format(salario))
if salario <= 1250.00:
    aumento = salario*0.15
    novo = (salario * 0.15) + salario
    print('O aumento salarial é de R$: {:.2f}'.format(aumento))
    print('Seu salário com aumento será de R$: {:.2f}'.format(novo))
if salario >= 1250.00:
    aumento2 = salario*0.10
    novo2 = (salario * 0.10) + salario
    print('O aumento salarial é de R$: {:.2f}'.format(aumento2))
    print('Seu salário com aumento será de R$: {:.2f}'.format(novo2))
    