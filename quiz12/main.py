def find_both2(n, s, small, large):
    if s[0] < s[1]:
        small = s[0]
        large = s[1]
    else:
        small = s[1]
        large = s[0]

    for i in range(3, n-1):
        if s[i] < s[i + 1]:
            if s[i] < small:
                small = s[i]
            if s[i + 1] > large:
                large = s[i + 1]
        else:
            if s[i + 1] < small:
                small = s[i + 1]
            if s[i] > large:
                large = s[i]
    return small, large

n= int(input('please input n:'))
arr = input('please input the array:')
arr = [int(n) for n in arr.split()]
print('output:', find_both2(n, arr, 0, 0))






