def count_sort(data, maxValue):  # 定义计数排序，data是列表数据，maxValue表示值
    bucket_len = maxValue + 1  # 定义桶的长度是值加1，桶号从0开始
    bucket = [0] * bucket_len  # 初始化桶
    count = 0  # 计数个数
    arr_len = len(data)  # 列表长度
    for i in range(arr_len):  # 遍历列表
        if not bucket[data[i]]:  # 列表数据不为桶号
            bucket[data[i]] = 0  # 这时初始化从0将列表数据做桶号
        bucket[data[i]] += 1  # 桶号依次加1

    for j in range(bucket_len):  # 遍历桶
        while bucket[j] > 0:  # 将列表数据放在对应桶号内
            data[count] = j
            count += 1  # 计数个数加1
            bucket[j] -= 1  # 个数减一，下一个相同的元素往前排
    print(count)
    return data  # 返回排序后的列表

a=[]
data = [62, 31, 84, 96, 19, 47]
print("排序前列表数据：", data)
data2 = count_sort(data, 96)  # 调用计数排序函数
print("排序后列表数据：", end='')
for j in range(6):
    a.append(data2[j])
print(a)



