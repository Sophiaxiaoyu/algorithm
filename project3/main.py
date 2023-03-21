# import itertools as it
#
# def graph():
#     matrix = list()
#     for j in range(N_Edges):
#         edge_vertices = input().split()
#         u = int(edge_vertices[0])
#         v = int(edge_vertices[1])
#         matrix[u - 1].append(v - 1)
#         matrix[v - 1].append(u - 1)
#
# def isomorphic(vertices):
#     flag = 1
#     isValid = False
#     print_isomorphic = 0
#     g = [[0 for i in range(20)] for j in range(20)]
#     h = [[0 for i in range(20)] for j in range(20)]
#     a[20] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}mp
#     while (flag):
#         for i in range (vertices):
#             for j in range(vertices):
#                 if (g[i][j] ^ h[a[i]][a[j]]):
#                     flag = 0
#
#         if (flag):
#             isValid = True
#             if (print_isomorphic == 0):
#                 print("isomorphic")
#                 print("vertices orderings are")
#                 print_isomorphic += 1
#
#             for p in range(vertices):
#                 print(a[i])
#         list = list(it.permutations(a))
#         print(list)
#
# if __name__ == '__main__':
#     print("Enter the number of vertices and edges", end='')
#     vertices, edges = int(input())
#     print('Enter the edges of graph 1', end='')
#     N_Edges = int(input())
#     graph()
#     isomorphic(vertices)
#
#
#
#
#
import networkx as nx

import matplotlib.pyplot as plt



def adMmatrix2Img(matrix):

    G = nx.Graph()

    n = len(matrix)

    point = []

    for i in range(n):

        point.append(i)

    G.add_nodes_from(point)

    edglist = []

    for i in range(n):

        for k in range(i + 1, n):

            if matrix[i][k] > 0:

                edglist.append((i, k))

    G.add_edges_from(edglist)

    position = nx.circular_layout(G)

    nx.draw_networkx_nodes(G, position, nodelist=point, node_color="y")

    nx.draw_networkx_edges(G, position)

    nx.draw_networkx_labels(G, position)

    plt.show()





if __name__ == '__main__':
    # matrix = [[1,2,1,1,1],
    #           [2,0,3,1,1],
    #           [1,3,0,2,2],
    #           [1,1,2,0,1],
    #           [1,1,2,1,0]]
    # matrix = [[0, 1, 0, 1, 0],
    #           [1, 0, 1, 1, 1],
    #           [0, 1, 0, 1, 1],
    #           [1, 1, 1, 0, 0],
    #           [0, 1, 1, 0, 0]]
    matrix = [[0, 1, 0, 1, 1],
              [1, 0, 0, 1, 0],
              [0, 0, 0, 1, 1],
              [1, 1, 1, 0, 1],
              [1, 0, 1, 1, 0]]

    adMmatrix2Img(matrix)