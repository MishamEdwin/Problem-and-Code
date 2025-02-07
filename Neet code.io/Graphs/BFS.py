graph={
    "A":["B","D"],
    "B":[],
    "D":["E","G"],
    "E":["C"],
    "C":[],
    "G":["F"],
    "F":[]
}

def BFS (graph,source):
    queue=[]
    queue.append(source)

    while queue: #runs till queue becomes empty
        node=queue.pop(0)
        print(node,end=" ")

        for neighbors in graph[node]:
            queue.append(neighbors)

BFS(graph,"A")
