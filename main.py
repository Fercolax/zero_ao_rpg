from random import randint

lista_npcs = []

player = {
    "nome": "Fernando",
    "level": 1,
    "exp":0,
    "exp_max":30,
    "hp": 100,
    "hp_max": 100,
    "dano": 25,
}

# função que gerar npcs
def criar_npcs(level):
    
    
    
    novo_npc = {
        "nome": f"Monstro #{level}",
        "level": level,
        "dano": 5 * level,
        "hp": 100 * level,
        "hp_max":100 * level,
        "exp": 7 * level,
    }
    return novo_npc
     
#função que gerar vários npcs   
def gerar_npcs(n_npcs):
    
    for x in range(1,n_npcs+1):
        novo_npc = criar_npcs(x)
        lista_npcs.append(novo_npc)
    
        
        
#função que exibe os npcs criados
def exibir_npcs():
    for npc in lista_npcs:
        exibir_npc(npc)
               

def exibir_npc(npc):
    print(f"Nome: {npc['nome']} // Level: {npc['level']} // Dano: {npc['dano']} // HP: {npc['hp']} // EXP: {npc['exp']}")
    
def exibir_player():
     print(f"Nome: {player['nome']} // Level: {player['level']} // Dano: {player['dano']} // HP: {player['hp']} / {player['hp_max']} // EXP: {player['exp']} / {player['exp_max']}")
    
def reset_player():
    player['hp'] = player['hp_max']
    
def reset_npc(npc):
    npc['hp'] = npc['hp_max']
    
def level_up():
    if player['exp'] >= player['exp_max']:
        player['level'] = player['level'] + 1
        player['exp'] = 0
        player['exp_max'] *= 2
        player['hp_max'] += 20
    
    
#inicia a batalha
def iniciar_batalha(npc):
    while player['hp'] > 0 and npc['hp'] > 0:
        atacar_npc(npc)
        atacar_player(npc)
        exibir_info_batalha(npc)
    if player['hp'] > 0:
        print(f"{player['nome']} venceu e ganhou {npc['exp']} de EXP!!!")
        player['exp'] += npc['exp']
        exibir_player()
    else:
        print(f"O {npc['name']} venceu!\n")
        print("GAME Over!!!")
        exibir_npc(npc)
    level_up()
    reset_player()
    reset_npc(npc)
    
    
# atacar npc será: o hp do npc - dano do player    
def atacar_npc(npc):
    npc['hp'] = npc['hp'] - player['dano']
    
# atacar o player - inverter a função de atacar o npc
def atacar_player(npc):
    player['hp'] = player['hp'] - npc['dano']
    
    
#função de info da batalha

def exibir_info_batalha(npc):
    print(f"Player:{player['nome']} // {player['hp']} / {player['hp_max']}")
    print(f"NPC: {npc['nome']} // { npc['hp']} / {npc['hp_max']}")
    print('------------------------\n')
    

gerar_npcs(5)
exibir_npcs()

exibir_player()
npc_selecionado = lista_npcs[0]
iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado)

exibir_player()

