Perfil = [{'Nome': 'Tiago Santo', 'Idade': 22, 'Cidade': 'Rondonópolis', 'UF estado': 'MT'},
          {'Nome': 'Valéria Cilli', 'Idade': 21, 'Cidade': 'Rondonópolis', 'UF estado': 'MT'}]

Perfil_2 = {'Nome': 'Marcos', 'Idade': 20, 'Cidade': 'Rondonópolis', 'UF estado': 'MT'}

# Metodo 1 de atualizar um valor dentro de uma dicionário (melhor metodo quando há mais de uma chave "{}")
Perfil[1]['Idade'] = 20

# Metodo 2 de atualizar um valor dentro de um dicionário
Perfil_2.update({'Idade' : 19})

# Metodo de adicionar um valor ao dicionario
Perfil[0]['Profissão'] = 'Analista de Patrimonio'
Perfil[1]['Profissão'] = 'Assistente'
Perfil_2['Profissão'] = 'Analista de Patrimonio'

# Metodo para remover um item do dicionário

del Perfil[1]['Profissão']
del Perfil_2['Idade']

#########################################

numeros_quadrados = {}

for x in range(1, 6):
    numeros_quadrados[x] = x**2
print(numeros_quadrados)

#############################

Carros = {'Nome': 'Hillux', 'Chevrolet': 'S10', 'Fiat': 'Titano'}

Pesquisa = input('Informe a marca')

if Pesquisa in Carros:
    print(f"A chave {Pesquisa} está no dicionario")
else: print(f"A chave {Pesquisa} está no dicionario")
    

