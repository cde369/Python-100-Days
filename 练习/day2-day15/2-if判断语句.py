"""
分段函数求值
        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)

Version: 0.1
Author: 骆昊
Date: 2018-02-28
"""


def Piecewise_function_evaluation():
    x = float(input("请输入x的值:"))
    if x > 1:
        F = 3 * x - 5
    elif -1 <= x <= 1:
        F = x + 2
    else:
        F = 5 * x + 3
    print(f"f(x) = {F}")



if __name__ == "__main__":
    Piecewise_function_evaluation()