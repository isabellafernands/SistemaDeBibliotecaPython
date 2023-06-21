import bd


class Livro:

  def __init__(self,
               titulo=None,
               isbn=None,
               subtitulo=None,
               autor=None,
               editora=None,
               edicao=None,
               genero=None,
               observacao=None):
    self.titulo = titulo
    self.isbn = isbn
    self.subtitulo = subtitulo
    self.autor = autor
    self.editora = editora
    self.edicao = edicao
    self.genero = genero
    self.observacao = observacao

  # ------ CREATE ------

  def cadastrarLivro(self):
    print("Preencha as informações do Livro:\n")
    self.titulo = input("Título do Livro: ")
    self.autor = input("Autor: ")
    self.ano = input("Ano de publicação: ")
    self.isbn = input("ISBN do Livro: ")
    self.editora = input("Editora: ")
    self.edicao = input("Edição: ")
    self.observacao = input("Observação necessária: ")
    self.genero = input("Gênero literário: ")
    self.subtitulo = input("Subtítulo (opcional): ")

    print("\nCadastrando Livro...")
    #(titulo, isbn, subtitulo, autor, editora, edicao, genero, observacao)
    bd.add_livro(self.titulo, self.isbn, self.subtitulo, self.autor, self.editora, self.edicao,  self.genero, self.observacao)
    print("\nLivro cadastrado com sucesso! :)")

  # ------ READ -----

  def exibirLivro(self):
    isbn = input("\nQual o ISBN do livro que deseja exibir? ")
    livro = bd.get_livro(isbn)
    if livro:
      print("Informações do Livro:\n")
      print(f"Título: {livro[0]}")
      print(f"Autor: {livro[3]}")
      print(f"Ano de Publicação: {livro[2]}")
      print(f"ISBN: {livro[1]}")
      print(f"Editora: {livro[4]}")
      print(f"Edição: {livro[6]}")
      print(f"Gênero Literário: {livro[5]}")
      print(f"Observação: {livro[7]}")
    else:
      print("Livro não encontrado.")

  # ------ UPDATE ------

  def atualizarLivro(self):
    isbn = input("\nQual o ISBN do livro que deseja atualizar? ")
    print("Preencha as informações atualizadas do Livro: \n")
    self.titulo = input("\nTítulo atualizado: ")
    self.subtitulo = input("\nSubtítulo atualizado: ")
    self.autor = input("\nAutor atualizado: ")
    self.editora = input("\nEditora atualizada: ")
    self.edicao = input("\nEdição atualizada: ")
    self.genero = input("Gênero literário atualizado: ")
    self.observacao = input("\nObservação atualizada: ")
    print("\nAtualizando Livro...")
    bd.update_livro(isbn, self.titulo, self.subtitulo, self.autor,
                    self.editora, self.edicao, self.genero, self.observacao)
    print("\nLivro atualizado com sucesso! :) ")

  # ------ DELETE ------

  def excluirLivro(self):
    isbn = input("\nQual o ISBN do livro que deseja excluir? ")
    print("\nExcluindo Livro...")
    bd.remove_livro(isbn)
    print("\nExclusão realizada com sucesso!")
