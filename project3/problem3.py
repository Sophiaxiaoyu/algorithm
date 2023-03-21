import numpy as np
from itertools import permutations


def GraphIsomorphism(graph1, graph2):
    graph1 = graph1
    graph2 = graph2

def isIsomorphic():
    if len(graph1) != len(graph2):
        print("not isomorphic")
        return

    for i in perm_list:
        #         print(i)
        if isIsomorphic1(i):
            print("isomorphic")
            # i = [j+1 for j in i]
            # print(i)
            print(list(np.asarray(i) + 1))
            return
    print("not isomorphic")


def isIsomorphic1(perm):
    #     print(perm)
    for i in range(len(graph1)):
        for j in range(len(graph1)):
            if graph1[i][j] != graph2[perm[i]][perm[j]]:
                return False
    return True
#####case1
graph2 = np.array([
        [0, 1, 0, 1, 1],
        [1, 0, 0, 1, 0],
        [0, 0, 0, 1, 1],
        [1, 1, 1, 0, 1],
        [1, 0, 1, 1, 0]])


# #####case2
# graph2=np.array([
#          [0, 1, 0, 1, 1, 0],
#          [1, 0, 1, 0, 0, 1],
#          [0, 1, 0, 1, 1, 0],
#          [1, 0, 1, 0, 0, 1],
#          [1, 0, 1, 0, 0, 1],
#          [0, 1, 0, 1, 1, 0]])

# #####case3
# graph2=np.array([
#         [0, 1, 0, 1, 0, 1, 0],
#         [1, 0, 1, 0, 1, 0, 0],
#         [0, 1, 0, 1, 0, 1, 0],
#         [1, 0, 1, 0, 0, 0, 1],
#         [0, 1, 0, 0, 0, 1, 1],
#         [1, 0, 1, 0, 1, 0, 1],
#         [0, 0, 0, 1, 1, 1, 0]])


#####case1
graph1 = np.array([
        [0, 1, 0, 1, 0],
        [1, 0, 1, 1, 1],
        [0, 1, 0, 1, 1],
        [1, 1, 1, 0, 0],
        [0, 1, 1, 0, 0]])

# #####case2
# graph1 =np.array([
#         [0, 1, 1, 0, 1, 0],
#         [1, 0, 1, 0, 0, 1],
#         [1, 1, 0, 1, 0, 0],
#         [0, 0, 1, 0, 1, 1],
#         [1, 0, 0, 1, 0, 1],
#         [0, 1, 0, 1, 1, 0]])


# #####case3
# graph1 = np.array([
#     [0, 1, 0, 1, 1, 0, 0],
#     [1, 0, 1, 0, 1, 0, 0],
#     [0, 1, 0, 1, 0, 1, 0],
#     [1, 0, 1, 0, 0, 0, 1],
#     [1, 1, 0, 0, 0, 1, 1],
#     [0, 0, 1, 0, 1, 0, 1],
#     [0, 0, 0, 1, 1, 1, 0]])



per_index=0
perm_list = list(permutations(range(0, len(graph1))))
GraphIsomorphism(graph1, graph2)
isIsomorphic()
