from random import sample
quantidades_numeros = input("Escolha os números para serem sotiados(use virgulas) ")
quantidades_numeros = quantidades_numeros.split(",")
numeros = []
for n in quantidades_numeros:
    numeros_sortiados = int(n.strip())
    numeros.append(numeros_sortiados)
    
tentativas = 3
sortiado = sample(numeros,1)
for rodada in range(1,4):
    print(f"tentativa {rodada} de {tentativas}")
    numero_escolhido = int(input("Adivinhe um número entre os números sotiados\n"))
    if (numero_escolhido < 1 or numero_escolhido > 100):
        print("Você deve digitar um número entre 1 e 100!")
        rodada = rodada - 1
        print(rodada)
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