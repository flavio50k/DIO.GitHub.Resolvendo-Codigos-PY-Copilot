# Recebe a palavra do usuário
palavra = input("Digite uma palavra: ")

# Normaliza a palavra (remove espaços e transforma em minúsculas)
palavra_limpa = palavra.replace(" ", "").lower()

# Inverte a palavra
palavra_invertida = palavra_limpa[::-1]

# Verifica se é palíndromo
if palavra_limpa == palavra_invertida:
    print(f'"{palavra}" é um palíndromo!')
else:
    print(f'"{palavra}" não é um palíndromo.')
