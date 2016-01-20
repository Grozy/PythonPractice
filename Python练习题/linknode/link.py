__author__ = 'syswin-sungzuozhi'
from node import Node


class LinkList(object):
    def __init__(self):
        self.head = 0


    def initlist(self, data):
        self.head = Node(data[0])
        p = self.head

        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next

    def __str__(self):
        p = self.head
        string = '['
        while p != 0:
            if len(string) == 1:
                string = string + str(p.data)
            else:
                string = string + ',' + str(p.data)
            p = p.next
        return string + ']'

    def insert(self, val, ratherThan):
        p = self.head
        while p != 0:
            if p.data > ratherThan:
                node = Node(val)
                if p.next == 0:
                    p.next = node
                else:
                    node.next = p.next
                p.next = node
                break
            p = p.next



if __name__ == '__main__':

    arr_count = raw_input("how many items?:\n")
    arr = []
    for i in range(0, int(arr_count)):
        item = raw_input();
        arr.append(int(item))

    a = [10 ,3, 8 ,6, 7, 1, 2, 9]
    list = LinkList()
    list.initlist(arr)

    print(str(list))

    list.insert(1,4)

    print(str(list))