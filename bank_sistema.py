# Desafio Python - Sistema Bancário
# Produzido por Eric Quevedo Silva (github.com/ericquevesil)

import datetime

def main():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """
    
    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3
    TAXA_SAQUE = 1.50  # Taxa por saque para monetização

    while True:
        opcao = input(menu).strip().lower()

        if opcao == "d":
            try:
                valor = float(input("Informe o valor do depósito: "))
                if valor > 0:
                    saldo += valor
                    extrato.append((datetime.datetime.now(), "Depósito", valor, None))
                    print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
                else:
                    print("Operação falhou! O valor informado é inválido.")
            except ValueError:
                print("Operação falhou! Valor inválido. Digite apenas números.")

        elif opcao == "s":
            try:
                valor = float(input("Informe o valor do saque: "))
                
                excedeu_saldo = valor > saldo
                excedeu_limite = valor > limite
                excedeu_saques = numero_saques >= LIMITE_SAQUES
                valor_total = valor + TAXA_SAQUE

                if excedeu_saldo:
                    print(f"Operação falhou! Você não tem saldo suficiente. Saldo atual: R$ {saldo:.2f}")
                elif excedeu_limite:
                    print(f"Operação falhou! O valor do saque excede o limite de R$ {limite:.2f}.")
                elif excedeu_saques:
                    print("Operação falhou! Número máximo de saques excedido.")
                elif valor > 0:
                    if saldo >= valor_total:
                        saldo -= valor_total
                        numero_saques += 1
                        extrato.append((datetime.datetime.now(), "Saque", valor, TAXA_SAQUE))
                        print(f"Saque de R$ {valor:.2f} realizado com sucesso! Taxa: R$ {TAXA_SAQUE:.2f}")
                    else:
                        print(f"Operação falhou! Saldo insuficiente para cobrir saque + taxa. Saldo necessário: R$ {valor_total:.2f}")
                else:
                    print("Operação falhou! O valor informado é inválido.")
            except ValueError:
                print("Operação falhou! Valor inválido. Digite apenas números.")

        elif opcao == "e":
            print("\n" + "=" * 40 + " EXTRATO " + "=" * 40)
            if not extrato:
                print("Não foram realizadas movimentações.")
            else:
                print(f"{'Data/Hora':<20} {'Operação':<10} {'Valor (R$)':>15} {'Taxa (R$)':>15}")
                print("-" * 60)
                for movimento in extrato:
                    data, operacao, valor, taxa = movimento
                    print(f"{data.strftime('%d/%m/%Y %H:%M'):<20} {operacao:<10} {valor:>15.2f} {taxa if taxa is not None else 0:>15.2f}")
            print("\n" + "-" * 60)
            print(f"SALDO ATUAL: R$ {saldo:.2f}".rjust(60))
            print("=" * 88 + "\n")

        elif opcao == "q":
            print("Obrigado por usar nosso sistema bancário. Até mais!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()