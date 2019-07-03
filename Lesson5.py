# !/usr/bin/python3
# @Author:千里

year = input("请输入一个年份 ")
if year.isnumeric():
    year = int(year)
    if year%4==0 and year%100!=0 or year%400==0:
        print(year ,"这是一个闰年")
    else:
        print(year ,"这不是闰年")
else:
    print("年份输入不合法，请输入一个正整数的年份")