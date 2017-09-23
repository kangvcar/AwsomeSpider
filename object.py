# -*- coding: utf-8 -*-
class People(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print self.name,'正在走路...'

class Teacher(People):

    def __init__(self, name, age, teachObject):
        People.__init__(self, name, age)
        self.teachObject = teachObject

    def Onteach(self):
        print self.name,'老师正在授课...'
        for i in self.teachObject:
            i.listen()

    def Teach(self):
        print '--------熬了50分钟--------'

    def Offteach(self):
        print self.name, '老师说下课了...'
        for i in self.teachObject:
            i.run()

class Student(People):

    def __init__(self, name, age, xuehao):
        self.name = name
        self.age = age
        self.xuehao = xuehao

    def listen(self):
        print self.name,self.xuehao,'正在听课...'

    def xiake(self):
        self.run()
if __name__ == "__main__":
    Hekangjian = Student('Hekangjian', 21, '07150214')
    Wuzhisheng = Student('Wuzhisheng', 20, '07150236')
    Zhouhaocheng = Student('Zhouhaocheng', 18, '07150250')
    studentList = [Hekangjian,Wuzhisheng,Zhouhaocheng]
    Liwenjin = Teacher('Liwenjin', 35, studentList)

Liwenjin.Onteach()
Liwenjin.Teach()
Liwenjin.Offteach()