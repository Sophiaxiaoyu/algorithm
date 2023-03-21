
import copy
import time
import pandas as pd
import numpy as np


def BronKerbosch(d, rn, pn, xn, u):
    if pn == 0 and xn == 0:
        route.append(copy.deepcopy(R[d]))
    if len(P[d]) > 0:
        u = P[d][0]
    for j in range(pn):
        v = P[d][j]
        if u != -1 and conf[u][v] == 1: continue
        R[d + 1] = []
        for k in range(rn):
            R[d + 1].append(R[d][k])
        R[d + 1].append(v)

        tp, tx = 0, 0

        X[d + 1] = []
        for k in X[d]:
            if conf[v][k]:
                X[d + 1].append(k)
                tx += 1

        P[d + 1] = []
        for k in P[d]:
            if conf[v][k] and k not in X[d]:
                P[d + 1].append(k)
                tp += 1

        BronKerbosch(d + 1, rn + 1, tp, tx, u)
        X[d].append(v)
        xn += 1
        # print("==========")

def conflict(data):
    m = len(data)
    M = [[0]*m]*m
    M = np.array(M)
    for k in range(m):
        for j in range(k+1,m):
            if data.taskStartTime[j] <= data.taskStartTime[k] <= data.taskEndTime[j] \
                    or data.taskStartTime[j] <= data.taskEndTime[k] <= data.taskEndTime[j]:
                M[j,k] = 1
                M[k,j] = 1
    return M

def reverse_m(graph):
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] == 1:
                graph[i][j]=0
            else:
                graph[i][j] = 1
    return (graph)

st = time.time()
# conf = [
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 1, 0, 1, 0, 0, 0, 0],
#         [0, 1, 0, 0, 0, 1, 0, 0, 0],
#         [0, 0, 0, 0, 1, 0, 0, 0, 0],
#         [0, 1, 0, 1, 0, 1, 0, 0, 0],
#         [0, 0, 1, 0, 1, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 1, 1],
#         [0, 0, 0, 0, 0, 0, 1, 0, 1],
#         [0, 0, 0, 0, 0, 0, 1, 1, 0]
# ]

conf = [
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 0]
]

#
# conf = reverse_m(conf)
# print(conf)
n = len(conf)
node_sum = []
for i in range(n):
    node_sum.append(sum(conf[i]))
R, P, X = [[]] * n, [[]] * n, [[]] * n
P[0] = sorted(range(len(node_sum)), key=lambda k: node_sum[k], reverse=True)
route = []

BronKerbosch(0, 0, len(conf), 0, -1)
# print(route)

arr=max(route,key=len)
clique=[]
for i in arr:
    a=i+1
    clique.append(a)
print('largest clique:',clique)

# print(time.time() - st)
