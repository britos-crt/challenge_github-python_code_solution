# String manipulation examples

text = input('Digite seu nome(string): ')  # Prompt user for input
print(f'\nString em maiúsculas: {text.upper()}')  # Convert to uppercase
print(f'String em minúsculas: {text.lower()}')  # Convert to lowercase

# Multiple string manipulations
print(f'String com a primeira letra maiúscula: {text.capitalize()}')  # Capitalize the first letter
print(f'String com cada palavra capitalizada: {text.title()}\n')  # Capitalize each word

print(f'String mutiplicada: {text.title()}\n' * 3)  # Remove leading and trailing spaces and multiply by 3
