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

def ver_cadastro (cadastros):
        if not cadastros:
            print("nenhum cadastro no sistema")
        else:
            print("\n ------ LISTA DE CADASTRO ------")
                
            for i, pessoa in enumerate (cadastros, 1):
                print(f"{i} . nome: {pessoa['Nome']}, idade:{pessoa['Idade']}, turma: {pessoa['Turma']}, curso: {pessoa['Curso']}")  

def main():
    cadastros = []
    while True:
        exibir_menu()
        opção = input("escolha uma opção:")
        if opção == "1":
            Cadastrar_pessoa(cadastros)
        elif opção == "2":
            ver_cadastro(cadastros)
        elif opção == "3":
            print("obrigado por utilizar o sistema")
            break
        else:
            print("opção inorreta.")


if __name__ == "__main__":
     main()