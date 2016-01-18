#-*-coding:gb2312-*- 
__author__ = 'syswin-sungzuozhi'

def quikSort(arr , min, max):
    if min > max:
        return
    tmp = arr[min] 
    i = min 
    j = max 

    while i != j:
        while a[j] >= tmp and i < j:
            j = j - 1
        while a[i] <= tmp and i < j:
            i = i + 1
        if i < j:
            tmp0 = a[i]
            a[i] = a[j]
            a[j] = tmp0

    arr[min] = arr[i]
    arr[i] = tmp

    quikSort(arr, min, i - 1)
    quikSort(arr, i + 1, max)
    return

if __name__ == '__main__':
    a = [10, 8 , 3, 1, 6, 4, 20, 16, 89, 56, 23]
    print a
    quikSort(a, 0, len(a) - 1)
    print a
