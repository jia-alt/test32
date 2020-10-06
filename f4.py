from random import randint as r
from fractions import Fraction as f
import argparse
def creat_formula():    #功能四生成随机式子
     ops = ['+', '-', '*', '/']
     n1 = r(1, 9)      #产生随机数
     n2 = r(1, 9)
     n3 = r(1, 9)
     n4 = r(1,9)
     o1 = r(0, 2)
     o2 = r(0, 3)
     o3 = r(0, 3)
     dic = {
         0: '(' + str(n1) + ops[o1] + '(' + str(n2) + ops[o2] + str(n3) + ')' + ')' + ops[o3] + str(n4),
         1: '(' + str(n1) + ops[o1] + str(n2) + ')' + ops[o2] + str(n3) + ops[o3] + str(n4),
         2: str(n1) + ops[o1] + str(n2) + ops[o2] + '(' + str(n3) + ops[o3] + str(n4) + ')',
         3: str(n1) + ops[o1] + '(' + '(' + str(n2) + ops[o2] + str(n3) + ')' + ops[o3] + str(n4) + ')',
         4: '(' + '(' + str(n1) + ops[o1] + str(n2) + ')' + ops[o2] + str(n3) + ')' + ops[o3] + str(n4),
         5: str(n1) + ops[o1] + '(' + str(n2) + ops[o2] + '(' + str(n3) + ops[o3] + str(n4) + ')' + ')',
         6: str(n1) + ops[o1] + '(' + str(n2) + ops[o2] + str(n3) + ops[o3] + str(n4) + ')',
         7: '(' + str(n1) + ops[o1] + str(n2) + ops[o2] + str(n3) + ')' + ops[o3] + str(n4),
         8: '(' + str(n1) + ops[o1] + str(n2) + ')' + ops[o2] + '(' + str(n3) + ops[o3] + str(n4) + ')',
         9: str(n1) + ops[o1] + '(' + str(n2) + ops[o2] + str(n3) + ')' + ops[o3] + str(n4), }
     test = r(0, 9)
     eqa = dic[test]
     return (eqa)
def _count(equa):                #计算式子值函数
     result = f(eval(equa)).limit_denominator(1000)   #利用eval函数计算式子的值,并将小数转化为分数
     result = str(result)
     return(result)
def _equations():    #功能一生成随机式子
        ops = ['+', '-', '*', '/']
        n1 = r(1, 9)      #产生随机数
        n2 = r(1, 9)
        n3 = r(1, 9)
        n4 = r(1, 9)
        o1 = r(0, 2)
        o2 = r(0, 3)
        o3 = r(0, 3)
        equa = str(n1) + ops[o1] + str(n2) + \
         ops[o2] + str(n3) + \
         ops[o3] + str(n4)
        return (equa)
def _input():             #控制输入
            num = 0
            n = 0
            for i in range(20):            #循环20道题
                eqa =  _equations()
                print(eqa, "=")
                result_right =  _count(eqa)  #
                answer = input("?")                 #接收输入的数
                if answer == result_right:
                    print("答对了，你真是个天才！")
                    num = num + 1
                else:
                    print("再想想吧，答案似乎是", result_right, "喔！")
                    n = n + 1
            print("你一共答对", num, "道题，一共20道题。")
def function_four(x):
        try:
            x = int(x)
            if x >= 0:
                for i in range(x):
                    result_right = creat_formula()
                    _right =  _count(result_right)
                    result_right = result_right + "="
                    print(result_right.ljust(40), _right)
            else:
                print('题目的数量必须是 正整数')
        except:
            print('题目的数量必须是 正整数')
        return (0)
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--cin")
    args = parser.parse_args()
    if args.cin == None:
        _input()  # 功能一入口
    else:
        function_four(args.cin)  # 功能四入口

