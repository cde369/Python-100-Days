"""
将华氏温度转换为摄氏温度
F = 1.8C + 32

Version: 0.1
Author: 骆昊
Date: 2018-02-27
"""

def hua_she():
    f = float(input('请输入华氏温度: '))
    c = (f - 32) / 1.8
    print('%.2f华氏度 = %.2f摄氏度' % (f, c))


"""
输入半径计算圆的周长和面积

Version: 0.1
Author: 骆昊
Date: 2018-02-27
"""
import math
def yuan():
    radius = float(input("请输入圆等的半价"))
    perimeter = 2 * math.pi * radius
    area = math.pi * radius * radius
    print('周长: %.2f' % perimeter)
    print('面积: %.2f' % area)


"""
输入年份 如果是闰年输出True 否则输出False

Version: 0.1
Author: 骆昊
Date: 2018-02-27
"""
def year():
    year = int(input("请输入年份"))
    is_leap = (year % 4 == 0 and year % 100 != 0 or
               year % 400 == 0)
    print(is_leap)

"""
字符串常用操作

Version: 0.1
Author: 骆昊
Date: 2018-02-27
"""
def str():
    str1 = 'hello, world!'
    print('字符串的长度是:', len(str1))
    print('单词首字母大写: ', str1.title())
    print('字符串变大写: ', str1.upper())
    # str1 = str1.upper()
    print('字符串是不是大写: ', str1.isupper())
    print('字符串是不是以hello开头: ', str1.startswith('hello'))
    print('字符串是不是以hello结尾: ', str1.endswith('hello'))
    print('字符串是不是以感叹号开头: ', str1.startswith('!'))
    print('字符串是不是一感叹号结尾: ', str1.endswith('!'))
    str2 = '- \u9a86\u660a'
    str3 = str1.title() + ' ' + str2.lower()
    print(str3)

"""
格式化输出
Version: 0.1
Author: 骆昊
Date: 2018-02-27
"""
def str_input():
    str1 = 'hello, world!'
    print('字符串的长度是:', len(str1))
    print('单词首字母大写: ', str1.title())
    print('字符串变大写: ', str1.upper())
    # str1 = str1.upper()
    print('字符串是不是大写: ', str1.isupper())
    print('字符串是不是以hello开头: ', str1.startswith('hello'))
    print('字符串是不是以hello结尾: ', str1.endswith('hello'))
    print('字符串是不是以感叹号开头: ', str1.startswith('!'))
    print('字符串是不是一感叹号结尾: ', str1.endswith('!'))
    str2 = '- \u9a86\u660a'
    str3 = str1.title() + ' ' + str2.lower()
    print(str3)


"""
检查变量的类型

Version: 0.1
Author: 骆昊
Date: 2018-02-27
"""
def leixing():
    a = 100
    b = 1000000000000000000
    c = 12.345
    d = 1 + 5j
    e = 'A'
    f = 'hello, world'
    g = True
    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))
    print(type(e))
    print(type(f))
    print(type(g))
"""
类型转换

Version: 0.1
Author: 骆昊
Date: 2018-02-27
"""

if __name__ == "__main__":

