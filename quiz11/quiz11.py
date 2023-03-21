class InsertionSort:
    def __call__(self,list):
        return self.main(list)
    def abnormal(self,i1,i2):
        return i1 > i2          #检测是否无序
    def main(self,list):
        for i in range(1,len(list)):
            if self.abnormal(list[i-1],list[i]):
                temp = list[i]
                for j in range(i,-1,-1):
                    # print("j =",j)
                    if j:
                        if self.abnormal(list[j-1],temp):
                            list[j] = list[j-1]
                            # print(list)
                            continue
                    # print("temp", temp)
                    list[j] = temp
                    # print(list)
                    break
        return list



class QuickSort:
    def __call__(self, List):
        return self.main(List)

    def IsOrdered(self, List):
        for i in range(1, len(List)):
            if List[i] < List[i - 1]:
                return False
        return True

    def main(self, List):
        subList = list()
        tempList = list()
        sort = InsertionSort()
        subList = [-1] + tempList + [len(List)]
        while not self.IsOrdered(List):
            subList = [-1] + tempList + [len(List)]
            subList = sort(subList)
            for i in range(1, len(subList)):  # i从列表第二位开始,防止超出范围
                head = subList[i - 1] + 1
                end = subList[i] - 1
                Len = end - head + 1

                pivot = List[head]  # 设pivot为列表的第一个元素
                index_L = head
                index_R = end

                # print('\n')
                # # time.sleep(0.5)
                # print(i)
                # print('pivot', pivot)
                # print("subList",subList)
                # print("List",List)
                # print(index_L, index_R)

                if Len == 1 or Len == 0:
                    continue

                while not index_L == index_R:
                    while List[index_R] >= pivot and not index_L == index_R:  # 主部分
                        index_R -= 1
                    List[index_L], List[index_R] = List[index_R], List[index_L]
                    while List[index_L] <= pivot and not index_L == index_R:
                        index_L += 1
                    List[index_L], List[index_R] = List[index_R], List[index_L]
                tempList.append(index_L)
        return List