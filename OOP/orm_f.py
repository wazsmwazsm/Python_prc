#! /usr/bin/env python3
#! -*- coding:UTF-8 -*-

''' 此例子只是一个简单实例, 很多内容都是不完善的, 意在理解 metaclass '''

class Field(object):

    def __init__(self, name, colnum_type):
        self.name = name
        self.colnum_type = colnum_type

    def __str__(self):
        # 方便打印本身信息
        return '<%s(%s):%s>' % (self.__class__.__name__, self.colnum_type, self.name)

# 字符串类型
class StringField(Field):

    def __init__(self, name, length=255):
        super(StringField, self).__init__(name, 'varchar('+str(length)+')')
# 整型
class IntegerField(Field):

    def __init__(self, name, length=20):
        super(IntegerField, self).__init__(name, 'bigint('+str(length)+')')

# metaclass 构造类
class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        # 如果是基类, 不修改
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict() # 用来保存类的属性映射
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        # 删掉类的属性, 防止实例的属性会遮盖类的同名属性
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)

# 基类 Model
class Model(dict, metaclass = ModelMetaclass): # 在这里已经代用了 ModelMetaclass 的 __new__ , 比 __init__ 要早

    def __init__(self, **kw):
        # 继承的原型是 dict, 将传入的变量传到 dict 的构造函数中, 其实就是建立了一个 dict
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []

        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        # 构造 sql
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

# 定义一个表的 model
# metaclass可以隐式地继承到子类, 但子类自己却感觉不到
class User(Model):
    # 定义类的属性到列的映射
    id = IntegerField('id')
    name = StringField('username', 40)
    email = StringField('email', 150)
    password = StringField('password', 40)

# 创建一个实例
u = User(id = 12345, name = 'Michael', email = 'test@orm.org', password = 'my-pwd')
# 保存到数据库：
u.save()
print(u['id']) # model 是由 dict 的原型创建的, 所以可以使用 dict 的操作
