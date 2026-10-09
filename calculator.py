# Greeting message
print('Olá, seja bem-vindo ao meu programa!')
name = input('Por favor, digite seu nome: ')
# Personalized greeting
print(f'Olá, {name}! É um prazer conhecê-lo(a).')

# This program will ask about value of and operation to perform
value1 = float(input('Digite o primeiro valor: '))
value2 = float(input('Digite o segundo valor: '))
operation = input('Digite a operação que deseja realizar (+, -, *, /): ')

# Perform the operation based on user input
if operation == '+':
    result = value1 + value2
elif operation == '-':
    result = value1 - value2
elif operation == '*':
    result = value1 * value2
elif operation == '/':
    if value2 != 0:
        result = value1 / value2
    else:
        result = 'Erro: Divisão por zero não é permitida.'
else:
    result = 'Erro: Operação inválida.'

# Display the result
print(f'O resultado da operação é: {result}')





