# coding=gbk
import unittest
import f4
class JustforTest(unittest.TestCase):
 # ���Թ���1
    def test_calc(self):
        print(" _input()������Ԫ���Կ�ʼ��")
        self.assertEqual(None, f4._input())
        print('\n������������Ǹ����')
# ���Թ���4
    def test_f4_integer_parser(self):
        print("function_four������Ԫ���Կ�ʼ��")
        x = input("���������в�����")
        self.assertEqual(0,f4.function_four(x))
        print("function_four������Ԫ���Խ�����")
if __name__ == '__main__':
    unittest.main()