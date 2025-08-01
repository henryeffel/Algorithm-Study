def dfs(graph,v,visited):
    #현재 노드를 방문처리
    visited[v] = True
    print(v,end="")
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문