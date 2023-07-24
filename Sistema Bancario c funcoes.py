limite = 500
saldo = 0
extrato = ""
numero_saques = 0
limite_saques = 3
numero_operacoes = 0

def menu():
    menu = ("""
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] sair
    =>
    """)

    return input(menu)

def depositar(saldo,deposito,extrato):
    if deposito > 0:
        saldo = saldo + deposito
        extrato += f"Deposito: R${deposito:.2f}\n"
        print(f"Deposito no valor de R${deposito:.2f} realizado com sucesso !\n")
        global numero_operacoes
        numero_operacoes += 1

    else:
        print("Valor inválido !")

    return saldo, extrato

while True:

    opcao = menu()

    if opcao == "d":
        deposito = float(input("\nValor do deposito: \n=> "))

        saldo, extrato = depositar(saldo,deposito, extrato)

    elif opcao == "s":
        saque = float(input("Valor do saque: \n=> "))

        if saque > limite:
            print("Saque maior que o limite permitido !\n")

        elif saque <= 0:
            print("Valor abaixo do mínimo, impossivel realizar a transfência !\n")

        elif numero_saques >= limite_saques:
            print("Limite de saques excedido !\n")

        elif saque > saldo:
            print("Você não saldo suficiente !")

        else:
            saldo = saldo - saque
            print(f"\nSaque de R${saque:.2f} realizado com sucesso !\n")
            extrato += f"Saque: R${saque:.2f}\n"
            numero_saques = numero_saques + 1
            numero_operacoes = numero_operacoes + 1

    elif opcao == "e":
        if numero_operacoes > 0:
            print(f"""Extrato bancario:
            \nSaldo: R${saldo}\n{extrato}""")

        else:
            print(f"""Extrato bancario: \nSaldo: R${saldo}
            \nNenhuma operação foi realizada nesta conta até o momento !""")

    elif opcao == "q":
        break

    else:
        print("Operação Invalida !")





