import copy
import random
import time
import matplotlib.pyplot as plt


class Step:
    def __init__(self):
        self.maxClique = []
        self.cliqueList = []
        self.maxnC = 0

    def maxCliqn(self):
        max = 0
        for clique in self.cliqueList:
            if max < len(clique):
                max = len(clique)
        return max

    def isNew(self, clique):
        for cl in self.maxClique:
            diff = list(set(clique).difference(set(cl)))
            if (len(diff)):
                continue
            else:
                return False

        return True

    def updateMaxClique(self):
        self.maxnC = self.maxCliqn()
        for clique in self.cliqueList:
            if (len(clique) == self.maxnC):
                if self.isNew(clique):
                    self.maxClique.append(clique)


class Solution1:
    def solution1(self, v, e):
        for i in range(0, len(v)):
            v[i] -= 1
        for i in range(0, len(e)):
            for j in range(len(e[i])):
                e[i][j] -= 1
        # print(v)
        # print(e)
        self.V = v
        self.E = e

    def isConnected(self, u, v):
        if u == -1 or v == -1:
            return 1
        edge_points = self.E[u]
        if v in edge_points:
            return 1
        else:
            edge_points = self.E[v]
            if u in edge_points:
                return 1
            else:
                return 0

    def isConnectedAll(self, clique, v):
        flag = 1
        for i in clique:
            if not self.isConnected(i, v):
                flag = 0
                break
        return flag

    def isConnectedOne(self, clique, v):
        flag = 1
        for i in clique:
            if self.isConnected(i, v):
                flag = 0
                break
        return flag

    def process(self):

        n = len(self.V)
        solutions = {}
        for i in range(0, n):
            solutions[i] = Step()
        for v in self.V:
            a = []
            a.append(v)
            solutions[0].cliqueList.append(a)
            solutions[0].updateMaxClique()

        for i in range(1, n):
            # cliqList= solutions[i-1].maxClique
            preData = solutions[i - 1]
            cliqList = preData.maxClique
            preMax = preData.maxnC
            for clique in cliqList:
                for v in self.V:
                    tempclique = copy.deepcopy(clique)
                    if not v in tempclique:
                        # if s.isConnectedAll(tempclique,v):
                        if self.isConnectedOne(tempclique, v):
                            tempclique.append(v)
                            solutions[i].cliqueList.append(tempclique)
            solutions[i].updateMaxClique()
            if not len(solutions[i].maxClique):
                break

                # for i in range(0,n):
            # print("step"+str(i)+": "+str(solutions[i].maxClique))

        for i in range(n - 1, -1, -1):
            solution = solutions[i]
            if len(solution.maxClique):
                maxn = solution.maxnC

                res = []
                for i in solution.maxClique[0]:
                    res.append(i + 1)
                print("the Largest Independent Set is :")
                print(res)
                break


class Solution2:

    def isConnected(self, u, v):
        if u == -1 or v == -1:
            return 1
        edge_points = self.E[u]
        if v in edge_points:
            return 1
        else:
            edge_points = self.E[v]
            if u in edge_points:
                return 1
            else:
                return 0

    def isConnectedAll(self, clique, v):
        flag = 1
        for i in clique:
            if not self.isConnected(i, v):
                flag = 0
                break
        return flag

    def solution2(self, v, e):
        for i in range(0, len(v)):
            v[i] -= 1
        for i in range(0, len(e)):
            for j in range(len(e[i])):
                e[i][j] -= 1
        # print(v)
        # print(e)
        self.V = v
        self.E = e

    def process(self):
        n = len(self.V)
        solutions = {}
        for i in range(0, n):
            solutions[i] = Step()
        for v in self.V:
            a = []
            a.append(v)
            solutions[0].cliqueList.append(a)
            solutions[0].updateMaxClique()

        for i in range(1, n):
            # cliqList= solutions[i-1].maxClique
            preData = solutions[i - 1]
            cliqList = preData.maxClique
            preMax = preData.maxnC
            for clique in cliqList:
                for v in self.V:
                    tempclique = copy.deepcopy(clique)
                    if not v in tempclique:
                        if self.isConnectedAll(tempclique, v):
                            tempclique.append(v)
                            solutions[i].cliqueList.append(tempclique)
            solutions[i].updateMaxClique()
            if not len(solutions[i].maxClique):
                break

        for i in range(n - 1, -1, -1):
            solution = solutions[i]
            if len(solution.maxClique):
                maxn = solution.maxnC
                

                for i in range(0, len(solution.maxClique[0])):
                    solution.maxClique[0][i] += 1
                print("the Largest Clique is :")
                print(solution.maxClique[0])
                break


#

if __name__ == "__main__":
    #  Below is the test case
    tc1_V = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    tc1_E = [[], [3, 5], [6], [5], [6], [], [8, 9], [9], []]
    s = Solution1()
    print("Test Case 1:")
    s.solution1(tc1_V, tc1_E)
    s.process()
    tc1_V = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    tc1_E = [[], [3, 5], [6], [5], [6], [], [8, 9], [9], []]
    s1 = Solution2()
    s1.solution2(tc1_V, tc1_E)
    s1.process()

    tc2_V = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    tc2_E = [[4], [3, 5, 6], [5, 6], [7, 8], [6], [], [8], [9], []]
    s = Solution1()
    print("Test Case 2:")
    s.solution1(tc2_V, tc2_E)
    s.process()

    tc2_V = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    tc2_E = [[4], [3, 5, 6], [5, 6], [7, 8], [6], [], [8], [9], []]
    s = Solution2()
    s.solution2(tc2_V, tc2_E)
    s.process()
#
#     list_time = []
#     list_size = []
#     for i in range(0,150):
#         V = []
#         E = []
#         for j in range(0,i):
#             V.append(j)
#             E.append([])
#         for j in range(0,i):
#             for k in range(0,i):
#                 if random.randint(0,1) == 1:
#                     E[j].append(k)
#         start = time.time()
#         s = Solution1()
#         s.solution1(V,E)
#         s.process()
#         end = time.time()
#         list_time.append(end - start)
#         list_size.append(len(V))
#         print("size: "+str(len(V))+" time: "+str(end - start))
#     plt.plot(list_size,list_time)
#     plt.show()

# ####belwo is for drawing the graph
# list_time = []
# list_size = []
# for i in range(0,30):
#     V = []
#     E = []
#     for j in range(0,i):
#         V.append(j)
#         E.append([])
#     for j in range(0,i):
#         for k in range(0,i):
#             if random.randint(0,1) == 1:
#                 E[j].append(k)
#     start = time.time()
#     s = Solution2()
#     s.solution2(V,E)
#     s.process()
#     end = time.time()
#     list_time.append(end - start)
#     list_size.append(len(V))
#     print("size: " + str(len(V)) + " time: " + str(end - start))
# plt.plot(list_size,list_time)
# plt.show()

