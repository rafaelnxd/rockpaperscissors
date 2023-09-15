8import random


user_action = input("Digite a sua escolha (Pedra, Papel ou Tesoura):")
possible_actions = ['Pedra','Papel','Tesoura']
computer_action=random.choice(possible_actions)
print(f"\nVocê escolheu {user_action}, Computador escolheu {computer_action}.\n")

if user_action == computer_action:
    print(f'Ambos os jogadores selecionara {user_action}, é empate')
elif user_action == "Pedra":
    if computer_action == "Tesoura":
        print(f'Pedra ganha de tesoura, você venceu!')
    else:
        print(f'Pedra perde de papel, você perdeu')
elif user_action == "Papel":
    if computer_action == "Pedra":
        print(f'Papel ganha de pedra, você venceu!')
    else:
        print(f'Papel perde de tesoura, você perdeu!')
elif user_action == "Tesoura":
    if computer_action == "Papel":
        print(f'Tesoura ganha de papel, você venceu')
    else:
        print(f'Tesoura perde de Pedra, você perdeu')


        def classifica_numero(numero):
    if numero > 0:
        if numero % 2 == 0:
            return "Positivo e Par"
        else:
            return "Positivo e Ímpar"
    elif numero < 0:
        if numero % 2 == 0:
            return "Negativo e Par"
        else:
            return "Negativo e Ímpar"
    else:
        return "Zero"

# Exemplos de uso:
print(classifica_numero(5))  # Isso imprimirá "Positivo e Ímpar"
print(classifica_numero(-2))  # Isso imprimirá "Negativo e Par"
print(classifica_numero(0))  # Isso imprimirá "Zero"







    
    
        


