import heapq

weight = [2, 5, 7, 3, 1]
value = [20, 30, 35, 12, 3]
maxcap = 13

# print("the information for goods：")
# print("weights：", weight)
# print("value：", value)
# print("the max weight for bag is: ", maxcap)

n = len(weight)
cweight = 0
cvalue = 0
bestv = 0
bests = []
num = 0
heap = []
heapq.heapify

def maxbound(i):
    global cweight, cvalue, n, weight, value, maxcap
    left = maxcap - cweight
    b = cvalue
    while i < n and weight[i] <= left:
        left -= weight[i]
        b += value[i]
        i += 1
    if i < n:
        b += (value[i] / weight[i]) * left
    return b


# BFS
i = 0

upper = maxbound(i)
str = ''
node_number=0

while (1):
    wt = cweight + weight[i]
    node_number += 2
    # print('node_number', node_number)
    # print("wt:",wt)
    if wt <= maxcap:
        if cvalue + value[i] > bestv:
            # print('i=',i+1)
            bestv = cvalue + value[i]
            # print("bestv=",bestv)
            bests = str + '1'
            bests = bests + '0' * (n - len(bests))
        if i + 1 < n:
            heapq.heappush(heap, [1 / upper, cweight + weight[i], cvalue + value[i], i + 1, str + '1'])
    upper = maxbound(i + 1)
    if upper >= bestv:
        if i + 1 < n:
            heapq.heappush(heap, [1 / upper, cweight, cvalue, i + 1, str + '0'])

    if len(heap) == 0:
        a=[]
        for i in range(len(bests)):
            if bests[i] == '1':
                a.append(i+1)
        print('best items:', a)
        print('bestvalue :', bestv)
        break

    # node_number += 1
    # print("heap:",heap)
    node = heapq.heappop(heap)
    upper = 1 / node[0]
    cweight = node[1]
    cvalue = node[2]
    i = node[3]
    str = node[4]
    # print('node numbers:',node)
    # print('node_number', node_number)
    # print('node numbers:',node)
print('node_number:', node_number)

