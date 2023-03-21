class FIFO_01_Pack_prune:
    def __init__(self, N, V, C, W):
        self.num = N
        self.Volume = V
        self.Cost = C
        self.Value = W
        self.BestValue = 0

        # 用于存放活结点，便于理解，把根结点，以及第0层结束标志-1放进去
        # 结点包括2个属性：当前空间大小，当前的价值大小
        self.queue = [[0, 0], [-1, -1], ]
        # 当前剩余价值和,bound()限界函数
        self.rest = 0
        # 把第一个减去，因为我们要在进入这一层前更新rest
        for i in range(1, N):
            self.rest += W[i]

    # 实现时叶子结点不加入到活结点列表
    def enQueen(self, pair, depth):
        if depth < self.num - 1:
            self.queue.append(pair)

    def pack_01(self):
        # selected = [0]*self.num
        # 首先取出根结点
        depth = 0
        pair = self.queue.pop(0)
        CurCost = pair[0]
        CurValue = pair[1]

        while True:
            # 判断左结点能否加入到队列，能的话，把当前空间和当前价值放入队列,满足约束条件
            if CurCost + self.Cost[depth] < self.Volume:
                # 满足限界函数
                if CurValue + self.Value[depth] + self.rest > self.BestValue:
                    # 在进入左子树时，更新bestvalue
                    self.BestValue = CurValue + self.Value[depth]
                self.enQueen([CurCost + self.Cost[depth], CurValue + self.Value[depth]], depth)

            # 右满足限界函数
            if CurValue + self.Value[depth] + self.rest > self.BestValue:
                self.enQueen([CurCost, CurValue], depth)

            # 然后弹出下一个结点
            pair = self.queue.pop(0)
            CurCost = pair[0]
            CurValue = pair[1]

            # 当同一层处理完毕时，先判断是否能够输出结果，判断的标准是队列是否为空，
            # 这时下一层的所有结点已经加入了队列，这时需要把下一层
            # 增加一个结尾-1便于判断，然后进入下一层，弹出下一个结点
            if CurCost == -1:
                if not self.queue:
                    return self.BestValue
                self.enQueen([-1, -1], depth)
                depth += 1
                # 在刚进入下一层时，更新rest
                self.rest -= self.Value[depth]
                # 弹出下一个结点
                pair = self.queue.pop(0)
                CurCost = pair[0]
                CurValue = pair[1]


    def print_Result(self):
        print(self.pack_01())



N = 8
V = 30
C = [11, 2, 3, 9, 13, 6, 15, 7, 19]
W = [5.0, 2.0, 5.0, 7.0, 5.0, 11.0, 6.0, 14.0]

FIFO_01_Pack_prune(N, V, C, W).print_Result()

