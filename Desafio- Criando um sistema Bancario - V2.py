import textwrap

def menu():
        menu =""" \n
        [d] Despositar
        [s] Sacar
        [e] Extrato
        [nc] Nova Conta
        [lc] Listar Contas
        [nu] Novo Usuário
        [f] Finalizar
        =>"""
        return input(textwrap.dedent(menu))

def depositar(saldo, valor_despositado, extrato, /):
    if valor_despositado > 0:
        saldo += valor_despositado
        extrato += f"Depósito:R$ {valor_despositado:.2f}\n"
        
    else:
      print("Valor digitado é inválido.")

    return saldo, extrato

def sacar(*, saldo, valor_sacado, extrato, limite, saques_realizados, limite_saques):
    sem_saldo = valor_sacado > saldo
    sem_limite = valor_sacado > limite
    excedeu_saques = saques_realizados == limite_saques

    if sem_saldo:
        print("Você não tem saldo suficiente.")

    elif sem_limite:
        print("O valor do saque é maior do que o seu limite.")
        
    elif excedeu_saques:
        print("Você antingiu o seu limites de saques.")
         
    elif valor_sacado > 0:
        saldo -= valor_sacado
        extrato += f"Saque:R$ {valor_sacado: .2f}\n"
        saques_realizados += 1
        
    else:
        print("O valor informado é inválido.")

    return saldo, extrato, saques_realizados

def exibir_extrato(saldo, /, *, extrato):
        print("\n##########-EXTRATO-##########") 
        print("Não foram encontradas movimentações financeiras."if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n#############################")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtar_usuario(cpf, usuarios)

    if usuario:
        print("\n !!! Já existe usuário com esse CPF! !!!")
        return
    nome =input("Informa o nome completo: ")
    data_nascimento = input("Informa o sua data de nascimento (dd-mm-aa) : ")
    endereco = input("Informa o seu endereço (logradouro, número - bairro - cidade/sigla estado): ")
    usuarios.append({"nome":nome, "data de nascimento": data_nascimento, "cpf": cpf, "endereco":endereco})
    print("=== Usuário criado com sucesso! ===")

def filtar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return  usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n !!! Usuário não encontrado, fluxo de criação de conta encerrado! !!!")
    return  None

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():

    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ""
    saques_realizados = 0
    usuarios =[]
    contas =[]

    while True:

        opcao = menu()

        match opcao:
            case "d":
                valor_despositado = float(input("Informe o valor que deseja depositar:"))
                saldo, extrato =  depositar(saldo, valor_despositado, extrato)

            case "s":
                valor_sacado =  float(input("Informe o valor que deseja sacar:"))
                saldo, extrato,saques_realizados = sacar(saldo = saldo, valor_sacado = valor_sacado, extrato = extrato, limite = limite,
                                        saques_realizados = saques_realizados, limite_saques = LIMITE_SAQUES)

            case "e":
                exibir_extrato(saldo, extrato=extrato)

            case "nc":
                numero_conta = len(contas) + 1
                conta = criar_conta(AGENCIA, numero_conta, usuarios)

                if conta:
                    contas.append((conta))
                    numero_conta += 1

            case "lc":
                listar_contas(contas)

            case "nu":
                criar_usuario(usuarios)
                
            case "f":
                break
            
            case default:
                print("Operação inválida. Por favor escolha outra opções.")

main()