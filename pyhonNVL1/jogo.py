from random import sample, randint

escolha = int(input("Digite 1 para escolher seus números, aperte 2 para ser aleatorio: "))
tentativas = 3
if escolha == 1:
    quantidades_numeros = input("Escolha os números para serem sotiados(use virgulas) ")
    quantidades_numeros = quantidades_numeros.split(",")
    numeros = []
    for n in quantidades_numeros:
        numeros_sortiados = int(n.strip())
        numeros.append(numeros_sortiados)
        
    sortiado = sample(numeros,1)
    for rodada in range(1,tentativas + 1):
        print(f"tentativa {rodada} de {tentativas}")
        numero_escolhido = int(input("Adivinhe um número entre os números sotiados\n"))
        if (numero_escolhido < 1 or numero_escolhido > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue
        if sortiado[0] == numero_escolhido:
            print(f"Meus parabens o numero sortiado foi {sortiado[0]}")
            break
        else:
            print("*=-"*10)
            print("Você errou tente de novo")
            if sortiado[0] > numero_escolhido:
                print("O número sortedo é maior")
            elif sortiado[0] < numero_escolhido:
                print("O número sorteado é menor")
            print("*=-"*10)
elif escolha == 2:
    numero = randint(1,50)
    print(numero)
    for rodada in range(1, tentativas + 1):
        print(f"Tentativa {rodada} de {tentativas}")
        escolher_numero = int(input("Escolha um número entre 1 a 50: "))
        if escolher_numero < 1 or escolher_numero > 50:
            print("Você deve digitar um número entre 1 e 100!")
            continue
        if numero == escolher_numero:
            print(f"Meus parabens o numero sortiado foi {numero}")
            break
        else:
            print("*=-"*10)
            print("Você errou tente de novo")
            if numero > escolher_numero:
                print("O número sortedo é maior")
            elif numero < escolher_numero:
                print("O número sorteado é menor")
            print("*=-"*10)
        

