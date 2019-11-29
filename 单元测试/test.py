import unittest
from .calculate import myDel, mySum


class Test(unittest.TestCase):
    def setUp(self):
        print("开始测试......")

    def tearDown(self):
        print("结束测试......")

    # 测试函数名 === test_待测函数名
    def test_mySum(self):
        self.assertEqual(mySum(1, 2), 3)

    def test_myDel(self):
        self.assertEqual(myDel(1, 2), -1)


if __name__ == '__main__':
    unittest.main()
