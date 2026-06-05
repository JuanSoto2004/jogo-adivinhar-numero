import random

def jogo():
    print("=== Jogo de Adivinhar o Número ===")
    print("Estou a pensar num número entre 1 e 100...")
    
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 10

    while tentativas < max_tentativas:
        tentativas += 1
        print(f"\nTentativa {tentativas}/{max_tentativas}")
        
        try:
            palpite = int(input("O teu palpite: "))
        except ValueError:
            print("Introduz um número válido!")
            tentativas -= 1
            continue

        if palpite < numero_secreto:
            print("📈 Muito baixo!")
        elif palpite > numero_secreto:
            print("📉 Muito alto!")
        else:
            print(f"🎉 Parabéns! Acertaste em {tentativas} tentativas!")
            return

    print(f"\n😢 Perdeste! O número era {numero_secreto}")

jogo()
