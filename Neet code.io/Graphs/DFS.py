graph={
    "A":["B","D"],
    "B":[],
    "D":["E","G"],
    "E":["C"],
    "C":[],
    "G":["F"],
    "F":[]
}

def DFS(graph,source):
    stack=[]
    stack.append(source)

    while stack: #runs till stack becomes empty
        node=stack.pop()
        print(node,end=" ")

        for neighbors in graph[node]:
            stack.append(neighbors)

DFS(graph,"A")