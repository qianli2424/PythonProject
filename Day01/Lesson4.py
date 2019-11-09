#author:qianli
import random

guess = random.choice(["石头","剪刀","布"])
input = input("请输入猜拳口令")
win = [["石头","布"],["布","剪刀"],["剪刀","石头"]]
list = list[guess,input]

if guess==input:
    print("平局 ")
elif list in win:
    print("恭喜你，赢了")
print(guess)