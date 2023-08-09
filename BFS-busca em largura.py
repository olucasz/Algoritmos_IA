def BFS_SP(arvore, partida, destino):
    visitada = []
     
    fila = [[partida]]
     
    if partida == destino:
        print("Você já está nessa cidade")
        return
    
    # Percorrendo a arvore com ajuda da fila
    while fila:
        path = fila.pop(0)
        cidade = path[-1]
         
        # Verifica se essa cidade nao foi visitada
        if cidade not in visitada:
            cidades_vizinhas = arvore[cidade]
             
            # Verifica as cidades vizinhas desta cidade
            for cidade_vizinha in cidades_vizinhas:
                new_path = list(path)
                new_path.append(cidade_vizinha)
                fila.append(new_path)
                
                # Verifica se essa cidade é seu destino
                if cidade_vizinha == destino:
                    print("Menor rota:", *new_path)
                    return
            visitada.append(cidade)
 
    # Condicao de rota quebrada
    print("Uma das rotas está quebrada :(")
    return
 
if __name__ == "__main__":
     # Arvore
    arvore = {'oradea': ['zerind', 'sibiu'],
             'zerind': ['oradea', 'arad'],
             'arad': ['zerind', 'timisoara', 'sibiu'],
             'timisoara': ['arad', 'lugoj'],
             'lugoj': ['timisoara', 'mehadia'],
             'mehadia': ['lugoj', 'dobreta'],
             'dobreta': ['mehadia', 'craiova'],
             'craiova': ['dobreta', 'rimnicu vilcea', 'pitesti'],
             'sibiu': ['oradea', 'arad', 'fagaras', 'rimnicu vilcea'],
             'fagaras': ['sibiu', 'bucharest'],
             'rimnicu vilcea': ['sibiu', 'pitesti', 'craiova'],
             'pitesti': ['rimnicu vilcea', 'craiova', 'bucharest'],
             'bucharest': ['pitesti', 'fagaras', 'giurgiu', 'urziceni'],
             'giurgiu': ['bucharest'],
             'urziceni': ['bucharest', 'vaslui', 'hirsova'],
             'hirsova': ['urziceni', 'eforie'],
             'eforie': ['hirsova'],
             'vaslui': ['urziceni', 'lasi'],
             'lase': ['vaslui', 'neamt'],
             'neamt': ['lasi']
             }
    
    # Executando a função
    BFS_SP(arvore, 'arad', 'urziceni')

