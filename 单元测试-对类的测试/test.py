import unittest
from myDict import MyDict


# test+ 代测试的类名
class TestMyDict(unittest.TestCase):
    def setUp(self):
        print("开始测试...")

    def tearDown(self):
        print("结束测试...")

    # 一般对类的测试有个(实例化阶段）
    def test_init(self):
        d = MyDict(a=1, b=2)
        # 断言
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 2)
        self.assertTrue(isinstance(d, dict))

    # 测试属性
    def test__attr(self):
        d = MyDict()
        d.key = "value"
        self.assertTrue("key" in d)
        self.assertEqual(d["key"], "value")

    # 判断
    def test_keyerror(self):
        d = MyDict()
        # 通过d["key"]访问不存在的属性抛出KeError异常
        with self.assertRaises(KeyError):
            value = d["key"]


 if __name__ == '__main__':
     unittest.main()
