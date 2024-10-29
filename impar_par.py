nome_de_usuario = input('Olá, digite seu nome de usuário: ')
    
print(f"""Olá {nome_de_usuario}, com duvidas se o número é impar ou par? Me informe o número abaixo e eu te respondo""")

valor_digitado = int(input('Informe o valor: '))

if valor_digitado % 2 == 0:
    print('Número par')
else:
    print('Número impar')