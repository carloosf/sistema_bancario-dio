def deposito(val, ext, saldo):
    saldo += val
    extrato(ext, val)
    return ext, saldo


def saque(val, ext, saldo, num_saques):
    if num_saques >= 3:
        print("Limite de saques diários atingido.")
        return ext, saldo, num_saques

    if val > 500:
        print("O valor máximo para saque é de R$500.")
        return ext, saldo, num_saques

    if saldo < val:
        print("Saldo insuficiente.")
        return ext, saldo, num_saques

    saldo -= val
    extrato(ext, -val)
    num_saques += 1
    print(f"Saque de R${val} realizado com sucesso.")
    return ext, saldo, num_saques


def extrato(ext, val):
    ext.append(val)
    return ext


ext = []
saldo = 0
num_saques = 0

while True:
    print("\n1: Depósito\n2: Saque\n3: Ver extrato\n4: Sair")
    opt = input("Escolha uma opção: ")

    if opt == "1":
        val = int(input("Insira o valor de depósito: "))
        ext, saldo = deposito(val, ext, saldo)
        print(f"Depósito de R${val} realizado com sucesso. Saldo atual: R${saldo}.")

    elif opt == "2":
        val = int(input("Insira o valor de saque: "))
        ext, saldo, num_saques = saque(val, ext, saldo, num_saques)
        print(f"Saldo atual: R${saldo}.")

    elif opt == "3":
        print("Extrato:", ext)

    elif opt == "4":
        break

    else:
        print("Opção inválida. Tente novamente.")
