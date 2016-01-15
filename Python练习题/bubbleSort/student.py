__author__ = 'syswin-sungzuozhi'
class Student(object):
    def __init__(self, n, s):
        self.name = n
        self.score = s
    def __str__(self):
        return ("name : %s score : %d" %(self.name, self.score))