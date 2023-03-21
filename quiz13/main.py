def get_min_boxes(things, box_weight):
    things = sorted(things, reverse=True)
    # print(things)
    m = len(things) - 1
    count = 0
    for i in range(len(things)):
        sum = 0
        print(i+1,': {', end='')
        sum = things[i]
        print(things[i], ' ', end='')
        while m >= len(things)/2:
            j = m
            sum += things[j]
            if sum > box_weight:
                count += 1
                break
            if i!=j:
                print(things[j], '', end='')
                m -= 1
        if j == i:
            print('}')
            break
        print('}')

    print('The minimum number of bins is:', count)


if __name__ == '__main__':
    things = [0.1, 0.26, 0.35, 0.4, 0.5, 0.6, 0.75, 0.99]
    box_weight = 1
    print('the capacity of each bin: ')
    get_min_boxes(things, box_weight)
