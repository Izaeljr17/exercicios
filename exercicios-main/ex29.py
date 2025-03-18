def exibir_menu():
    print("Bem vindo ao menu de cadastro")
    print("1 - Novo Cadastro")
    print("2 - Ver Cadastro")
    print("3 - Sair")
    print("-----------------------------")

    def Cadastrar_pessoa (cadastros):
        nome = input("nome:")
        idade = input("idade:")
        turma = input("turma:")
        curso = input("curso:")
        cadastros.append({"nome": nome, "idade": idade, "turma": turma, "curso": curso})
        print("Cadastro realizado com sucesso!")