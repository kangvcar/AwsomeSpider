# -*- coding: utf-8 -*-
class People(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print self.name,'正在走路'

class Teacher(People):

    def __init__(self, name, age, teachObject):
        self.name = name
        self.age = age
        self.teachObject = teachObject

    def Onteach(self):
        print self.name,'老师正在授课。'
        self.Onlisten()

    def Offteach(self):
        self.run()

    def Onlisten(self):
        print self.teachObject, '正在听课'


class Student(People):

    def __init__(self, name, age, xuehao):
        self.name = name
        self.age = age
        self.xuehao = xuehao

    def listen(self):
        print self.name,self.xuehao,'正在听课'

    def xiake(self):
        self.run()

Liwenjin = Teacher('Liwenjin', 35, 'AllStudent')
Hekangjian = Student('Hekangjian', 21, '07150214')
Wuzhisheng = Student('Wuzhisheng', 20, '07150236')
Zhouhaocheng = Student('Zhouhaocheng', 18, '07150250')

Liwenjin.Onteach()
Hekangjian.listen()
Wuzhisheng.listen()
Zhouhaocheng.listen()
Hekangjian.xiake()
Wuzhisheng.xiake()
Zhouhaocheng.xiake()
Liwenjin.Offteach()