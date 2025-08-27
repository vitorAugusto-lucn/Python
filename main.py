import random
deposito = 0
wallet = 0
saldo_atual = 10

def dep_cre():
    int(input("Quanto deseja depositar? Valor minimo: 10₢", deposito))
    wallet = deposito
    if wallet >= deposito:
        print("Saldo em carteira: ", wallet)
    else:
        wallet < saldo_atual
        print("Saldo insuficiente, adicione mais creditos!")

def inicio():
    print("Boas Vindas ao 'Macaco Milionário!', para começar faça o depósito!")
    print(dep_cre)
    print("Cada rodada custa", vlr_aposta, "₢")
    vlr_aposta = 20 // wallet
    
    rodadas = []
    
    int(input("Quantas rodadas deseja apostar? Gera ate 3 rodadas.", rodadas[3]))
    if rodadas < 3:
        print("O máximo de rodadas é 3(três).")
    else:
        print("Valor da sua aposta", vlr_aposta * rodadas)

    wallet - vlr_aposta
    
def interface():    
    
    rodadas = []
    
    if rodadas[1]:
        print(f" {[0]} | {[0]} | {[0]} "), random 
    if rodadas[2]:
        print(f" {[0]} | {[0]} | {[0]} "), random
        print(f" {[0]} | {[0]} | {[0]} "), random
    if rodadas[3]:
        print(f" {[0]} | {[0]} | {[0]} "), random
        print(f" {[0]} | {[0]} | {[0]} "), random
        print(f" {[0]} | {[0]} | {[0]} "), random    




            
