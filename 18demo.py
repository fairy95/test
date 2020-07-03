print("hello world!")  # 字符串str
print(2333)  # 整数int
print(2.333)  # 小数float
print(True,False)  # 布尔型bool
print(None)  # 空值NoneType
print(())  # 元组tuple
print([])  # 数组/列表list
print({})  # 字典dict
print(2333,2.333,"你好")  # 打印多个字符
"""
多行注释
"""
'''
多行注释
'''
# 快捷注释 ctrl + /

# 加上end 不换行
print(1,end="")
print(2,end="")
print(3)  
# 加上end 以end中的内容间隔 不换行
print(1,end="&&&")
print(2,end="&&&")
print(3)  

# 同类型数据才可以相加
print("哈哈哈"+"嘻嘻嘻")  

# print不用申明变量类型
a = 1  
print(a)

# input默认输入字符串型
c = float(input("输入第一个数："))  
d = float(input("输入第二个数："))
e = c + d
print("输出两数之和：",e)

# type查看数据类型
print(type("123"))  

aihao = input("输入我的爱好：")
year = (input("输入我的年龄："))
# format数据传入
print("大家好，我的爱好是{}，我的年龄是{}岁".format(aihao,year))  
# 不按顺序的写法 也能重复
print("大家好，我的爱好是{ah}，我的年龄是{y}岁，我的爱好是{ah}，我的年龄是{y}岁".format(ah=aihao,y=year))  

a = input("请输入:")
print("长度是{}".format(len(a)))