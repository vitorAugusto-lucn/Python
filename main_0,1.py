import random
import time

# Variáveis globais
wallet = 0  # Começa com 0, o jogador precisa depositar
taxa_de_vitoria = 0.3  # 30% de chance de vitória
custo_temporario = None  # Para ofertas especiais

def dep_cre():
    """Função para depositar créditos na carteira (valor mínimo: 5₢)"""
    global wallet
    while wallet < 5:  # Garante que o depósito seja suficiente para pelo menos uma aposta
        try:
            deposito = int(input("Quanto deseja depositar? (mínimo 5₢): "))
            if deposito >= 5:
                wallet += deposito
                print(f"✅ Depósito de {deposito}₢ realizado! Saldo atual: {wallet}₢")
                break
            else:
                print("❌ O valor mínimo de depósito é 5₢.")
        except ValueError:
            print("❌ Por favor, insira um número válido.")

def escolher_aposta():
    """Permite ao jogador escolher o valor da aposta por rodada (mínimo 5₢)"""
    while True:
        try:
            aposta = int(input("Quanto deseja apostar por rodada? (mínimo 5₢): "))
            if aposta < 5:
                print("❌ A aposta mínima por rodada é 5₢.")
            elif aposta > wallet:
                print(f"❌ Saldo insuficiente! Você tem {wallet}₢.")
            else:
                return aposta
        except ValueError:
            print("❌ Por favor, insira um número válido.")

def gerar_matriz_controlada(num_rodadas):
    """
    Gera as linhas com controle de sorte:
    - 30% de chance de ter pelo menos 1 linha vencedora
    """
    tem_vitoria = random.random() < taxa_de_vitoria
    matriz = []

    for i in range(num_rodadas):
        if tem_vitoria and i == 0:
            num = random.randint(1, 9)
            linha = [num, num, num]
            tem_vitoria = False
        else:
            linha = [random.randint(1, 9) for _ in range(3)]
            # Evita vitória acidental se não for sorteada
            while linha[0] == linha[1] == linha[2]:
                linha = [random.randint(1, 9) for _ in range(3)]
        matriz.append(linha)
    
    return matriz

def verificar_premio(matriz, num_rodadas, vlr_aposta):
    """Verifica linhas vencedoras e calcula prêmio com multiplicador"""
    premios_por_rodada = {1: 1.2, 2: 1.3, 3: 1.4}
    multiplicador = premios_por_rodada[num_rodadas]

    vitorias = 0
    for linha in matriz:
        if linha[0] == linha[1] == linha[2]:
            vitorias += 1

    if vitorias > 0:
        premio_base = vitorias * vlr_aposta
        premio_total = int(premio_base * multiplicador)
        print(f"🎉 {vitorias} linha(s) vencedora(s)! Prêmio multiplicado por {multiplicador}x!")
        return premio_total
    else:
        return 0

def interface_animada(matriz):
    """Exibe a animação de raspagem para cada linha."""
    print("\n--- Raspando as rodadas... 🎫 Scratching ---")
    time.sleep(1)

    for i, linha in enumerate(matriz):
        print(f"Rodada {i+1}: ", end="", flush=True)
        time.sleep(0.5)
        
        for j, num in enumerate(linha):
            if j > 0:
                print(" | ", end="", flush=True)
            print("?", end="", flush=True)
            time.sleep(0.3)
            print("\b\b" + str(num), end="", flush=True)
            time.sleep(0.4)
        print()
    print("-------------------------------")

def inicio():
    """Função principal para iniciar o jogo."""
    global wallet, custo_temporario

    print("💰 === Boas-vindas ao 'Macaco Milionário'! === 💰")
    print(f"Saldo atual: {wallet}₢")

    # Se o jogador está usando uma oferta especial de aposta baixa
    aposta_atual = custo_temporario if custo_temporario else None

    # Oferecer depósito se necessário
    if wallet < 5:
        print("💳 Você precisa de créditos para jogar.")
        dep_cre()

    # Permitir que o jogador escolha o valor da aposta
    if aposta_atual:
        usar_oferta = input(f"Oferta ativa: apostar por {aposta_atual}₢ nesta rodada? (s/n): ").strip().lower()
        if usar_oferta == 's':
            vlr_aposta = aposta_atual
            print(f"✅ Aposta definida para {vlr_aposta}₢ (oferta especial).")
        else:
            vlr_aposta = escolher_aposta()
    else:
        vlr_aposta = escolher_aposta()

    # Número de rodadas
    while True:
        try:
            num_rodadas = int(input(f"Quantas rodadas deseja apostar? (1 a 3) Custo total: {vlr_aposta * num_rodadas}₢: "))
            if 1 <= num_rodadas <= 3:
                custo_total = num_rodadas * vlr_aposta
                if custo_total > wallet:
                    print(f"❌ Saldo insuficiente! Você precisa de {custo_total}₢, mas tem {wallet}₢.")
                else:
                    break
            else:
                print("❌ Escolha entre 1 e 3 rodadas.")
        except ValueError:
            print("❌ Por favor, insira um número válido.")

    # Descontar aposta
    wallet -= custo_total
    print(f"🎟️ Apostas realizadas! {num_rodadas} rodada(s). Custo: {custo_total}₢. Saldo restante: {wallet}₢")

    # Gerar e revelar resultados
    matriz = gerar_matriz_controlada(num_rodadas)
    interface_animada(matriz)

    # Verificar prêmio
    premio = verificar_premio(matriz, num_rodadas, vlr_aposta)
    if premio > 0:
        wallet += premio
        print(f"💰 Você ganhou {premio}₢! Novo saldo: {wallet}₢")
    else:
        print("❌ Nenhuma linha vencedora. Tente novamente!")

    # Resetar oferta após uso
    if custo_temporario and usar_oferta == 's':
        print(f"➡️ Oferta usada. Aposta voltou ao valor normal a partir da próxima.")
        custo_temporario = None

# === Programa Principal ===
if __name__ == "__main__":
    # Primeiro depósito inicial
    if wallet == 0:
        print("💳 Para começar, faça seu primeiro depósito!")
        dep_cre()

    while True:
        inicio()
        continuar = input("Deseja jogar novamente? (s/n): ").strip().lower()
        if continuar != 's':
            print("❌ Nenhuma linha vencedora. Tente novamente!")
            oferta = input("Você está desistindo? Que tal tentar por 2₢ na próxima rodada? (s/n): ").strip().lower()
            if oferta == 's' and wallet >= 2:
                custo_temporario = 2
                print("✅ Ótimo! Na próxima rodada, você poderá apostar por apenas 2₢. Boa sorte! 🍀")
            elif oferta == 's' and wallet < 2:
                print("❌ Saldo insuficiente para oferta. Depósito necessário.")
                dep_cre()
                if wallet >= 2:
                    custo_temporario = 2
                    print("✅ Oferta ativada! Próxima aposta por 2₢.")
                else:
                    print("➡️ Continue jogando normalmente.")
            else:
                print("Obrigado por jogar! Até a próxima! 🐵")
            break