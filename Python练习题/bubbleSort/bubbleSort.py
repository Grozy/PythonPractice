def sort(arr):
    print(len(arr))
    for i in range(len(arr)):
        for j in range(0 ,len(arr) - 1 - i):
            if arr[j] < arr[j + 1]:
                tmp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = tmp

if __name__ == '__main__':
    # simplei
    a = [32, 52, 127, 42, 1, 42, 34, 53, 88, 93, 23, 22, 7, 12, 8, 23, 233, 54, 13, 2]
    # input
    # b = []
    # char_count = raw_input("char number:")
    # print(char_count)
    # for i in range(0, int(char_count)):
    #     number = raw_input()
    #     b.append(number)

    print("----------------- before sorted -----------------\n")
    print(a)
    print("----------------- sorting -----------------\n")
    sort(a)
    print("----------------- sorted -----------------\n")
    print(a)