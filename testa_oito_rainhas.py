from oito_rainhas import monta

# Caso exista alguma posição de ataque o programa irá retornar 1, caso seja uma solução ao problema das 8 rainhas irá retornar 0, e caso não seja uma entrada válida ao teste o retorno será igual a -1
# Em suma:
# 0 = Não é solução para o problema das 8 rainhas
# 1 = É solução para o problema das 8 rainhas
# -1 = Entrada inválida, ou seja, tabuleiro não é 8x8, possui valores diferentes de 0 e 1, não possui 8 rainhas.

tabuleiro = '00001000','01000000','00010000','00000010','00100000','00000001','00000100','10000000'

def teste():
    assert monta(tabuleiro) == 1 # TABULEIRO COM SOLUÇÃO   
