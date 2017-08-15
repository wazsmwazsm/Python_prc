#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

class MyClass(object):  # 所以类默认继承 object 类，可以省略不写
    """ 一个简单的类实例 """
    i = 1234
    def f(self):    # self 代表实例
        return 'hello my friend!'

# 实例化类
x = MyClass()
# 动态绑定数据
x.a = 12
print(x.a)

# 访问实例的属性、方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())

print("x 属于 : ", type(x))



# 使用构造函数

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
    def sum(self):
        print(self)
        print(self.__class__)
        return self.r + self.i

x = Complex(3.0, -4.5)
print(x.sum())

# 类的属性和方法
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性，私有属性在类外部无法直接进行访问
    # 实际是经过名称转换, __weight 改成了 _weight 访问 _weight 还是能访问到的
    __weight = 0
    # 构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))

p = people('qin', 26, 88)
p.speak()

# 单继承

class student(people):
    grade = ''
    def __init__(self, n, a, w, g):
        # 调用父类的方法
        # people.__init__(self,n,a,w)  # 不是好做法
        # 使用 super , 当然多重继承会有问题
        # super(student, self).__init__(n,a,w)
        super().__init__(n,a,w) # python3 可以直接 super()
        self.grade = g
    # 重写父类方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))

s = student('ken',10,60,3)
s.speak()

# 多继承
class speaker():
    topic = ''
    name = ''
    def __init__(self, n, t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))

class sample(speaker, student):
    a = ''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)

test = sample("Tim",25,80,4,"Python")
test.speak()   #方法名同，默认调用的是在括号中排前地父类的方法 使用 super 也一样
# 多态的表现
print(isinstance(test, sample))
print(isinstance(test, speaker))
print(isinstance(test, student))
print(isinstance(test, people))
print(isinstance(p, student))  # 父不是子的实例

# 私有属性、私有方法，python 的权限并不严格，全靠自觉
# 变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，
# 是特殊变量，特殊变量是可以直接访问的，不是private变量
class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0    # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print (self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print (counter.publicCount)
# print (counter.__secretCount)  # 报错，实例不能访问私有变量
print (counter._JustCounter__secretCount)  # 只是经过名称转换，其实还能访问
#!/usr/bin/python3

class Site:
    def __init__(self, name, url):
        self.name = name       # public
        self.__url = url   # private

    def who(self):
        print('name  : ', self.name)
        print('url : ', self.__url)

    def __foo(self):          # 私有方法
        print('这是私有方法')

    def foo(self):            # 公共方法
        print('这是公共方法')
        self.__foo()

x = Site('菜鸟教程', 'www.runoob.com')
x.who()        # 正常输出
x.foo()        # 正常输出
# x.__foo()      # 报错
x._Site__foo()   # 只是经过名称转换，其实还能访问

# 运算符重载
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    # 直接打印类时触发
    def __str__(self):
        return "Vector (%d, %d)" % (self.a, self.b)
    # 两个实例相加时触发, 两个参数分别是两个实例
    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print(v1, v2)
print(v1 + v2)
