from selenium import webdriver
from time import sleep

def writed(word):
    with open(r'D:\title.txt','a') as f:
        f.write(word+'\n')
    f.close()

d = webdriver.Chrome()
d.get("https://www.baidu.com")
list = d.find_elements_by_class_name('mnav')
print(len(list))

for i in range(len(list)):
    ele = d.find_elements_by_class_name('mnav')
    ele[i].click()
    print(d.title)
    writed(d.title)
    d.back()
d.quit()
