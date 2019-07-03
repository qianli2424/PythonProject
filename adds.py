# !/usr/bin/python3
# @Author:千里
#定义了一个从a累加到b的方法
def adds(a,b):
    i = a
    sum = 0
    while i<=b:
        sum = sum+i
        i = i+1
    return sum

def test_adds(a1,b1,expect):
    result = adds(a1,b1)
    if result == expect:
        print("测试通过")
    else:
        print(result)
        print("测试失败")

test_adds(1,100,5050)