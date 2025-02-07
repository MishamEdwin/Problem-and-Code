graph={
    "A":["B","C"],
    "B":["F","D"],
    "C":[],
    "F":["E"],
    "D":["I","G"],
    "I":[],
    "E":["H"],
    "G":["H"],
    "H":[]
}

def DFSpath(graph,src,dst):

    if src==dst:  # Base Condition
        return True

    ans=False

    for neighgbor in graph[src]:
        ans= ans or DFSpath(graph,neighgbor,dst)
    
    return ans

print(DFSpath(graph,"A","H"))
