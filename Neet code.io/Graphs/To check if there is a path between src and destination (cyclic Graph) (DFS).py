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

def DFSpath(graph,src,dst,vis):
    if src==dst:
        return True

    ans=False
    vis.add(src)

    for neighbor in graph[src]:
        if neighbor not in vis:
            ans = ans or DFSpath(graph,neighbor,dst,vis)
    return ans

vis=set()
print(DFSpath(graph,"A","H",vis))