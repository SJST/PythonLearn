# coding : utf-8
# 连接 unittest
import unittest


# 使用unittest 必须 继承unittest
# 创建测试类
import unittest


# 使用unittest 必须 继承unittest
# 创建测试类
class Test(unittest.TestCase):
    # 定义类方法 类方法只会执行一次
    @classmethod
    def setUpClass(cls):
        print("这是类执行之前的方法")

    @classmethod
    def tearDownClass(cls):
        print("这是类执行之后的方法")

    # 创建测试之前的方法 setup
    def setUp(self):
        print('test -> setup')
        pass

    # 创建测试之后的方法
    def tearDown(self):
        print('test -> tearDown')
        pass

    # 创建第一个case 如果 case不是test 开头 则 不能执行case
    def test_01(self):
        print("这是个测试方法")

    def test_02(self):
        print("这是第二个测试方法")


if __name__ == '__main__':
    unittest.main()

# class TestMethod(unittest.TestCase):
#     # 创建第一个case 如果 case不是test 开头 则 不能执行case
#     def test_01(self):
#         print("这是个测试方法")
#
#     def test_02(self):
#         print("这是第二个测试方法")
#
#
# if __name__ == '__main__':
#     unittest.main()
