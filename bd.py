import sqlite3

conn = sqlite3.connect("bdd.db")


def criar_bdd():
  # Tabela dos Usuários
  conn.execute("""
    CREATE TABLE IF NOT EXISTS Usuario (
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        cpf INTEGER NOT NULL PRIMARY KEY,
        telefone INTEGER NOT NULL,
        data_nasc TEXT NOT NULL,
        endereco TEXT NOT NULL
    );
    """)

  # Tabela dos Livros
  conn.execute("""
    CREATE TABLE IF NOT EXISTS Livro (
        titulo TEXT NOT NULL,
        subtitulo TEXT NOT NULL,
        isbn INTEGER NOT NULL PRIMARY KEY,
        autor TEXT NOT NULL,
        editora TEXT NOT NULL,
        genero TEXT NOT NULL,
        edicao INTEGER NOT NULL,
        observacao TEXT NOT NULL
    );
    """)

  # Tabela Emprestimo
  conn.execute("""
    CREATE TABLE IF NOT EXISTS Emprestimo (
        data_Emp TEXT NOT NULL,
        data_Dev TEXT NOT NULL,
        status TEXT NOT NULL,
        cpf INTEGER NOT NULL,
        isbn INTEGER NOT NULL,
        PRIMARY KEY (cpf),
        FOREIGN KEY (cpf) REFERENCES Usuario(cpf),
        FOREIGN KEY (isbn) REFERENCES Livro(isbn)
    );
    """)


# CRUD USUARIO


# CREATE
def add_usuario(nome, email, cpf, telefone, data_nasc, endereco):
  conn.execute(
    "INSERT INTO Usuario (nome, email, cpf, telefone, data_nasc, endereco) VALUES (?, ?, ?, ?, ?, ?)",
    (nome, email, cpf, telefone, data_nasc, endereco))
  conn.commit()


# READ
def get_usuarios():
  cursor = conn.execute("SELECT * FROM Usuario")
  return cursor.fetchall()


# UPDATE
def update_usuario(cpf, nome, email, telefone, data_nasc, endereco):
  conn.execute(
    "UPDATE Usuario SET nome = ?, email = ?, telefone = ?, data_nasc = ?, endereco = ? WHERE cpf = ?",
    (nome, email, telefone, data_nasc, endereco, cpf))
  conn.commit()


# DELETE
def remove_usuario(cpf):
  conn.execute("DELETE FROM Usuario WHERE cpf = ?", (cpf, ))
  conn.commit()


# CRUD LIVRO


# CREATE
def add_livro(titulo, isbn, subtitulo, autor, editora, edicao, genero,
              observacao):
  conn.execute(
    "INSERT INTO Livro (titulo, isbn, subtitulo, autor, editora, edicao, genero, observacao) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
    (titulo, isbn, subtitulo, autor, editora, edicao, genero, observacao))
  conn.commit()


# READ
def get_livro(isbn):
  cursor = conn.execute("SELECT * FROM Livro WHERE isbn = ?", (isbn, ))
  return cursor.fetchone()


def get_livros():
  cursor = conn.execute("SELECT * FROM Livro")
  return cursor.fetchall()


# UPDATE
def update_livro(isbn, titulo, subtitulo, autor, editora, edicao, genero,
                 observacao):
  conn.execute(
    "UPDATE Livro SET titulo = ?, subtitulo = ?, autor = ?, editora = ?, edicao = ?, genero = ?, observacao = ? WHERE isbn = ?",
    (titulo, subtitulo, autor, editora, edicao, genero, observacao, isbn))
  conn.commit()


# DELETE
def remove_livro(isbn):
  conn.execute("DELETE FROM Livro WHERE isbn = ?", (isbn, ))
  conn.commit()


# CREATE
def add_emprestimo(data_emp, data_dev, status, cpf, isbn):
  conn.execute(
    "INSERT INTO Emprestimo (data_Emp, data_Dev, status, cpf, isbn) VALUES (?, ?, ?, ?, ?)",
    (data_emp, data_dev, status, cpf, isbn))
  conn.commit()


def get_emprestimo(cpf):
  cursor = conn.execute("SELECT * FROM Emprestimo WHERE cpf = ?", (cpf, ))
  row = cursor.fetchone()
  if row:
    emprestimo = {
      'idEmprestimo': row[0],
      'data_Emp': row[1],
      'data_Dev': row[2],
      'status': row[3],
      'cpf': row[4],
      'isbn': row[5]
    }
    return emprestimo
  else:
    return None


def get_emprestimos():
  cursor = conn.execute("SELECT * FROM Emprestimo")
  return cursor.fetchall()


# UPDATE
def update_emprestimo(data_emp, data_dev, status, cpf, isbn):
  conn.execute(
    "UPDATE Emprestimo SET data_Emp = ?, data_Dev = ?, status = ?, isbn = ? WHERE cpf = ?",
    (data_emp, data_dev, status, isbn, cpf))
  conn.commit()


# DELETE
def remove_emprestimo(cpf):
  conn.execute("DELETE FROM Emprestimo WHERE cpf = ?", (cpf, ))
  conn.commit()


# Chamada da função para criar o banco de dados
criar_bdd()
