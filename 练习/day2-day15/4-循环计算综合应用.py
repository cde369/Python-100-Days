"""
求解《百钱百鸡》问题
1只公鸡5元 1只母鸡3元 3只小鸡1元 用100元买100只鸡
问公鸡 母鸡 小鸡各有多少只

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""
import random


def chicken():
    for x in range(0, 20):
        for y in range(0, 33):
            z = 100 - x - y
            if 5 * x + 3 * y + z / 3 == 100:
                print(f"公鸡有{x}只，母鸡有{y}只，小鸡有{z}只")


"""
Craps赌博游戏
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次要色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""
from random import randint


def craps():
    money = 1000  # 本金
    needs_go_on = False
    while True:  # 判断下注金额是否满足条件
        debt = int(input('请下注: '))
        if 0 < debt <= money:
            break
    first = randint(1, 6) + randint(1, 6)
    print('玩家摇出了%d点' % first)
    if first == 7 or first == 11:
        print('玩家胜!')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜!')
        money -= debt
    else:
        needs_go_on = True
    while needs_go_on:
        current = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % current)
        if current == 7:
            print('庄家胜')
            money -= debt
            needs_go_on = False
        elif current == first:
            print('玩家胜')
            money += debt
            needs_go_on = False


"""
输出斐波那契数列的前20个数
1 1 2 3 5 8 13 21 ...

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""


def fibonacci():
    a = 0
    b = 1
    for _ in range(20):
        a, b = b, a + b
        print(a)


"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""
import random


def guess():
    answer = random.randint(1, 100)
    counter = 0
    while True:
        counter += 1
        number = int(input('请输入: '))
        if number < answer:
            print('大一点')
        elif number > answer:
            print('小一点')
        else:
            print('恭喜你猜对了!')
            break
    print('你总共猜了%d次' % counter)
    if counter > 7:
        print('你的智商余额明显不足')


"""
找出100~999之间的所有水仙花数
水仙花数是各位立方和等于这个数本身的数
如: 153 = 1**3 + 5**3 + 3**3

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""


def lily():
    for x in range(100, 1000):
        low = x % 10
        mid = x // 10 % 10
        high = x // 100
        if x == low ** 3 + mid ** 3 + high ** 3:
            print(x)


"""
输出乘法口诀表(九九表)

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""
def rabel():
    for x in range(1,10):
        for y in range(1,x+1):
            print(f"{x}*{y} = {x*y}",end="\t")
        print("")
if __name__ == "__main__":
    rabel()
