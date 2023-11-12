import random

def gerar_frase_inicial(tamanho=28):
    return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ ') for _ in range(tamanho))

def realizar_mutacao(frase, taxa_mutacao=0.05):
    return ''.join(
        novo_caractere if random.random() < taxa_mutacao else antigo_caractere
        for antigo_caractere, novo_caractere in zip(frase, gerar_frase_inicial())
    )

def calcular_pontuacao(frase, frase_alvo="METHINKS IT IS LIKE A WEASEL"):
    return sum(1 for a, b in zip(frase, frase_alvo) if a == b)

def algoritmo_weasel():
    frase_alvo = "METHINKS IT IS LIKE A WEASEL"
    melhor_frase = gerar_frase_inicial()
    melhor_pontuacao = 0

    iteracao = 1
    while melhor_pontuacao < len(frase_alvo):
        novas_frases = [realizar_mutacao(melhor_frase) for _ in range(100)]
        
        for nova_frase in novas_frases:
            pontuacao = calcular_pontuacao(nova_frase)
            if pontuacao > melhor_pontuacao:
                melhor_pontuacao = pontuacao
                melhor_frase = nova_frase
        
        print(f"Iteração {iteracao}: {melhor_frase} - Pontuação: {melhor_pontuacao}")
        iteracao += 1

        if melhor_pontuacao == len(frase_alvo):
            break

if __name__ == "__main__":
    algoritmo_weasel()
