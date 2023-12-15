"""
用for循环实现1~100求和

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""


def sum_100():
    sm = 0
    for i in range(101):
        sm += i
    print(sm)


"""
用for循环实现1~100之间的偶数求和

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""


def sum_100_2():
    sm = 0
    for i in range(101):
        if i % 2 == 0:
            sm += i
    print(sm)


"""
输入非负整数n计算n!

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""


def com():
    U = 1
    n = int(input("请输入一个非负整数:"))
    if n > 0:
        for x in range(1, n + 1):
            U *= x
    else:
        print("输入数据有误！！")
    print(f"n！={U}")


"""
打印各种三角形图案

*   
**
***
****
*****

    *
   **           第i行前面有 总行数-i 个空格 i个*
  ***
 ****
*****

    *          每行空格数量为 4 3 2 1 0    即 f（0） = 4  f（1）= 3  row-i-1
   ***          
  *****
 *******
*********

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""


def Print_triangle():
    row = int(input('请输入行数: '))

    for i in range(row):
        for _ in range(i):
            print('*', end='')
        print("")

    for i in range(row):  # 控制行
        for j in range(row):  # 控制列输出
            if j < row - i - 1:
                print(' ', end='')
            else:
                print('*', end='')
        print("")

    for i in range(row):
        for _ in range(row - i - 1):
            print(' ', end='')
        for _ in range(2 * i + 1):
            print('*', end='')
        print()


"""
用while循环实现1~100求和

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""


def sum_100_while():
    x = 1
    sums = 0
    while x <= 100:
        sums += x
        x += 1
    print(sums)
"""
用while循环实现1~100之间的偶数求和

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""
def sum_100_while2():
    x = 2
    sums = 0
    while x <= 100:
        sums += x
        x += 2
    print(sums)
if __name__ == "__main__":
    sum_100_while2()
