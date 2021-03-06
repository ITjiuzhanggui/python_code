from .test_nu import get_formatted_name

"""
11.1.1 单元测试和测试用例
"""
import unittest


class NamesTestCase(unittest.TestCase):
    """
    测试name_function.py
    """

    def test_first_last_name(self):
        """
        能够正确地处理像Janis Joplinz这样的姓名吗？
        :return:
        """
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEquals(formatted_name, 'Janis Joplin')


unittest.main()
