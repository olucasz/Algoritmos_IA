#(i j k) → i(Menor disco); j(Intermediario); k(Maior disco)
# 1º Expandir os valores de i. Por exemplo: (1,1,1) = [(2(i+1),1,1),(3(i+2),1,1)] 
# 2º Expadir os valores de j, onde SE j==i, não expande. Além disso os a expansão também não pode ser igual a i
# 3º Expadir os valores de k, onde SE k==i e k==j, não expande.Além disso os a expansão também não pode ser igual a i nem igual a j

import networkx as nx

grafo = nx.Graph()


def grafo_hanoi(n_discos):
    for i in range(1, n_discos+1):
        for j in range(1, n_discos+1):
            for k in range(1, n_discos+1):
                for l in range(1, n_discos+1):
                    for m in range(1, n_discos+1):
                      aux=1
                      while aux < 4:
                          if aux!=i:
                              grafo.add_edge((i, j, k, l, m), (aux, j, k, l, m))
                          if aux!=j:
                              if j!=i:
                                  if aux!=i:
                                      grafo.add_edge((i, j, k, l, m), (i, aux, k, l, m))
                          if aux!=k:
                              if k!=i and k!=j:
                                  if aux!=i and aux!=j:
                                      grafo.add_edge((i, j, k, l, m), (i, j, aux, l, m))
                          if aux!=l:
                              if l!=i and l!=j and l!=k:
                                  if aux!=i and aux!=j and aux!=k:
                                      grafo.add_edge((i, j, k, l, m), (i, j, k, aux, m))
                          if aux!=m:
                              if m!=i and m!=j and m!=k and m!=l:
                                  if aux!=i and aux!=j and aux!=k and aux!=l:
                                      grafo.add_edge((i, j, k, l, m), (i, j, k, l, aux))
                          aux+=1
    return grafo

def busca_em_extensão(grafo, inicio, objetivo):
    #Define a fila de busca
    fila = [inicio]

    #Define os nós visitados
    visitados = [inicio]

    #Define o caminho a percorrer
    parentes = {}

    #Enquanto a fila não estiver vazia
    while fila:
        no = fila.pop(0)

        if no == objetivo:
            caminho = [objetivo]

            while objetivo != inicio:
                caminho.insert(0, parentes[objetivo])
                objetivo = parentes[objetivo]
            return caminho

        #Para cada vizinho do nó
        for vizinho in grafo[no]:
            if vizinho not in visitados:
                #Adiciona o nó como visitado
                visitados.append(vizinho)

                #Adiciona na fila
                fila.append(vizinho)

                #Adiciona o pai do vizinho sendo o nó
                parentes[vizinho] = no

    return False

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

def ldfs(grafo, origem, destino, limite,visitado=None, parentes=None, profundidade=0):
    if visitado == None:    
        visitado = [origem]
    if parentes == None:
        parentes = {}
    if profundidade == limite:
        return False

    for vizinho in grafo[origem]:
        if vizinho not in visitado:
            visitado.append(vizinho)
            parentes[vizinho] = origem
            if vizinho == destino:
                return parentes
            resultado = ldfs(grafo, vizinho, destino, limite, visitado, parentes, profundidade+1)
            if resultado != False:
                return resultado
            visitado.remove(vizinho)
    return False

def ids(grafo, origem, destino, limite):
    for i in range(limite):
        resultado = ldfs(grafo, origem, destino, i)
        if resultado != False:
            return resultado
    return False

def grafo_to_dict(grafo):
    return nx.to_dict_of_lists(grafo)

def main():
    grafo_hanoi(3)
    dic = grafo_to_dict(grafo)
    
    origem = (1,1,1,1,1)
    objetivo = (3,3,3,3,3)

    # Busca em extensão
    print("Busca em Extensão: ", busca_em_extensão(dic, origem, objetivo))

main()