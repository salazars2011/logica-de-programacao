dados_brutos = [
    "  carlos eduardo silva;desenvolvedor;11988887777  ",
    "  ana paula mendes;analista de rh;21977776666  ",
    "  roberto carlos oliveira;gerente de projetos;31966665555  "
]


def limpar_e_formatar_texto(texto):
    texto_formatado = texto.strip().upper()
    return texto_formatado


def extrair_codigo_ou_ddd(dado):
    dado_limpo = dado.strip()
    ddd = dado_limpo[0:2]
    return ddd


def processar_e_exibir_cadastros(lista_dados):
    total = 0

    for item in lista_dados:
        partes = item.split(";")

        nome = limpar_e_formatar_texto(partes[0])
        cargo = limpar_e_formatar_texto(partes[1])
        ddd = extrair_codigo_ou_ddd(partes[2])

        print(f"Nome: {nome}")
        print(f"Cargo: {cargo}")
        print(f"DDD: {ddd}")
        print("-" * 40)

        total += 1

    return total


def main():
    print("==================================================")
    print("     SISTEMA DE GESTÃO MODULARIZADO - AV2")
    print("==================================================\n")

    print("Iniciando o processamento dos dados...\n")

    total_processado = processar_e_exibir_cadastros(dados_brutos)

    print(f"Total de registros processados: {total_processado}")

    print("\n==================================================")
    print("             PROCESSAMENTO CONCLUÍDO")
    print("==================================================")


if __name__ == "__main__":
    main()
