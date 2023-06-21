from usuario import Usuario
from livro import Livro
from emprestimo import Emprestimo
import matplotlib.pyplot as plt
from colorama import init, Fore, Style

# Inicializar a biblioteca colorama
init()


# Função para exibir o menu principal
def exibir_menuPRINCIPAL():
  while True:
    try:
      limpar()
      print(f"\n{Fore.MAGENTA}MENU:{Style.RESET_ALL}")
      print(f"{Fore.CYAN}1. Manter Livros")
      print(f"{Fore.CYAN}2. Manter Usuários")
      print(f"{Fore.CYAN}3. Manter Empréstimos")
      print(f"{Fore.RED}4. Sair{Style.RESET_ALL}")
      selecao = int(
        input(f"{Fore.YELLOW}Selecione uma opção:{Style.RESET_ALL} "))

      if selecao == 1:
        menuLivro()
      elif selecao == 2:
        menuUsuario()
      elif selecao == 3:
        menuEmprestimo()
      elif selecao == 4:
        break
      else:
        print(
          f"{Fore.RED}\nOpção inválida! Por favor, tente novamente.{Style.RESET_ALL}"
        )
    except ValueError as e:
      print(
        f"{Fore.RED}\nOpção inválida, por favor tente novamente. Erro: {e}{Style.RESET_ALL}"
      )
    finally:
      if selecao == 4:
        print(
          f"{Fore.YELLOW}Obrigada por utilizar nosso sistema!\nAté logo! :) {Style.RESET_ALL}"
        )
      else:
        print(f"{Fore.RED}\nOpção inválida! Tente novamente.{Style.RESET_ALL}")


def limpar():
  # Importar o módulo os do sistema operacional
  import os
  # Importar um módulo para aguardar um tempo em segundos passados como parâmetro
  from time import sleep

  def screen_clear():
    # Linux ou Mac
    if os.name == 'posix':
      _ = os.system('clear')
    else:
      # Windows
      _ = os.system('cls')

  sleep(1)
  screen_clear()


def menuUsuario():
  print(f"\n{Fore.MAGENTA}----- MENU DE USUÁRIO -----")
  print(f"{Fore.CYAN}1. Cadastrar Usuário")
  print(f"{Fore.CYAN}2. Exibir Usuário")
  print(f"{Fore.CYAN}3. Atualizar Usuário")
  print(f"{Fore.CYAN}4. Excluir Usuário")
  print(f"{Fore.RED}0. Voltar ao Menu Principal")

  while True:
    opcao = input(f"\n{Fore.YELLOW}Digite a opção desejada: {Style.RESET_ALL}")

    if opcao == "1":
      usuario = Usuario(None, None, None, None, None, None)
      usuario.cadastrarUsuario()
      menuUsuario()
    elif opcao == "2":
      usuario = Usuario(None, None, None, None, None, None)
      usuario.exibirUsuario()
      menuUsuario()
    elif opcao == "3":
      usuario = Usuario(None, None, None, None, None, None)
      usuario.atualizarUsuario()
      menuUsuario()
    elif opcao == "4":
      usuario = Usuario(None, None, None, None, None, None)
      usuario.excluirUsuario()
      menuUsuario()
    elif opcao == "0":
      exibir_menuPRINCIPAL()
    else:
      print(
        f"{Fore.RED}Opção inválida! Por favor, digite uma opção válida.{Style.RESET_ALL}"
      )

  print("Retornando ao Menu Principal...")


def menuLivro():
  #livro = None
  book = Livro()  #(None, None, None, None, None, None, None, None)

  print(f"{Fore.MAGENTA}-----MENU DE LIVRO -----")
  print(f"{Fore.CYAN}1. Cadastrar Livro")
  print(f"{Fore.CYAN}2. Exibir Livro")
  print(f"{Fore.CYAN}3. Atualizar Livro")
  print(f"{Fore.CYAN}4. Excluir Livro")
  print(f"{Fore.RED}0. Voltar ao Menu Principal")

  while True:
    opcao = input(f"\n{Fore.YELLOW}Digite a opção desejada: {Style.RESET_ALL}")

    if opcao == "1":
      book = Livro()  #(None, None, None, None, None, None, None, None)
      book.cadastrarLivro()
      menuLivro()
    elif opcao == "2":
      #if book.exibirLivro() is not None:
      book.exibirLivro()
      menuLivro()
      #else:
      #print("Nenhum livro cadastrado. Por favor, cadastre um livro primeiro.")
    elif opcao == "3":
      if book is not None:
        book.atualizarLivro()
        menuLivro()
      else:
        print(
          "Nenhum livro cadastrado. Por favor, cadastre um livro primeiro.")
    elif opcao == "4":
      if book is not None:
        book.excluirLivro()
        book = None
        menuLivro()
      else:
        print(
          "Nenhum livro cadastrado. Por favor, cadastre um livro primeiro.")
    elif opcao == "0":
      exibir_menuPRINCIPAL()
    else:
      print(
        f"{Fore.RED}Opção inválida! Por favor, digite uma opção válida.{Style.RESET_ALL}"
      )

  print("Retornando ao Menu Principal...")


def menuEmprestimo():
  empres = Emprestimo(None, None, None, None, None)

  print(f"{Fore.MAGENTA}----- MENU DE EMPRÉSTIMO -----")
  print(f"{Fore.CYAN}1. Cadastrar Empréstimo")
  print(f"{Fore.CYAN}2. Exibir Empréstimo")
  print(f"{Fore.CYAN}3. Atualizar Empréstimo")
  print(f"{Fore.CYAN}4. Excluir Empréstimo")
  print(
    f"{Fore.CYAN}5. Exibir gráfico de Empréstimos")  # Nova opção adicionada
  print(f"{Fore.RED}0. Voltar ao Menu Principal")

  while True:
    opcao = input(f"\n{Fore.YELLOW}Digite a opção desejada: {Style.RESET_ALL}")

    if opcao == "1":
      empres.cadastrarEmprestimo()
      menuEmprestimo()
    elif opcao == "2":

      empres.exibirEmprestimo()
      menuEmprestimo()
    elif opcao == "3":
      if empres is not None:
        empres.atualizarEmprestimo()
        menuEmprestimo()
      else:
        print(
          "Nenhum empréstimo cadastrado. Por favor, cadastre um empréstimo primeiro."
        )
    elif opcao == "4":
      if empres is not None:
        empres.excluirEmprestimo()
        empres = None
        menuEmprestimo()
      else:
        print(
          "Nenhum empréstimo cadastrado. Por favor, cadastre um empréstimo primeiro."
        )
    elif opcao == "5":
      if empres is not None:
        empres.gerar_grafico_emprestimos(
        )  # Chamada do método para exibir o gráfico
        menuEmprestimo()
      else:
        print(
          "Nenhum empréstimo cadastrado. Por favor, cadastre um empréstimo primeiro."
        )
      menuEmprestimo()
    elif opcao == "0":
      exibir_menuPRINCIPAL()
    else:
      print(
        f"{Fore.RED}Opção inválida! Por favor, digite uma opção válida.{Style.RESET_ALL}"
      )

  print("Retornando ao Menu Principal...")


exibir_menuPRINCIPAL()
