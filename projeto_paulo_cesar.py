
# AV1 - Projeto Final: Sistema de Cadastro e Busca em Python
# Aluno: Paulo César
# Tema: Sistema de Biblioteca

livros = [
    {
        "codigo": 1,
        "titulo": "Dom Casmurro",
        "autor": "Machado de Assis",
        "ano": 1899,
        "disponivel": "Sim"
    },
    {
        "codigo": 2,
        "titulo": "O Pequeno Principe",
        "autor": "Antoine de Saint-Exupery",
        "ano": 1943,
        "disponivel": "Sim"
    },
    {
        "codigo": 3,
        "titulo": "1984",
        "autor": "George Orwell",
        "ano": 1949,
        "disponivel": "Nao"
    }
]


def exibir_menu():
    print("\n===== SISTEMA DE BIBLIOTECA =====")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Buscar livro")
    print("4 - Remover livro")
    print("5 - Sair")
    print("=================================")


def cadastrar(lista):
    print("\n--- CADASTRAR LIVRO ---")

    try:
        codigo = int(input("Codigo do livro: "))

        if buscar_indice(lista, codigo) != -1:
            print("Esse codigo ja esta cadastrado!")
            return

        titulo = input("Titulo: ").strip()
        autor = input("Autor: ").strip()
        ano = int(input("Ano de publicacao: "))

        if titulo == "" or autor == "":
            print("Preencha todos os campos!")
            return

        if ano <= 0:
            print("Ano invalido!")
            return

        disponivel = input("Disponivel? (Sim/Nao): ").strip().lower()

        if disponivel not in ["sim", "nao"]:
            print("Digite apenas Sim ou Nao!")
            return

        novo_livro = {
            "codigo": codigo,
            "titulo": titulo,
            "autor": autor,
            "ano": ano,
            "disponivel": disponivel.capitalize()
        }

        lista.append(novo_livro)

        print("Livro cadastrado com sucesso!")

    except ValueError:
        print("Erro! Digite numeros validos.")


def listar(lista):
    print("\n--- LIVROS CADASTRADOS ---")

    if len(lista) == 0:
        print("Nenhum livro cadastrado.")
        return

    for livro in lista:
        print("-------------------------")
        print("Codigo:", livro["codigo"])
        print("Titulo:", livro["titulo"])
        print("Autor:", livro["autor"])
        print("Ano:", livro["ano"])
        print("Disponivel:", livro["disponivel"])

    print("-------------------------")


def buscar_indice(lista, codigo):
    for i in range(len(lista)):
        if lista[i]["codigo"] == codigo:
            return i

    return -1


def buscar(lista):
    print("\n--- BUSCAR LIVRO ---")
    print("1 - Buscar por codigo")
    print("2 - Buscar por titulo")

    opcao = input("Escolha como deseja buscar: ")

    indice = -1

    if opcao == "1":
        try:
            codigo = int(input("Digite o codigo: "))
            indice = buscar_indice(lista, codigo)

        except ValueError:
            print("Digite um codigo numerico valido!")
            return

    elif opcao == "2":
        titulo = input("Digite o titulo: ").strip().lower()

        for i in range(len(lista)):
            if lista[i]["titulo"].lower() == titulo:
                indice = i
                break

    else:
        print("Opcao invalida!")
        return

    if indice == -1:
        print("Livro nao encontrado!")

    else:
        print("\nLivro encontrado!")
        print("Codigo:", lista[indice]["codigo"])
        print("Titulo:", lista[indice]["titulo"])
        print("Autor:", lista[indice]["autor"])
        print("Ano:", lista[indice]["ano"])
        print("Disponivel:", lista[indice]["disponivel"])


def remover(lista):
    print("\n--- REMOVER LIVRO ---")

    try:
        codigo = int(input("Codigo do livro que deseja remover: "))

        indice = buscar_indice(lista, codigo)

        if indice == -1:
            print("Livro nao encontrado!")

        else:
            livro = lista.pop(indice)
            print("Livro removido:", livro["titulo"])

    except ValueError:
        print("Digite um codigo numerico valido!")


while True:

    exibir_menu()

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        cadastrar(livros)

    elif opcao == "2":
        listar(livros)

    elif opcao == "3":
        buscar(livros)

    elif opcao == "4":
        remover(livros)

    elif opcao == "5":
        print("Sistema encerrado. Obrigado!")
        break

    else:
        print("Opcao invalida! Escolha de 1 a 5.")
