__author__ = 'syswin-sungzuozhi'

if __name__ == '__main__':

    len = 4

    arr = [1] * len
    print(arr)

    for i1 in range(1, len):
        arr[1] = i1
        for i2 in range(1, len):
            arr[2] = i2
            for i3 in range(1, len):
                arr[3] = i3
                book = [0] * len
                for i in range(1, len):
                    # print("arr:%d i:%d" %(arr[i],i))
                    book[arr[i]] = 1
                    sum = 0
                    for i in range(1, len):
                        sum += book[i]
                    if sum == 3:
                        print("%d, %d, %d" % (i1, i2, i3))




