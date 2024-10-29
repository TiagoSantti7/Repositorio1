import os

restaurantes = [{'nome': 'Praça', 'categoria':'Japonesa', 'status':False}, 
                {'nome': 'Pizza Suprema', 'categoria':'Pizza', 'status':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'status': False}]

def exibir_nome_do_programa():
    '''Essa função exibi o nome do programa'''
    print("""ＳＡＢＯＲ ＥＸＰＲＥＳＳ""")

def exibir_opcoes():
    '''Essa função exibe as opções do menu'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar status do restaurante')
    print('4. Sair\n')

def voltar_ao_menu_principal():
    '''Essa função faz com que o programa volte para o menu principal'''
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def exibir_subtitulo(texto):
    '''Essa função limpa o console para exbir o texto indicado'''
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def finalizar_app():
    '''Essa função finaliza o app'''
    exibir_subtitulo('Finalizando app...')

def opcao_invalida():
    '''Essa função Exibe o texto para opções invalidas e retorna ao perfil'''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    ''' Essa função é responsável por cadastrar um novo restaurante

        Inputs:
        - Nome do restaurante
        - Categoria

        Outputs:
        - Adiciona um novo restaurante a lista de restaurantes

    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurente = {'nome':nome_do_restaurante, 'categoria':categoria, 'status':False}
    restaurantes.append(dados_do_restaurente)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def alterar_estado_restaurante():

#parte que irá receber o valor busca para ativação/desativação do restaurante.(visual) 
    exibir_subtitulo('Alternando status do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o status: ')
    restaurante_encontrado = False

#parte que irá executar a ativação/desativação do restaurante (prática)
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['status'] = not restaurante['status']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['status']  else f'O restaurante {nome_restaurante} foi desativado com sucesso' # IF NA STRING FUNCIONA SE A INVERSÃO QUE O "nota restaurante['status'] " FOR DE FALSE PARA TRUE, POIS IRÁ CONSIDERAR QUE HÁ UM INDICADOR POSITIVO. E O ELSE É QUANDO A INVERSÃO FOR PARA FALSE 
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    voltar_ao_menu_principal()


def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'categoria'.ljust(20)} | {'Status'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        status = 'Ativado' if restaurante['status'] else "Desativado"
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {status}')

    voltar_ao_menu_principal()



def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()    
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()