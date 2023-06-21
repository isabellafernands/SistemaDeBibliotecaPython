import bd
import matplotlib.pyplot as plt


class Emprestimo:

  def __init__(self, data_emprestimo, data_devolucao, status, cpf, isbn):
    self.data_emprestimo = data_emprestimo
    self.data_devolucao = data_devolucao
    self.status = status
    self.cpf = cpf
    self.isbn = isbn

  #------ CREATE ------
  def cadastrarEmprestimo(self):
    print("Preencha as informações do Empréstimo:\n")
    data_emprestimo = input("Data de Empréstimo (dd/mm/aaaa): ")
    data_devolucao = input("Data de Devolução (dd/mm/aaaa): ")
    status = input("Status do Empréstimo: ")
    cpf = input("CPF do Usuário: ")
    isbn = input("ISBN do Livro: ")
    print("\nCadastrando Empréstimo...")
    bd.add_emprestimo(data_emprestimo, data_devolucao, status, cpf, isbn)
    print("\nEmpréstimo cadastrado com sucesso! :) ")

  #------ READ -----
  def exibirEmprestimo(self):
    cpf = input("Digite o CPF do usuário para exibir o empréstimo: ")
    emprestimo = bd.get_emprestimo(cpf)

    if emprestimo:
      print("\nInformações do Empréstimo:")
      print(f"CPF do Usuário: {emprestimo['cpf']}")
      print(f"Data de Empréstimo: {emprestimo['data_Emp']}")
      print(f"Data de Devolução: {emprestimo['data_Dev']}")
      print(f"Status: {emprestimo['status']}")
      print(f"ISBN do Livro: {emprestimo['isbn']}")
      print("\n")
    else:
      print("\nEmpréstimo não encontrado.\n")

  #------ UPDATE ------
  def atualizarEmprestimo(self):
    cpf = input("Digite o CPF do usuário para atualizar o empréstimo: ")
    emprestimo = bd.get_emprestimo(cpf)

    if emprestimo:
      print("Preencha as informações atualizadas do Empréstimo:\n")
      data_emprestimo = input("Data de Empréstimo atualizada (dd/mm/aaaa): ")
      data_devolucao = input("Data de Devolução atualizada (dd/mm/aaaa): ")
      status = input("Status do Empréstimo atualizado: ")
      isbn = input("ISBN do Livro atualizado: ")
      print("\nAtualizando Empréstimo...")
      bd.update_emprestimo(data_emprestimo, data_devolucao, status, cpf, isbn)
      print("\nEmpréstimo atualizado com sucesso! :) ")
    else:
      print("\nEmpréstimo não encontrado.\n")

  #------ DELETE ------
  def excluirEmprestimo(self):
    cpf = input("Digite o CPF do usuário para excluir o empréstimo: ")
    print("\nExcluindo Empréstimo...")
    bd.remove_emprestimo(cpf)
    print("\nExclusão realizada com sucesso!")

  def gerar_grafico_emprestimos(self):
    dados = self.obter_dados_para_grafico()

    # Separar os meses e a quantidade de empréstimos em listas
    meses = list(dados.keys())
    quantidades = list(dados.values())

    # Configurar o gráfico
    plt.figure(figsize=(10, 6))
    plt.bar(meses, quantidades)
    plt.xlabel('Mês')
    plt.ylabel('Quantidade de Empréstimos')
    plt.title('Gráfico de Empréstimos por Mês')

    # Exibir o gráfico
    plt.show()
  def obter_dados_para_grafico(self):
    dados = {}
    for i in range(12):
      dados[str(i + 1)] = 0

    emprestimo = bd.get_emprestimos()
    meses = []

    for empre in emprestimo:
      meses.append(empre[1][2:4])

    for mes in meses:
      if mes[0] == '0':
        dados[mes[1]] += 1
      else:
        dados[mes] += 1

    return dados
