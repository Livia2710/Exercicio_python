# Importação de bibilotecas necessárias
import os

# Lista de dicionários representantes os restaurantes
restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
                {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
                {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo': False}]

def exibir_nome_do_programa():
    print("""
    𝑆𝑎𝑏𝑜𝑟 𝑒𝑥𝑝𝑟𝑒𝑠𝑠
    """)
        
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n ')

def finalizar_app():
    exibir_subtitulo('Finalizando o app\n')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal')
    main()

def opcao_invalida():
    print('Opção Inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls') #Limpa a tela (Funciona somente no Window)
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def main():
    """
    Função principal que inicia o programa
    """
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
    
# _______________________________________________________________________

def cadastrar_novo_restaurante():
    """
Função para cadastar um novo restaurante

Inputs: 
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante à lsita de restaurantes
"""
exibir_subtitulo('Cadastro de novos restaurante\n')
nome_do_restaurante = input(f'Digite o nome do restaurante que deseja cadastrar: ')
categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
restaurantes.append(dados_do_restaurante)
print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')

voltar_ao_menu_principal()

def alternar_estado_do_restaurante():
    """
    Função para ativar ou desativar um restaurante
    """
    exibir_subtitulo('Alternando estado do restaurante\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
         if nome_do_restaurante == restaurante['nome']:
              restaurante_encontrado = True
              restaurante['ativo'] = not restaurante['ativo'] #Inverte o estado(False para True)
              mensagem = f'O restaurante {nome_do_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_do_restaurante} foi desativado com sucesso!'
              print(mensagem)

    if not restaurante_encontrado:
         print('O restaurante não foi encontrado!')

voltar_ao_menu_principal()

def listar_restaurante():
    """
    Função para listar tdos os restaurante cadastrados
    """
    exibir_subtitulo('Listando os restaurantes\n')

    print(f'{nome_do_restaurante.ljust(21)} | {'categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
         nome_do_restaurante = restaurante['nome']
         categoria = restaurante['categoria']
         ativo = 'ativado' if restaurante['ativo'] else 'desativado'
         print(f'-{nome_do_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
 
    voltar_ao_menu_principal()
# __________________________________________________________________

def escolher_opcao():
    """
    Função para processar a escolha do usuário no menu principal
    """  
    try:
       opcao_escolhida = int(input('Escolha uma opção'))

       if opcao_escolhida == 1:
           cadastrar_novo_restaurante()
       elif opcao_escolhida == 2:
           listar_restaurante()
       elif opcao_escolhida == 3:
           alternar_estado_do_restaurante()
       elif opcao_escolhida == 4:
           finalizar_app()
       else:
           opcao_invalida()
    except:
        opcao_invalida()
           
           