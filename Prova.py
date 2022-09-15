#Exercicio01

#n = int(input("Digite: "))
#n1 = int(input("Digite: "))
#n2 = int(input("Digite: "))

#if n > n1 > n2:
#    print(f"O maior numero é {n}")
#elif n1 > n > n2:
#    print(f"O maior numero é {n1}")
#elif n2 > n1 > n:
#    print(f"O maior numero é {n2}")
#elif n > n2 > n1:
#    print(f"O maior numero é {n}")
#elif n1 > n2 > n:
#    print(f"O maior numero é {n1}")
#elif n2 > n > n1:
#    print(f"O maior numero é {n2}")

#Exercico02

#idade = int(input("Digite: "))
#tempo = int(input("Quanto tempo você trabalhou: "))

#if idade >= 65:
#    print("Você ja pode se aponsentar.")
#elif tempo >= 30:
#    print("Você ja pode se aponsentar.")
#elif idade >= 60 and tempo >= 25:
#    print("Você ja pode se aposentar.")
#else:
#    print("Você ainda não pode se aponsentar.")

#Exercicio03

#contador = 0
#while contador != 5:
#    n = str(input("Adivinhe a letra: ")).upper()
#    if n == "V":
#        print("Você ganhou!")
#        contador = 4
#    else:
#        print("Você Errou!")
#    contador += 1

#Exercicio04

#C = 0
#saldo = 0
#while C != 4:
#    print("====================\n"
#          "[1] Consulta Saldo.\n"
#          "[2] Saque.\n"
#          "[3] Depósito.\n"
#          "[4] Sair.")
#    opcao = int(input("Digite uma opção: "))

#    if opcao == 1:
#        print(f"Seu saldo é de {saldo}.")
#    elif opcao == 2:
#        saque = float(input("Qunato você quer sacar: "))
#        if saldo < saque:
#            print("Saldo insuficiente.")
#            print(f"Seu saldo é de {saldo}.")
#        else:
#            saldo = saldo - saque
#            print(f"Agora seu saldo é de {saldo}.")
#    elif opcao == 3:
#        deposito = float(input("Quanto você quer depositar: "))
#        saldo = saldo + deposito
#        print(f"Agora seu saldo é de {saldo}.")
#    elif opcao == 4:
#        print("Saindo do programa!")
#        C = 4
#    else:
#        print("Numero invalido!")