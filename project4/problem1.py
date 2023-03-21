def countSort(arr):
    max_value = max(arr)
    res = []
    count_nums = [0 for i in range(max_value + 1)]
    for num in arr:
        count_nums[num] += 1
    for i in range(len(count_nums)):
        if count_nums[i] != 0:
            res.extend(count_nums[i] * [i])
    return res

# data = [1, 4, 1, 2, 7, 5, 2]
data=[5, 2, 9, 5, 2, 3, 5]
countSort(data)
a=[]
for i in range (len(data)):
    for j in range(len(countSort(data))):
        if data[i] == countSort(data)[j]:
            c=j
            a.append(c)
            break
print('Original array:', data)
print('Table for the counts:',a)
print('Sorted array: ',countSort(data))


