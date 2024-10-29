print('Olá, informe sua idade abaixo e diremos sua faixa etária')

idade = int(input('Digite o número da sua idade: '))

if idade <= 12:
    print(f'Aos {idade} anos você é considerado(a) criança')
elif 12 < idade < 18:
    print(f'Aos {idade} anos você é considerado(a) adolescente')
else:
    print(f'Aos {idade} anos você é considerado(a) adulto')


# Criando uma lista de compras
lista_de_compras = ["Maçã", "Banana", "Leite", "Pão", "Queijo"]

# Adicionando um item à lista
lista_de_compras.append("Ovos")

# Removendo um item da lista
lista_de_compras.remove("Banana")

# Exibindo a lista
print("Lista de Compras:")
for item in lista_de_compras:
    print("- " + item)