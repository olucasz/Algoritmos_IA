#Define o grafo
grafo = {
    'Oradea': ['Zerind', 'Sibiu'],
    'Zerind': ['Oradea', 'Arad'],
    'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Dobreta'],
    'Dobreta': ['Mehadia', 'Craiova'],
    'Craiova': ['Dobreta', 'Rimnicu Vilcea', 'Pitesti'],
    'Sibiu': ['Oradea', 'Arad', 'Fagaras', 'Rimnicu Vilcea'],
    'Rimnicu Vilcea': ['Sibiu', 'Craiova', 'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Urziceni', 'Iasi'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
}

def dfs(grafo, origem, destino, visitado=None, parentes=None):
    if visitado == None:    
        visitado = [origem]
    if parentes == None:
        parentes = {}

    
    for vizinho in grafo[origem]:
        if vizinho not in visitado:
            visitado.append(vizinho)
            parentes[vizinho] = origem
            if vizinho == destino:
                return parentes
            resultado = dfs(grafo, vizinho, destino, visitado, parentes)
            if resultado != False:
                return resultado
    return False





origem = 'Neamt'
objetivo = 'Eforie'
solucao = dfs(grafo, origem, objetivo)
caminho = [objetivo]
while origem != objetivo:
    caminho.insert(0, solucao[objetivo])
    objetivo = solucao[objetivo]

print("caminho: ", caminho)