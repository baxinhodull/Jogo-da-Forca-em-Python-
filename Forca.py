import random

palavras = ["python", "programacao", "computador", "aula", "variavel"]

def jogar_forca():
    palavra_sorteada = random.choice(palavras)

    palavra_escondida = "-" * len(palavra_sorteada)
    letras_adivinhas = []

    max_tentativas = 6

    while True:
        print(f"\nPalavra: {palavra_escondida}")
        print(f"Tentativas restantes: {max_tentativas}")
        
        
        letra = input("Digite uma letra: ").lower()

       
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, digite apenas uma letra.")
            continue

        if letra in letras_adivinhas:
            print("Você já digitou essa letra. Tente outra por favor.")
            continue
        letras_adivinhas.append(letra)

        
        if letra in palavra_sorteada:
            lista = list(palavra_escondida)
            for indice in range(len(palavra_sorteada)):
                if letra == palavra_sorteada[indice]:
                    lista[indice] = letra
            palavra_escondida = "".join(lista)
            print(f"Boa! A letra '{letra}' está na palavra.")
        else:
            max_tentativas -= 1
            print(f"Letra '{letra}' não encontrada. Você tem {max_tentativas} tentativas restantes.")

        
        if palavra_escondida == palavra_sorteada:
            print(f"Parabéns, você ganhou!! A palavra era '{palavra_sorteada}'.")
            break

        
        if max_tentativas == 0:
            print(f"Você perdeu. A palavra era '{palavra_sorteada}'.")
            break

def continuar_jogo():
    while True:
        resposta = input("\nVocê quer jogar novamente? (s/n): ").lower()
        if resposta == "s":
            return True
        elif resposta == "n":
            print("Obrigado por jogar! Até a próxima!")
            return False
        else:
            print("Resposta inválida. Digite 's' para sim ou 'n' para não.")


while True:
    jogar_forca()  
    if not continuar_jogo():  
        break
