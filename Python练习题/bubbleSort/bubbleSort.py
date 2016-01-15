# bubble sort

from student import Student

def sort(arr):
    print(len(arr))
    for i in range(len(arr)):
        for j in range(0 ,len(arr) - 1 - i):
            if arr[j] < arr[j + 1]:
                tmp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = tmp

if __name__ == '__main__':

    """
    a = [32, 52, 127, 42, 1, 42, 34, 53, 88, 93, 23, 22, 7, 12, 8, 23, 233, 54, 13, 2]

    b = []
    char_count = raw_input("char number:")
    print(char_count)
    for i in range(0, int(char_count)):
        number = raw_input()
        b.append(number)

    print("----------------- before sorted -----------------\n")
    print(a)
    print("----------------- sorting -----------------\n")
    sort(a)
    print("----------------- sorted -----------------\n")
    print(a)
    """

# sort by score
    students = []
    numberOfMember = raw_input("how many student?")
    for idx in range(int(numberOfMember)):
        name = raw_input("name:")
        score = raw_input("score:")
        aStudent = Student(name, int(score))
        students.append(aStudent)

    for i in range(len(students)):
        for j in range(len(students) - i - 1):
            if students[j].score > students[j + 1].score:
                tmp = students[j]
                students[j] = students[j + 1]
                students[j + 1] = tmp

    for theStudent in students:
        print(str(theStudent))