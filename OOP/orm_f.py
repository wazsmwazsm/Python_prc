#! /usr/bin/env python3
#! -*- coding:UTF-8 -*-

class Field(object):
    def __init__(self, name, colnum_type):
        self.name = name
        self.colnum_type = colnum_type
    def __str__(self):
        # 方便打印本身信息
        return '<%s:%s>' % (self.__class__.__name__, self.name)

# 字符串类型
class StringField(Field):
    def __init__(self, name, length=255):
        super(StringField, self).__init__(name, 'varchar('+length+')')
# 整型
class IntegerField(Field):
    def __init__(self, name, length=20):
        super(IntegerField, self).__init__(name, 'bigint('+length+')')

# metaclass 构造类
class ModelMetaclass(type):
    def __mew__(cls, name, bases, attrs):
        # 如果是基类, 不修改
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict() # 用来保存类的属性映射
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        # 删掉 Field 的属性, 防止实例的属性会遮盖类的同名属性
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)

# 基类 Model
class Model(dict, metaclass = ModelMetaclass):
    def __init__(self, **kw):
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
            args.append(getter(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))    
