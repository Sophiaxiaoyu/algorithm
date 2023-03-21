n = 6
a, b, c, d, e,f = range(n)
count = 0
graph = [
    {a, b, d},
    {b, a, c, e},
    {c, b, f},
    {d, a, e},
    {e, b, d, f},
    {f,e,c}
]
color_number = 3
x = [0] * n
X = []

def conflict(k):
    global n, graph, x
    nodes = [node for node in range(k) if node in graph[k]]
    if x[k] in [x[node] for node in nodes]:
        return True

    return False

def coloring(k):
    global n, color_number, graph, x, X, count
    if k == n:
        count+=1
        print(count,':' ,end="")
        print(x)
    else:
        for color in range(color_number):
            x[k] = color
            if not conflict(k):
                coloring(k + 1)
    return count

print('the number of solutions is:',coloring(a))
