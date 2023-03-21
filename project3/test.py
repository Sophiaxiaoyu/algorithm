
import numpy as np

def getAA(A):
    RES=np.full((len(A), len(A)), 0)
    for i in range(len(A)):
        for j in range(len(A)):
            if(A[i][j]>0):
                RES[i][j]=1
    return RES

def getRA(A,AA):
    RX = np.full((len(A), len(A)), 0)
    for i in range(len(A)):
        for j in range(len(A)):
            if(i==j):
                RX[i][j]=AA[i][j]
            else:
                res=0
                for k in range(len(A)):
                    res += (A[i][k] + A[j][k])*((AA[i][k]^AA[j][k])^1)
                RX[i][j] = res
    return RX

def getRX(A,AA):
    RX=np.full((len(A),len(A)),0)
    for i in range(len(A)):
        for j in range(len(A)):
            if (i == j):
                RX[i][j] = AA[i][j]
            else:
                res = 0
                for k in range(len(A)):
                    res += (A[i][k] + A[j][k])*(AA[i][k]^AA[j][k])
                RX[i][j] = res
    return RX

if __name__ == '__main__':
    ###case1
    A = np.array([
        [0, 1, 0, 1, 1],
        [1, 0, 0, 1, 0],
        [0, 0, 0, 1, 1],
        [1, 1, 1, 0, 1],
        [1, 0, 1, 1, 0]])


    # ###case2
    # A=np.array([
    #     [0, 1, 1, 0, 1, 0],
    #     [1, 0, 1, 0, 0, 1],
    #     [1, 1, 0, 1, 0, 0],
    #     [0, 0, 1, 0, 1, 1],
    #     [1, 0, 0, 1, 0, 1],
    #     [0, 1, 0, 1, 1, 0]])

    # # ######case3
    # A = np.array([
    #     [0, 1, 0, 1, 1, 0, 0],
    #     [1, 0, 1, 0, 1, 0, 0],
    #     [0, 1, 0, 1, 0, 1, 0],
    #     [1, 0, 1, 0, 0, 0, 1],
    #     [1, 1, 0, 0, 0, 1, 1],
    #     [0, 0, 1, 0, 1, 0, 1],
    #     [0, 0, 0, 1, 1, 1, 0]])


    AA=getAA(A)#获取同型矩阵
    RA=getRA(A,AA)#获取行间同或矩阵为RA
    RX=getRX(A,AA)#获取行间异或矩阵为RA


    ###case1
    A1 = np.array([
        [0, 1, 0, 1, 0],
        [1, 0, 1, 1, 1],
        [0, 1, 0, 1, 1],
        [1, 1, 1, 0, 0],
        [0, 1, 1, 0, 0]])


    # ####case2
    # A1=np.array([
    #     [0, 1, 0, 1, 1, 0],
    #     [1, 0, 1, 0, 0, 1],
    #     [0, 1, 0, 1, 1, 0],
    #     [1, 0, 1, 0, 0, 1],
    #     [1, 0, 1, 0, 0, 1],
    #     [0, 1, 0, 1, 1, 0]])

    # #####case3
    # A1 = np.array([
    #     [0, 1, 0, 1, 0, 1, 0],
    #     [1, 0, 1, 0, 1, 0, 0],
    #     [0, 1, 0, 1, 0, 1, 0],
    #     [1, 0, 1, 0, 0, 0, 1],
    #     [0, 1, 0, 0, 0, 1, 1],
    #     [1, 0, 1, 0, 1, 0, 1],
    #     [0, 0, 0, 1, 1, 1, 0]])
    AA1=getAA(A1)
    RA1=getRA(A1,AA1)
    RX1=getRX(A1,AA1)
    flag=0
    aid=np.full((len(A),len(A)),0)
    for i in range(len(A)):
        for j in range(len(A)):
            aid[i][j]=A[i][j]
    for i in range(len(RX1)):
        # print("RX1:",RX1[i])
        temp=[]#测试用的
        index=-1
        for j in range(len(RX)):
            if(set(RX[j]) == set(RX1[i])):
                temp=RX[j]#测试用的
                index=j #找到匹配的行了 记录用于下一步骤
                # print("temp:", temp)  # 测试用的
                # print('index',index)
                break#找到了就没必要找接下去了
        if(index!=-1):#也就是找到匹配行
            if(set(RA[index]) != set(RA1[i]) or set(A[index]) != set(A1[i])): #还要判断相对应的行间同或矩阵、行间异或矩阵是否也存在同样的匹配
                flag=1
                print("not isomorphic！")
                break
            #若成立才交换 否则直接退出
            print("change the rows:{1} {0}".format(index + 1, i + 1))
            a = np.arange(1, 6)
            c = a[i]
            a[i] = a[index]
            a[index] = c
            print('c', c)
            print('a[i]', a[i])
            print('a[index]', a[index])
            print('a', a)
            # a = np.arange(1,6)
            # print(a)
            # for i in range(len(a)):
            #     for j in range(len(a)):
            #         if a[i] == j:
            #             c = a[i]
            #             a[i] = a[index]
            #             a[index] = c
            #             print('c', c)
            #             print('a[i]', a[i])
            #             print('a[index]', a[index])
            #             print('a', a)


            #以下都是同样的操作 交换对应矩阵的行和列 先交换行 再交换列
            for k in range(len(RX)):
                RX[index][k], RX[i][k] = RX[i][k], RX[index][k]
            for k in range(len(RX)):
                RX[k][index], RX[k][i] = RX[k][i], RX[k][index]
            for k in range(len(RX)):
                RA[index][k],RA[i][k]=RA[i][k],RA[index][k]
            for k in range(len(RX)):
                RA[k][index],RA[k][i]=RA[k][i],RA[k][index]
            for k in range(len(RX)):
                A[index][k],A[i][k]=A[i][k],A[index][k]
            for k in range(len(RX)):
                A[k][index],A[k][i]=A[k][i],A[k][index]
        else:
            flag = 1
            print(" not isomorphic！")
            break
    if (flag == 0):
        print("isomorphic！")
        print("temp:", temp)
        print("original adjacency matrices:\n", aid)
        print(" change the adjacency matrices:\n", A)
        print("same as another adjacency matrices A1:\n{0}".format(A1))


