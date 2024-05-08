saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
limite_saques = 3
saque_total = 0
extrato_depositos = ""
extrato_saques = ""

menu = """

Digite a operção que deseja realizar:

1 - Depositar
2 - Sacar
3 - Extrato
4 - Sair

"""

while True:

    opcao = input(menu)

    if opcao == "1":
    
     valor = float(input("Digite o valor a ser depositado: "))
     if valor > 0:
         saldo += valor
         extrato_depositos += f"Depósito: R$ {valor:,.2f}\n"
         print(f"Valor de R$ {valor:,.2f} depositado com sucesso!")

    elif opcao == "2":
        saque = float(input("Valor a ser sacado:"))
        
        if saque <= saldo:
            if saque > saldo:
               print("Valor indisponivel para saque!")
               
            elif numero_de_saques >= limite_saques:
               print("Limite maximo de saques diarios atingidos!")
        
            elif saque > 500:
               print("Valor maximo para saque é R$500,00")
        
            elif (saque_total + saque) > 1500:
               print("Valor de R$1500,00 de saque diário excedido!")

            else:
               print(f"Valor de R$ {saque:,.2f} sacado com sucesso")
               numero_de_saques +=1
               saldo -= saque
               saque_total += saque
               extrato_saques += f"Saque de:R${saque:,.2f}\n"
        else:
           print("Saldo insuficiente!")
            
    elif opcao == "3":
        if extrato_saques == "" and extrato_depositos == "":
           print("Não foram realizadas movimentações.")

        else:
           print("Depósitos:")
           print(extrato_depositos)
           
           print("Saques:")
           print(extrato_saques)   
        
           print(f"Saldo atual da conta R${saldo:,.2f}")
    
    elif opcao == "4":
        print("Encerrando sistema, obrigado pela preferência")
        break

    else:
        print("Opção invalida!")

