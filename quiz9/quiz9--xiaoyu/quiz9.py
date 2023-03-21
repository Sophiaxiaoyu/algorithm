def Vertex(node):
    if (node in path):
        return False
    return True

def cycle(E, n, root):
    path.append(root)
    for i in E[root]:
        if (Vertex(i)):
            if (cycle(E, n, i)):
                return True

    if (len(path) == n):
        if (path[0] in E[path[len(path) - 1]]):
            return True
        else:
            return False
    path.pop()


def HamiltonianCycle(E, n, root):
    if (cycle(E, n, root)):
        print("There is a Hamilton Cycle")
        for i in range(len(path)):
            path[i] = path[i] + 1
        print(path)
    else:
        print('There is no Hamilton Cycle')


path = []
print('N_Vertices is: ',end='')
N_Vertices = int(input())
matrix = list()
for i in range(N_Vertices):
    matrix.append([])
print('N_Edges is: ',end='')
N_Edges = int(input())
print('edge_vertices is: ')
for j in range(N_Edges):
    edge_vertices = input().split()
    u = int(edge_vertices[0])
    v = int(edge_vertices[1])
    matrix[u - 1].append(v - 1)
    matrix[v - 1].append(u - 1)

HamiltonianCycle(matrix, N_Vertices, 0)

