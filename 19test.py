# 元组，列表，字典可以相互嵌套
# 元组：任意类型，长度固定
b = (1,2,3,"4",True,(1,2,3,4),[1,2,3,4],{"username":"dd"})  # 元组可以是任意类型
print(b[-1])  # 元组取值 第一个元素下标为0 最后一个元素是-1 倒着数为负数
print(b[-3])
print(len(b))  # len：元组长度


# 列表：任意类型，长度可变
a = [1,2,3,"4",True,(1,2,3,4),[1,2,3,4],{"username":"dd"}]
b = a[-1]
print(b)
# append：添加列表元素，此方法只能列表用，元组不能用
a.append("daeg")  
print(len(a))  # 列表长度
print(a)

# clear删除全部元素
a.clear()
print(a)

# pop从列表中取出元素并且删除取出元素，一般不用
c = a.pop(1)  # 参数是元素的下标
print(c)
print(a)

# count统计数组中某个值的个数
d = a.count(1)  # True也算作1，Flase算作0
print(d)

# index统计数组中某个值的下标
print(index("2"))


# 字典，键值对 键（key） 值（value)，值可以是任意类型
a = {"user":"dao"}

# 字典取值：2种方法
print(a["nvpy"])  # 如果键不存在，这种方式会报错
print(a.get("passea"))  # 如果键不存在，这种方式会不报错，输出None

# 修改键值、添加键值：2种方法，第二种不常用
# key值存在，就是修改；key不存在，就是新增
a["user"] = "hahahah"
print(a)
a.update({"user":"hiehie"})
print(a)
# 添加字典元素
a["xing"] = "ou"
print(a)
a.update({"ming":"qian"})
print(a)

# pop删除字典键值
a.pop("xing")
print(a)