#Define o grafo com cidades e os custos
grafo = {
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Dobreta': 75},
    'Dobreta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Dobreta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Sibiu': {'Oradea': 151, 'Arad': 140, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}


def busca_menor_custo(grafo, origem, destino):#retorna a solução ou falha
    #vai receber minha cidade de origem
    borda = [origem]


    #inicializa o vetor vizitado vazio
    vizitado = []


    #inicializa o custo sendo 0
    custo = {origem: 0}


   
    caminho = {origem: [origem]}


    #loop
    while borda:
        #identifico o primeiro no e tiro da borda
        no = borda.pop(0)
        #se o no nao for vizitado
        if no not in vizitado:
            #se o no for o objetivo final ele para
            if no == destino:
                return caminho[no], custo[no]
            #caso ele nao for o objetivo
            #marca ele como vizitado e adiciona os proximos caminhos
            vizitado.append(no)


            #expandir
            for vizinho in grafo[no]:
                #se o custo nao estiver no grafo ou precisar ser atualizado
                #pelo novo caminho ser menor
                if vizinho not in custo or custo[vizinho] > custo[no] + grafo[no][vizinho]:
                    #atualiza o custo
                    custo[vizinho] = custo[no] + grafo[no][vizinho]
                    #atualiza o caminho
                    caminho[vizinho] = caminho[no] + [vizinho]
                    #adiciona o vizinho na borda
                    borda.append(vizinho)
                #oedena a borda pelo custo
                borda = sorted(borda, key=lambda x: custo[x])
               
    #se nao encontra retorna falso
    return False


print("Digite a cidade de origem: ")
origem = input()
print("Digite a cidade de destino: ")
destino = input()
print (busca_menor_custo(grafo, origem, destino))
