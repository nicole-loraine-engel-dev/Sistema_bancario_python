#Sistema Financeiro em Python

print("Olá! Bem vindo ao sistema finaneiro Python")
print("Escolha a opção desejada:")

menu = '''

[1] Deposito
[2] Saque
[3] Extrato
[4] Sair

=> '''

#Definições

Saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

#O while se usa para quando irá repetir um bloco de código várias vezes
#Função input() - usa-se para obter entrada do usuário através do terminal, exibe uma mensagem para o usuário, aguarda até que o usuário digite alguma informação e, em seguida, retorna essa entrada como uma string.
#Se escolher a opção 1 - o valor é igual um nº decimal. Depois pergunta o valor
#Se valor é maior que 0, saldo acrescenta valor e extrato pergunta valor do deposito (duas casas decimais em ponto flutuante)    senão printa a operação falhou! 

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito:  "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")   

#Se escolher opção 2, o valor é um flutuante e pergunta o valor do saque
        
    elif opcao == "2":
        valor = float(input("Informe o valor do saque"))

#Excedeu saldo é valor maior que saldo, excedeu limite o valor maior que limite, excedeu saque o numero do saque é maior ou igual o limite de saques

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numero_saques >= limite_saques

#Para cada opção acima, printa uma frase.

        if excedeu_saldo:
            print("A operação falhou! Você não tem saldo o suficiente.")
        
        elif excedeu_limite:
            print("Operação falhou! O valor excede o limite da conta")

        elif excedeu_saque:
            print("Operação falhou! Numero máximo de saques diários excedido")

#Ou se o valor for maior que 0, diminui saldo do valor, o extrato adiciona perguntando o valor do saque (numero com 2 decimais), e o numero de saque somatiza 1.    Senão printa falha
        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("Operação falhou! O valor informado é inválido.")

#Ou opção 3 que printa o extrato e no segundo print com if ternário.
#IF Ternário: Permite escrever uma condição em uma única linha. Composto por três partes, a primeira parte é o retorno caso a expressão retorne verdadeiro, a segunda é a expressão lógica e a terceira é o retorno caso a expressão não seja atendida. 
#if not extrato else extrato > Se o extrato não esta vazio, exibo o que esta dentro da variável de extrato. 

    elif opcao == "3":
        print("\n ................EXTRATO..................")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print("f\nSaldo: R$ {saldo:.2f}")
        print("...........................................")

#opção sair

    elif opcao == "4":
        break

    else:
        print("Operação inválida! Por favor, selecione novamente a opção desejada")