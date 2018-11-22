#!/usr/bin/python3.3
# _*_ coding: utf-8 _*_


class ObjectCreator(object):
    pass

# 将类实例化，生成一个类的对象
my_obj = ObjectCreator()
print("", ObjectCreator)
print("", my_obj)


# 做参数传给函数
def echo(o):
    print(o)

echo(ObjectCreator)

print("hasattr('new_attribute') == ", hasattr(ObjectCreator, 'new_attribute'))
# add attribution for ObjectCreator
ObjectCreator.new_attribute = 'foo'
print("hasattr('new_attribute') == ", hasattr(ObjectCreator, 'new_attribute'))

print("ObjectCreator.new_attribute == ", ObjectCreator.new_attribute)

# 可以将类赋值给一个变量
ObjectCreatorMirror = ObjectCreator

print("ObjectCreatorMirror :", ObjectCreatorMirror)
print("ObjectCreatorMirror() :", ObjectCreatorMirror())


# dynamic create class
print("============ dynamic create class")


def choose_class(name):
    if name == 'foo':
        class Foo(object):
            pass
        return Foo      # return class instead of class's instance
    else:
        class Bar(object):
            pass
        return Bar      # return class instead of class's instance

MyClass = choose_class('foo')
print("MyClass:", MyClass)

print("MyClass():", MyClass())
