max_V, now_W, now_V, best_X = 0, 0, 0,[] # max-value、now-weight、now_value、best_solution
# print('please input the number of goods, the weight for bag, with space to split：')
# n, c = map(int, input().split())
n=5
c=9
# for i in range(n):
#     print(f' please enter the weight and value for {i + 1} ，with space to split：')
#     goods.append(list(map(int, input().split())))
# print(goods)
goods=[[2,20],[5,30],[7,35],[3,12],[1,3]]
x = [0 for i in range(n)]  # initialize the solution

def backtrack(i):  # i is the layer，nis the number of goods，the total number of layer is n+1
    global max_V, now_V, now_W, best_X, x
    if i >= n:
        if max_V < now_V:
            max_V = now_V
            best_X = x[:]
    else:
        if now_W + goods[i][0] <= c:
            x[i] = 1
            now_W += goods[i][0]
            now_V += goods[i][1]
            backtrack(i + 1)
            now_W -= goods[i][0]
            now_V -= goods[i][1]
        x[i] = 0
        backtrack(i + 1)

backtrack(0)
print(f'the max profile is：{max_V}')
print(f'the goods which are in bag：{[i + 1 for i in range(n) if best_X[i]]}')
