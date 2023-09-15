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


def distancia(altura, velocidade_aviao):
    # Convertendo a velocidade do avião de km/h para m/s
    velocidade_aviao_ms = (velocidade_aviao / 3.6)

    # Calculando o tempo de voo usando a fórmula fornecida
    tempo_de_voo = ((2 * altura) / 9.81) ** 0.5

    # Calculando o alcance horizontal usando a fórmula fornecida
    alcance_horizontal = velocidade_aviao_ms * tempo_de_voo

    # Arredondando o alcance para 2 casas decimais
    alcance_horizontal = round(alcance_horizontal, 2)

    return alcance_horizontal

# Exemplo de uso:
altura_em_metros = 1000  # Altura em metros
velocidade_do_aviao_km_h = 500  # Velocidade do avião em km/h

# Chamando a função para calcular o alcance
resultado = distancia(altura_em_metros, velocidade_do_aviao_km_h)
print(f"A bomba percorrerá {resultado} metros até atingir o alvo no solo.")




def hexagono(lado, unidade):
    # Calcula a área do hexágono
    area = (3 * (lado ** 2) * (3 ** 0.5)) / 2

    # Calcula o perímetro do hexágono (a soma dos lados)
    perimetro = 6 * lado

    # Formata os resultados com as unidades de medida
    area_str = f"{area:.1f} {unidade}^2"
    perimetro_str = f"{perimetro} {unidade}"

    # Retorna os resultados em uma única string
    resultado = f"área: {area_str} e perímetro: {perimetro_str}"
    return resultado

# Exemplo de uso:
lado = 4  # Comprimento de um lado
unidade = "cm"  # Unidade de medida

# Chamando a função para calcular área e perímetro
resultado = hexagono(lado, unidade)
print(resultado)



def saque(valor):
    # Inicializa as variáveis para contar as cédulas
    cedulas_50 = 0
    cedulas_20 = 0
    cedulas_10 = 0

    # Calcula a quantidade de cédulas de 50 reais
    while valor >= 50:
        cedulas_50 += 1
        valor -= 50

    # Calcula a quantidade de cédulas de 20 reais
    while valor >= 20:
        cedulas_20 += 1
        valor -= 20

    # Calcula a quantidade de cédulas de 10 reais
    while valor >= 10:
        cedulas_10 += 1
        valor -= 10

    # Cria a string de saída com as quantidades de cédulas
    resultado = f"50: {cedulas_50} 20: {cedulas_20} 10: {cedulas_10}"
    return resultado

# Exemplo de uso:
valor_de_saque = 130  # Valor de saque em reais

# Chamando a função para calcular as cédulas necessárias
resultado = saque(valor_de_saque)
print(resultado)

def saque(valor):
    # Inicializa as variáveis para contar as cédulas
    cedulas_50 = valor // 50
    valor %= 50
    cedulas_20 = valor // 20
    valor %= 20
    cedulas_10 = valor // 10

    # Cria a string de saída com as quantidades de cédulas
    resultado = f"50: {cedulas_50} 20: {cedulas_20} 10: {cedulas_10}"
    return resultado

# Exemplo de uso:
valor_de_saque = 130  # Valor de saque em reais

# Chamando a função para calcular as cédulas necessárias
resultado = saque(valor_de_saque)
print(resultado)

    
        


