menu = """
[d] Despositar
[s] Sacar
[e] Extrato
[f] Finalizar
=>"""

saldo = 0
limite = 500
extrato = ""
saques_realizados = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    match opcao:
        case "d":
            valor_despositado = float(input("Informe o valor que deseja depositar:"))

            if valor_despositado > 0:
                saldo += valor_despositado
                extrato += f"Depósito:R$ {valor_despositado:.2f}\n"
        
            else:
                print("Valor digitado é inválido.")

        case "s":
            valor_sacado =  float(input("Informe o valor que deseja sacar:"))

            sem_saldo = valor_sacado > saldo
            sem_limite = valor_sacado > limite
            excedeu_saques = saques_realizados == LIMITE_SAQUES

            if sem_saldo:
                print("Você não tem saldo suficiente.")
                continue

            if sem_limite:
                print("O valor do saque é maior do que o seu limite.")
                continue 
        
            if excedeu_saques:
                print("Você antingiu o seu limites de saques.")
                continue
        
            if valor_sacado > 0:
                saldo -= valor_sacado
                extrato += f"Saque:R$ {valor_sacado: .2f}\n"
                saques_realizados += 1
        
            else:
                print("O valor informado é inválido.")

        case "e":
            print("\n##########-EXTRATO-##########") 
            print("Não foram encontradas movimentações financeiras."if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("\n#############################") 

        case "f":
             break
        
        case default:
            print("Operação inválida. Por favor escolha outra opções.")