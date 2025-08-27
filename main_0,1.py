import random
import time  # Para a animação

# Variáveis globais
wallet = 10  # Saldo inicial
vlr_aposta = 5  # Cada rodada custa 5₢

def dep_cre():
    """Função para depositar créditos na carteira."""
    global wallet
    try:
        deposito = int(input("Quanto deseja depositar? Valor mínimo: 10₢: "))
        if deposito >= 10:
            wallet += deposito
            print(f"Depósito realizado! Saldo atual: {wallet}₢")
        else:
            print("O valor mínimo de depósito é 10₢.")
    except ValueError:
        print("Por favor, insira um valor numérico válido.")

def verificar_premio(matriz, num_rodadas, vlr_aposta):
    """
    Verifica quantas linhas são vencedoras (3 números iguais)
    e calcula o prêmio com base no número de rodadas apostadas.
    """
    premios_por_rodada = {1: 1.2, 2: 1.3, 3: 1.4}
    multiplicador = premios_por_rodada[num_rodadas]

    vitorias = 0
    for linha in matriz:
        if linha[0] == linha[1] == linha[2]:  # Todos os 3 números iguais
            vitorias += 1

    if vitorias > 0:
        premio_base = vitorias * vlr_aposta  # Prêmio base: valor da aposta por linha vencedora
        premio_total = int(premio_base * multiplicador)
        print(f"🎉 {vitorias} linha(s) vencedora(s)! Prêmio multiplicado por {multiplicador}x!")
        return premio_total
    else:
        return 0

def inicio():
    """Função principal para iniciar o jogo."""
    global wallet

    print("Boas-vindas ao 'Macaco Milionário'! 🐵💰")
    print(f"Saldo atual: {wallet}₢")
    print(f"Cada rodada custa {vlr_aposta}₢.")

    # Verificar saldo
    if wallet < vlr_aposta:
        print("Saldo insuficiente para jogar.")
        dep_cre()
        if wallet < vlr_aposta:
            print("Saldo ainda insuficiente. Encerrando...")
            return

    # Escolher número de rodadas
    while True:
        try:
            num_rodadas = int(input("Quantas rodadas deseja apostar? (1 a 3): "))
            if 1 <= num_rodadas <= 3:
                break
            else:
                print("Por favor, escolha entre 1 e 3 rodadas.")
        except ValueError:
            print("Por favor, insira um número válido.")

    # Calcular custo total
    custo_total = num_rodadas * vlr_aposta
    if wallet < custo_total:
        print(f"Saldo insuficiente! Você precisa de {custo_total}₢, mas tem apenas {wallet}₢.")
        dep_cre()
        if wallet < custo_total:
            print("Saldo ainda insuficiente. Encerrando...")
            return

    # Descontar aposta
    wallet -= custo_total
    print(f"Apostas realizadas! {num_rodadas} rodada(s). Custo: {custo_total}₢. Saldo restante: {wallet}₢")

    # Gerar as rodadas (mas ainda não revelar)
    matriz = [[random.randint(1, 9) for _ in range(3)] for _ in range(num_rodadas)]

    # Exibir com animação de raspagem
    print("\n--- Raspando as rodadas... 🎫 Scratching ---")
    time.sleep(1)

    interface_animada(matriz)

    # Verificar prêmio
    premio = verificar_premio(matriz, num_rodadas, vlr_aposta)
    if premio > 0:
        wallet += premio
        print(f"💰 Você ganhou {premio}₢! Novo saldo: {wallet}₢")
    else:
        print("❌ Nenhuma linha vencedora. Tente novamente!")

def interface_animada(matriz):
    """Exibe a animação de raspagem para cada linha."""
    for i, linha in enumerate(matriz):
        print(f"Rodada {i+1}: ", end="", flush=True)
        time.sleep(0.5)
        
        # Mostrar cada número com um pequeno atraso
        for j, num in enumerate(linha):
            if j > 0:
                print(" | ", end="", flush=True)
            print("?", end="", flush=True)
            time.sleep(0.3)
            # Apagar o ? e mostrar o número (simulação simples)
            print("\b\b" + str(num), end="", flush=True)
            time.sleep(0.5)
        print()  # nova linha após cada rodada
    print("-------------------------------")

# === Programa Principal ===
if __name__ == "__main__":
    while True:
        inicio()
        continuar = input("Deseja jogar novamente? (s/n): ").strip().lower()
        if continuar != 's':
            print(f"Obrigado por jogar! Saldo final: {wallet}₢. Até a próxima! 🐵")
            break
