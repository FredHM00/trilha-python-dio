menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            

        else:
        
            print("Depósito Falhou, valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor a ser sacado: "))

        acima_saldo = valor > saldo
       
        acima_limite = valor > limite
       
        saque_excedente = numero_saques >= LIMITE_SAQUES
        if acima_saldo:
                print("Saldo insuficiente")
        elif acima_limite:

            print("Excede o limite máximo por saque")  

        elif saque_excedente:
             
             print("Número máximo de saques excedido.") 

        elif valor > 0:

            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
             
             print("O Valor informado é inválido.")            
    
    elif opcao == "e":
        EXTRATO = "EXTRATO"   
        
        print(EXTRATO.center(32, "="))

        print("Não foram realizadas movimentações." if not extrato else extrato)
        
        print(f"\nSaldo: R$ {saldo:.2f}")

        print("===============================")

    elif opcao == "q":

        break

    else:
        
        print("Operação inválida, por favor selecione novamente a operação desejada.")
  
