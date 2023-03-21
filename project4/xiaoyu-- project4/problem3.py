from sys import maxsize
from itertools import permutations

def greedy_path(j):
    path_vertexs.append(j)
    row = c[j]
    copy_row = [value for value in row]
    walked_vertex = []
    for i in path_vertexs:
        walked_vertex.append(copy_row[i])
    for vertex in walked_vertex:
        copy_row.remove(vertex)
    if len(path_vertexs) < n_verticlas:
        min_e = min(copy_row)
        j = row.index(min_e)
        path_length.append(min_e)
        greedy_path(j)
    else:
        min_e = c[j][0]
        path_length.append(min_e)
        path_vertexs.append(0)
    return path_vertexs, path_length


def print_path(vertexs, lengths):
    path = ''
    vertexs = [vertex + 1 for vertex in vertexs]
    for i, vertex in enumerate(vertexs):
        path += str(vertex)
        if i == n_verticlas:
            break
        path += '->'
    print("the lowest cost ：", sum(lengths))
    print("path ：", path)



def heuristic(graph, s):
    # store all vertex apart from source vertex
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)
    min_path = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:
        # store current Path weight(cost)
        current_pathweight = 0
        # compute current path weight
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]
        # update minimum
        min_path = min(min_path, current_pathweight)
    return min_path



if __name__ == "__main__":
    print('the greedy algorithm:')

    n_verticlas=5
    c = [[0, 60, 100, 50, 90],
         [60, 0, 70, 40, 30],
         [100, 70, 0, 65, 55],
         [50, 40, 65, 0, 110],
         [90, 30, 55, 110, 0]]


    # n_verticlas = 4
    # c = [[0, 10, 15, 20],
    #      [10, 0, 35, 25],
    #      [15, 35, 0, 30],
    #      [20, 25, 30, 0]]

    path_length = []
    path_vertexs = []
    path_vertexs, path_length = greedy_path(0)
    print_path(path_vertexs, path_length)

#####the heuristic algorithm:
    # print('-----------------------')
    # print('the heuristic algorithm:')
    # V = 5
    # c = [[0, 60, 100, 50, 90],
    #      [60, 0, 70, 40, 30],
    #      [100, 70, 0, 65, 55],
    #      [50, 40, 65, 0, 110],
    #      [90, 30, 55, 110, 0]]

    #
    # V = 4
    # c = [[0, 10, 15, 20],
    #      [10, 0, 35, 25],
    #      [15, 35, 0, 30],
    #      [20, 25, 30, 0]]
    # s = 0
    # print('the lowest cost ：',heuristic(c, s))

