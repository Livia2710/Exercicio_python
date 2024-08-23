import os
import json
import sys
import tkinter as tk
from modelos.restaurante import Restaurante
from modelos.avaliacao import Avaliacao

# Função para obter o caminho do diretorio de dados
def get_data_dir():
    if getattr(sys, 'frozen', False):
        # Se estiver executando como um executavel
        return os.path.dirname(sys.executable)
    else:
        # Se estuver executndo como script
        return os.path.dirname(os.path.abspath(__file__))
    
# Nome do arquivo onde os dados dos restaurantes são armazenados
ARQUIVO_DADOS = os.path.join(get_data_dir(), 'dados_restaurantes.json')

# Função para carregar dados do restaurante a partir de um arquivo JSON
def carregar_dados():
    try:
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            Restaurante.restaurantes.clear() # Limpa a lsita de restaurante antes de carregar os novos dados
            for restaurante_dados in dados:
                restaurante = Restaurante(
                    restaurante_dados['nome'],
                    restaurante_dados['categoria']
                )
                # Configura o estado ativo e as avaliações do restaurante
                restaurante._ativo = restaurante_dados['ativo']
                restaurante._avaliacao =[Avaliacao(**avaliacao) for avaliacao in restaurante_dados ['avaliacao']]
    except FileNotFoundError:
        print(f"Arquvo de dados não foi encontrado. Criando um novo arquivo em {ARQUIVO_DADOS}")
        salvar_dados()


def salvar_dados():
    dados = []
    for restaurante in Restaurante.restaurantes:
        dados.append({
            'nome': restaurante._nome,
            'categoria': restaurante._categoria,
            'ativo': restaurante._ativo,
            'avaliacao': [avaliacao.__dict__() for avaliacao in restaurante._avaliacao]
        })
    with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False) # Salve os dados no arquivo com indentação para melhor leitura

# Função principal do programa, que exibe o menu e executa as ações selecionadas pelo usuario
def main():
    carregar_dados()

    while True:
        os.system('cls'if os.name == 'nt' else 'clear') # Limpa a tela antes de exibir o menu
        print("=-=-=-=- Restaurante Expresso =-=-=-=")
        print("\n1. Cadastrar restaurante")
        print(" 2. Listar restaurantes")
        print(" 3. Habilitar restaurante")
        print(" 4. Avaliar restaurante")
        print(" 5. Alterar restaurante")
        print(" 6. Excluir restaurante")
        print(" 7. Sair")

        opcao = input("\nEscolha uma opção:")

        # Chama a função correspondente a opção escolhida
        if opcao == '1':
            cadastrar_restaurante()
        elif opcao == '2':
            listar_restaurante()
        elif opcao == '3':
            habilitar_restaurante()
        elif opcao == '4':
            avaliar_restaurante()
        elif opcao == '5':
            alterar_restaurante()
        elif opcao == '6':
            excluir_restaurante()
        elif opcao == '7':
            salvar_dados() # Salva os dados antes de sair
            print("\nDados salvos. Obrigado pro usar o sistema, Até logo!")
            break
        else:
            print("Opção invalida. Tente novamente.")

        input("\nPressione Enter para continuar...")

# Função para cadastrar um novo restaurante
def cadastrar_restaurante():
    nome = input("Digite o nome do restaurante: ")
    categoria = input("Digite a categoria do restaurante: ")
    novo_restaurante = Restaurante(nome, categoria) # Cria um novo objeto Restaurante
    print(f"\nRestaurante {nome} cadastrado com sucesso !")

# Função para lsitar todos os restaurante cadstradps
def listar_restaurante():
    print("Lista de Restaurantes:")
    Restaurante.listar_restaurante()

# Função ára habilitar ou desabilitar um restaurante
def habilitar_restaurante():
    nome = input("Digite o nome do restaurante que deseja habilitar/desabilitar: ")
    for restaurante in Restaurante.restaurantes:
        if restaurante._nome.lower() == nome.lower():
            restaurante.alternar_estado() #Altera i estado do restaurante (ativo/inativo)
            print(f"Estado do restaurante {restaurante._nome} alterado para {restaurante.ativo}")
            salvar_dados() # Salva os dados após a alteração
            return
    print("Restaurante não encontrado")

# Função para adicionar uma avaliação a um restaurante
def avaliar_restaurante():
    nome = input("Digite o nome do restaurante que deseja avaliar: ")
    for restaurante in Restaurante.restaurantes:
        if restaurante._nome.lower() == nome.lower():
            cliente = input("Digite seu nome: ")
            while True:
                try:
                    nota = float(input("Digite a nota (de 0 a 10)"))
                    if 0 <= nota <= 10:
                        restaurante.receber_avaliacao(cliente, nota) # Adiciona a avaliação ao restaurante
                        print("Avaliação registrada cm sucesso!")
                        salvar_dados() 
                        return
                    else:
                        print("A nota deve estar entre 0 a 10. ")
                except ValueError:
                    print("Por favor, digite um número válido.")
    print("Restaurante não encontrado.")

# Função para alterar as informações de um restaurante
def alterar_restaurante():
    nome = input("Digite o nome do restaurante que deseja alterar: ")
    for restaurante in Restaurante.restaurantes:
        if restaurante._nome.lower() == nome.lower():
            novo_nome = input(f"Digite o novo nome do restaurante (atual: {restaurante._nome}): ")
            nova_categoria = input(f"Digite a nova categoria do restaurante (atual: {restaurante._categoria}): ")

            # Atualiza o nome e a categoria do restaurante se forem fornecidos novos valores
            if novo_nome:
                restaurante._nome = novo_nome.title()
            if nova_categoria:
                restaurante._categoria = nova_categoria.upper()

            print(f"Restaurante alterado com sucesso para: {restaurante}")
            salvar_dados()
            return
    print("Restaurante não encontrado. ")

# Função para excluir um restaurante da lista
def excluir_restaurante():
    nome = input("Digite o nome do restaurante que deseja excluir: ")
    for restaurante in Restaurante.restaurantes:
        if restaurante._nome.lower() == nome.lower():
            confirmacao = input(f"Tem certeza que deseja excluir o restaurante '{restaurante._nome}' ? (S/N): ")
            if confirmacao.lower() == 's':
                Restaurante.restaurantes.remove(restaurante) # Remove o restaurante da lista
                print(f"Restaurante '{restaurante._nome}' excluido com sucesso. ")
                salvar_dados()
            else:
                print("Operação de exclusão cancelada. ")
            return
    print("Restaurante não encontrado. ")

# ________________________________________________________________________


    # Configuração da janela principal
janela = tk.Tk() # Cria a janela principal
janela.title("Calculadora Trigonométrica") # Define o titulo da janela
janela.geometry("400x550") # Tamanho da janela
janela.configure(bg="#f0f0f0")


# Verifica se o script está sendo executado diretamente e chama a função principal
if __name__ == '__main__':
    main()

janela.mainloop()
