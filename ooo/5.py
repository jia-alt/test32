# coding=gbk
import unittest
import f4
import argparse
class JustforTest(unittest.TestCase):
 # ���Թ���2
    def test_calc(self):
        print(" out_input()������Ԫ���Կ�ʼ��")
        self.assertEqual(None, f4.out_input())
        print('\n������������Ǹ����')
# ���Թ���3
    def test_f4_integer_parser(self):
        print("input_count������Ԫ���Կ�ʼ��")
        x = input("���������в�����")
        self.assertEqual(0,f4.input_count(x))
        print("input_count������Ԫ���Խ�����")
if __name__ == '__main__':
    unittest.main()

