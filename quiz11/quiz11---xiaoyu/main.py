def quick_sort(arr):
    if len(arr) < 2:
        return arr
    stack = []
    stack.append(len(arr) - 1)
    stack.append(0)
    while stack:
        l = stack.pop()
        r = stack.pop()

        index = partition(arr, l, r)
        if l < index - 1:
            stack.append(index - 1)
            stack.append(l)
        if r > index + 1:
            stack.append(r)
            stack.append(index + 1)

def partition(arr, start, end):
    pivot = arr[start]
    while start < end:
        while start < end and arr[end] >= pivot:
            end -= 1
        arr[start] = arr[end]
        while start < end and arr[start] <= pivot:
            start += 1
        arr[end] = arr[start]
    arr[start] = pivot
    return start


if __name__ == '__main__':
    list = [100, -10, 200, 50, -22, 22, 32, 101]
    print('original list:',list)
    quick_sort(list)
    print('after quick sort:',list)
