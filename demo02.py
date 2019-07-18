"""
 一、  del
   删除变量
 1. 语法:
del 变量名1, 变量名2
 2. 作用：
用于删除变量,同时解除与对象的关联.如果可能则释放对象。
 3. 自动化内存管理的引用计数：
每个对象记录被变量绑定(引用)的数量,当为0时被销毁。

    a=“悟空”
    b=a
    c=a
    del a,b   #删除变量a,b不释放对象悟空
    c=none    #不再引用悟空（悟空引用计数为零）
"""
#  二、身份运算符 （is  is not）

a = 800
b = 1000
c = 800
d = 1000
print(id(a))
print(id(b))
print(id(c))

print(a is b)  # is的本质是通过id来判断的
print(a is c)
print(b is d)  # ture只适用于文件式，终端交互式中结果为false

# 小整数对象池：CPython 中整数 -5 至 256,永远存在小整数对象池中,不会被释放并可重复使用。

# 池 （提高内存利用率）

# 运算符优先级
# 	高到低：
# 算数运算符
# 比较运算符
# 快捷运算符
# 身份运算符
# 逻辑运算符

#  行
# 一个物理行，两个逻辑行
d = 1 + 2 \
    + 3 + 4
# 四个物理行，一个逻辑行
d = (1
     + 2
     + 3
     + 4)
# pass 语句

# 通常用来填充语法空白。

"""
  选择语句
"""
sex = input("请输入性别")
if sex == "男":
    print("您好，先生！")  # tab键默认缩进4个空格
elif sex == "女":
    print("您好，女士！")
else:
    print("性别未知")

print("后续逻辑")

#   调试：让程序中断，逐语句执行
#    目的：审查运行过程中变量取值
#         审查程序运行流程
#   步骤：
#       1.加断点
#       2.调试运行，debug
#       3.F8,执行一行
#       4.ctrl+f2  停止

# 真值表达式

if 100:  # 本质if bool(100)
    print("真值")
if 0:
    print("真值")  # 空

# 条件表达式
sex = none
if input("请输入性别") == "男":
    sex = 1
else:
    sex = 0
print(sex)
# 例：
sex = 1 if input("请输入性别") == "男" else 0
print(sex)

"""
    循环语句
     while 条件：
     满足条件执行的循环体
     else：
     不满足条件执行一次
     
     跳转语句
     break
"""

while true:
    use = int(input("请输入美元"))
    print(usd * 6.9)
    if input("输入q键退出"):
        break

#  while 计数

count = 0
while count < 3:
    count += 1
    use = int(input("请输入美元"))
    print(usd * 6.9)
