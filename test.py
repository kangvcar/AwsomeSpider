# -*-coding:utf-8 -*-

# class Employee:
#     'Common base class for all employees'
#     empCount = 0
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount += 1
#
#     def displayCount(self):
#         print "Total Employee %d" % Employee.empCount
#
#     def displayEmployee(self):
#         print "Name :", self.name, "Salary :", self.salary
#
# ## This would create first object of Employee class
# emp1 = Employee("Maxsu", 2000)
#
# ## This would create second object of Employee class
# emp2 = Employee("Kobe", 5000)
#
# ## This would create second object of Employee class
# emp3 = Employee("James", 9000)
#
# # emp1.salary = 7000  #Add an 'salary' attribute
# # emp1.name = 'xyz'   #Modify 'name' attribute
# #del emp1.salary #Delete 'name' attibute
#
# # emp1.displayEmployee()
# # emp2.displayEmployee()
# # print "Total Employee %d" % Employee.empCount
# #
# # print hasattr(emp1, 'salary') #Retures true if 'salary' attribute exists
# # print getattr(emp1, 'salary') #Retures value of 'salary' attribute
# # print setattr(emp1, 'salary', 7055) #Set attribute 'salary' at 7055
# # print delattr(emp1, 'salary',)    #Delete attribute 'salary'
#
# print "Employee.__doc__:", Employee.__doc__
# print "Employee.__name__:", Employee.__name__
# print "Employee.__module__:", Employee.__module__
# print "Employee.__bases__:", Employee.__bases__
# print "Emoloyee.__dict__:", Employee.__dict__

# print '-----------------------------------------------------------------------'

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#     def __del__(self):
#         class_name = self.__class__.__name__
#         print class_name, "destroyed"
#
# pt1 = Point()
# pt2 = pt1
# pt3 = pt1
# print id(pt1), id(pt2), id(pt3)
# del pt1
# del pt2
# del pt3

# print '-----------------------------------------------------------------------'

# class Parent:   #define parent class
#     parentAttr = 100
#     def __init__(self):
#         print "Calling parent constructor"
#
#     def parentMethod(self):
#         print "Calling parent method"
#
#     def setAttr(self, attr):
#         Parent.parentAttr = attr
#
#     def getAttr(self):
#         print "Parent attribute:", Parent.parentAttr
#
# class Child(Parent):    #define child class
#     def __init__(self):
#         print "Calling child constructor"
#
#     def childMethod(self):
#         print "Calling child method"
#
# c = Child()
# c.childMethod()
# c.parentMethod()
# c.setAttr(200)
# c.getAttr()

# print '-----------------------------------------------------------------------'

# class Parent:
#     def myMethod(self):
#         print "Calling parent method"
#
# class Child(Parent):
#     def myMethod(self):
#         print "Calling Child method"
#
# c = Child()
# c.myMethod()

#print '-----------------------------------------------------------------------'

# class Vector:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __str__(self):
#         return 'Vector(%d, %d)' % (self.a, self.b)
#
#     def __add__(self, other):
#         return Vector(self.a + other.a, self.b + other.b)
#
# v1 = Vector(2,10)
# v2 = Vector(5,-2)
# print (v1 + v2)

#print '-----------------------------------------------------------------------'
#
# class JustCounter:
#     __secretCount = 0
#
#     def count(self):
#         self.__secretCount += 1
#         print self.__secretCount
#
# counter = JustCounter()
# counter.count()
# counter.count()
# print counter._JustCounter__secretCount






















