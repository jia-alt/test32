# coding=gbk
import unittest
import f4
class JustforTest(unittest.TestCase):
 # 测试功能1
    def test_calc(self):
        print(" _input()函数单元测试开始：")
        self.assertEqual(None, f4._input())
        print('\n答对啦，你真是个天才')
# 测试功能4
    def test_f4_integer_parser(self):
        print("function_four函数单元测试开始：")
        x = input("输入命令行参数：")
        self.assertEqual(0,f4.function_four(x))
        print("function_four函数单元测试结束。")
if __name__ == '__main__':
    unittest.main()