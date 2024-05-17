menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[u] Cadastrar Usuário
[c] Cadastrar Conta Bancária
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

usuarios = []
contas = []
numero_conta = 1

def depositar(valor, /):
    if valor > 0:
        return valor, f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Depósito Falhou, valor informado é inválido.")
        return 0, ""
    
def sacar(*, saldo, valor, limite, numero_saques, LIMITE_SAQUES):
    acima_saldo = valor > saldo
    acima_limite = valor > limite
    saque_excedente = numero_saques >= LIMITE_SAQUES

    if acima_saldo:
        print("Saldo insuficiente")
        return 0, ""
    elif acima_limite:
        print("Excede o limite máximo por saque")
        return 0, ""
    elif saque_excedente:
        print("Número máximo de saques excedido.")
        return 0, ""
    elif valor > 0:
        return -valor, f"Saque: R$ {valor:.2f}\n"
    else:
        print("O Valor informado é inválido.")
        return 0, ""

def exibir_extrato(saldo, /, *, extrato):
    print("EXTRATO".center(32, "="))
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("===============================")

def cadastrar_usuario(nome, data_nascimento, cpf, endereco):
    cpf = ''.join(filter(str.isdigit, cpf))  # Remove caracteres não numéricos do CPF
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Erro: CPF já cadastrado.")
            return
    usuarios.append({
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    })
    print(f"Usuário {nome} cadastrado com sucesso.")

def cadastrar_conta(cpf):
    global numero_conta
    usuario = next((usuario for usuario in usuarios if usuario['cpf'] == cpf), None)
    if usuario:
        contas.append({
            'agencia': '0001',
            'numero_conta': numero_conta,
            'usuario': usuario
        })
        print(f"Conta {numero_conta} cadastrada com sucesso para o usuário {usuario['nome']}.")
        numero_conta += 1
    else:
        print("Erro: Usuário não encontrado.")

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor do depósito: "))
        deposito, descricao = depositar(valor)
        saldo += deposito
        extrato += descricao

    elif opcao == "s":
        valor = float(input("Informe o valor a ser sacado: "))
        saque, descricao = sacar(saldo=saldo, valor=valor, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)
        saldo += saque
        extrato += descricao
        if saque != 0:
            numero_saques += 1

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "u":
        nome = input("Nome: ")
        data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
        cpf = input("CPF: ")
        endereco = input("Endereço (logradouro - número - bairro - cidade/estado): ")
        cadastrar_usuario(nome, data_nascimento, cpf, endereco)

    elif opcao == "c":
        cpf = input("Informe o CPF do usuário: ")
        cadastrar_conta(cpf)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
