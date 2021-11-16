from waypy.agent import Agente
from functions import posicoes

def ligar_os_pontos(coordenadas):
    posicoes = []

    #Calcula as coordenadas para saber a qual quadrado se referem.
    pos1 = ((coordenadas[1] - 1) * 8) + coordenadas[0]
    pos2 = ((coordenadas[3] - 1) * 8) + coordenadas[2]

    posicoes.append(pos1)
    posicoes.append(pos2)

    return posicoes

def buscar_caminho(pontos):
    agente = Agente()
    agente.starting_points = [str(pontos[0])] #ponto de partida
    agente.nodes = posicoes.nos
    agente.graphs = posicoes.arestas

    caminho = agente.encontrar_ajuda_humanitaria(str(pontos[1]), "AMPLITUDE") #ponto final, metodo.

    if type(caminho) != list:
        return False
    else:
        return caminho