# ==========================================
# Global Solution - Python 1º Semestre
# ==========================================
captacoes = []
recebimentos = []


def sobre_projeto():
    print("========================================" +
    "\nO PROJETO" + 
    "\n========================================")

    print("Este projeto simula o funcionamento de um sistema de energia solar espacial. Nele, um satélite capta energia "
    "\npor meio de painéis solares e transmite essa energia para uma estação terrestre. O programa registra os dados " \
    "\ninformados pelo usuário, calcula a eficiência da transmissão e permite simular situações de falha."
    "\nTambém são apresentados relatórios com informações sobre o desempenho do sistema."
    "\nA proposta busca relacionar tecnologia, sustentabilidade e aplicações da indústria espacial.")

    

def ler_valor_positivo(mensagem):
    while True:
        try:
            valor = float(input(mensagem))

            if valor < 0:
                print("\nERRO: Digite um valor positivo.")
            else:
                return valor

        except ValueError:
            print("\nERRO: Digite apenas números.")



def registrar_captacao():
    print("========================================"
    "\nREGISTRO DE ENERGIA CAPTADA"
    "\n========================================")

    print("Informe a energia gerada pelos painéis solares."
    "\nUnidade utilizada: Watts (W)"
    "\nExemplos: 250 | 500.5 | 1000\n")

    energia = ler_valor_positivo(
        "Digite a energia captada pelo satélite (W): "
    )

    captacoes.append(energia)

    print(f"\nRegistro salvo com sucesso: {energia:.2f} W")
    


def registrar_recebimento():
    print("========================================"
    "\nREGISTRO DE ENERGIA RECEBIDA"
    "\n========================================")

    print("Informe a energia recebida pela estação terrestre."
    "\nUnidade utilizada: Watts (W)"
    "\nExemplos: 200 | 450.5 | 900\n")

    energia = ler_valor_positivo(
        "Digite a energia recebida na Terra (W): "
    )

    recebimentos.append(energia)

    print(f"\nRegistro salvo com sucesso: {energia:.2f} W")



def calcular_eficiencia(captada, recebida):
    return (recebida / captada) * 100



def mostrar_eficiencia():
    print("========================================"
    "\nCÁLCULO DE EFICIÊNCIA"
    "\n========================================")

    if len(captacoes) == 0 or len(recebimentos) == 0:
        print("\nNão existem registros suficientes.")
        
        return

    captada = captacoes[-1]
    recebida = recebimentos[-1]

    eficiencia = calcular_eficiencia(captada, recebida)

    print(f"\nEnergia captada : {captada:.2f} W"
    f"\nEnergia recebida: {recebida:.2f} W"
    f"\nEficiência: {eficiencia:.2f}%")

    

def simular_falha():
    print("========================================"
    "\nSIMULAÇÃO DE FALHAS"
    "\n========================================")

    print("1 - Nuvens densas"
    "\n2 - Desalinhamento do laser"
    "\n3 - Detrito espacial")

    opcao = input("\nEscolha uma opção: ")

    match opcao:
        case "1":
            perda = 10
            descricao = "Nuvens densas"

        case "2":
            perda = 30
            descricao = "Desalinhamento do laser"

        case "3":
            perda = 50
            descricao = "Detrito espacial"

        case _:
            print("\nOpção inválida.")
            
            return

    print(f"\nFalha simulada: {descricao}"
    f"\nPerda estimada de eficiência: {perda}%")

    

def relatorio():
    print("========================================"
    "\nRELATÓRIO GERAL"
    "\n========================================")

    if len(captacoes) == 0:
        print("\nNenhum registro de energia captada.")
    else:
        print("\nENERGIA CAPTADA"
        "\n------------------------------")

        for valor in captacoes:
            print(f"{valor:.2f} W")

        media_captada = sum(captacoes) / len(captacoes)

        print(f"\nQuantidade: {len(captacoes)}"
        f"\nMaior valor: {max(captacoes):.2f} W"
        f"\nMenor valor: {min(captacoes):.2f} W"
        f"\nMédia: {media_captada:.2f} W")

    if len(recebimentos) == 0:
        print("\nNenhum registro de energia recebida.")
    else:
        print("\nENERGIA RECEBIDA")
        print(f"\n------------------------------")

        for valor in recebimentos:
            print(f"{valor:.2f} W")

        media_recebida = sum(recebimentos) / len(recebimentos)

        print(f"\nQuantidade: {len(recebimentos)}"
        f"\nMaior valor: {max(recebimentos):.2f} W"
        f"\nMenor valor: {min(recebimentos):.2f} W"
        f"\nMédia: {media_recebida:.2f} W")

    

def mostrar_menu():
    print("========================================"
    "\nCENTRO DE CONTROLE DE ENERGIA ESPACIAL"
    "\n========================================")

    print("1 - Sobre o projeto"
    "\n2 - Registrar energia captada"
    "\n3 - Registrar energia recebida"
    "\n4 - Calcular eficiência"
    "\n5 - Simular falha"
    "\n6 - Relatório geral"
    "\n0 - Encerrar")


while True:
    mostrar_menu()

    opcao = input("\nDigite a opção desejada: ")

    match opcao:
        case "1":
            sobre_projeto()

        case "2":
            registrar_captacao()

        case "3":
            registrar_recebimento()

        case "4":
            mostrar_eficiencia()

        case "5":
            simular_falha()

        case "6":
            relatorio()

        case "0":
            print("\nSistema encerrado.")
            break

        case _:
            print("\nOpção inválida.")
