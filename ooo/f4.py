from random import randint as r
from fractions import Fraction as f
import argparse
def _formula():  # 生成随机式子
    ops = ['+', '-', '*', '/']
    n1 = r(1, 9)  # 产生随机数
    n2 = r(1, 9)
    n3 = r(1, 9)
    n4 = r(1, 9)
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
def run_count(eq):           #计算式子值函数
    result = f(eval(eq)).limit_denominator(1000)   #利用eval函数计算式子的值
    result = str(result)
    return(result)
def out_input():             #控制输入
            num = 0
            n = 0
            for i in range(20):            #循环20道题
                eqa = _formula()
                print(eqa, "=")
                result_right = run_count(eqa)  #
                answer = input("?")                 #接收输入的数
                if answer == result_right:
                    print("答对了，你真是个天才！")
                    num = num + 1
                else:
                    print("再想想吧，答案似乎是", result_right, "喔！")
                    n = n + 1
            print("你一共答对", num, "道题，一共20道题。")
def input_count(n):
          try:
            n = int(n)
            if n >= 0:
                data = open("result.txt", 'w+')
                for i in range(n):
                    eqa = _formula()
                    result_right = run_count(eqa)
                    eqa = eqa + "="
                    print(eqa.ljust(40), result_right,file=data)
                data.close()
            else:
                print('题目的数量必须是 正整数')
          except:
              print('题目的数量必须是 正整数')
          return(0)
if __name__ == "__main__":
       parser = argparse.ArgumentParser()
       parser.add_argument("-c", "--cin")
       args = parser.parse_args()
       if args.cin == None:
           out_input()
       else:
          input_count(args.cin)