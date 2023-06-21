import bd

class Usuario:
    def __init__(self, nome, email, cpf, telefone, data_nasc, endereco):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.telefone = telefone
        self.data_nasc = data_nasc
        self.endereco = endereco

    def cadastrarUsuario(self):
        print("Preencha as informações do Usuário:")
        novo_usuario = input("\nNome Completo: ")
        email = input("\nEmail: ")
        cpf = input("\nCPF (Apenas números): ")
        telefone = input("\nTelefone: ")
        data_nasc = input("\nData de nascimento (dd/mm/aaaa): ")
        endereco = input("Endereço: ")
        print("\nCadastrando novo usuário...")
        bd.add_usuario(novo_usuario, email, cpf, telefone, data_nasc, endereco)
        print("\nUsuário cadastrado com sucesso! :)\n")

    def exibirUsuario(self):
        print("Exibir usuário:")
        cpf = input("\nDigite o CPF do usuário: ")
        usuarios = bd.get_usuarios()
        for usuario in usuarios:
            if str(usuario[2]) == cpf:
                print("\nNome: ", usuario[0])
                print("Email: ", usuario[1])
                print("CPF: ", usuario[2])
                print("Telefone: ", usuario[3])
                print("Data de Nascimento: ", usuario[4])
                print("Endereço: ", usuario[5])
                return
        print("\nUsuário não encontrado!")

    def atualizarUsuario(self):
        cpf = input("\nQual o CPF do usuário que deseja editar? ")
        print("\nPreencha com as informações atualizadas do usuário:")
        upd_usuario = input("\nNome Completo: ")
        upd_email = input("\nEmail: ")
        upd_cpf = input("\nCPF (Apenas números): ")
        upd_telefone = input("\nTelefone: ")
        upd_data_nasc = input("\nData de nascimento (dd/mm/aaaa): ")
        upd_endereco = input("Endereço: ")
        print("\nAtualizando as informações...")
        bd.update_usuario(cpf, upd_usuario, upd_email, upd_telefone, upd_data_nasc, upd_endereco)
        print("\nUsuário atualizado com sucesso! :)\n")

    def excluirUsuario(self):
        cpf = input("\nQual o CPF do usuário que deseja apagar? ")
        print("\nApagando usuário...")
        bd.remove_usuario(cpf)
        print("\nUsuário excluído com sucesso! :)\n")
