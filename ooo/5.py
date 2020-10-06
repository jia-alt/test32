# coding=gbk
import unittest
import f4
import argparse
class JustforTest(unittest.TestCase):
 # 测试功能2
    def test_calc(self):
        print(" out_input()函数单元测试开始：")
        self.assertEqual(None, f4.out_input())
        print('\n答对啦，你真是个天才')
# 测试功能3
    def test_f4_integer_parser(self):
        print("input_count函数单元测试开始：")
        x = input("输入命令行参数：")
        self.assertEqual(0,f4.input_count(x))
        print("input_count函数单元测试结束。")
if __name__ == '__main__':
    unittest.main()

