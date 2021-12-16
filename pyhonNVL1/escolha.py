import jogo_da_velha
import jogo
print("Escolha (1) jogo da sorte e (2) joga da velha")
jogar = int(input("Qual jogo escolheu? "))

if jogar == 1:
    jogo.sorte()
elif jogar == 2:
    jogo_da_velha.velha()
else:
    print("Deu erro ;(")
