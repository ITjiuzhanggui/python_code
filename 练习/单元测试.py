"""
11.1 测试函数
"""


def get_formatted_name(first, last):
    """
    生成整洁的姓名
    :param first:
    :param last:
    :return:
    """
    full_name = first + ' ' + last
    return full_name.title()


# while True:
#     first = input("\nPlease give me a first name: ")
#     if first == 'q':
#         break
#
#     last = input("\nPlease give me a last name: ")
#     if last == 'q':
#         break
#
#     formatted_names = get_formatted_name(first, last)
#     print("\tNeatly formatted name: " + formatted_names + ".")

"""
11.1.1 单元测试和测试用例
"""
import unittest


class NamesTestCase(unittest.TestCase):
    """
    测试name_function.py
    """

    def test_fiirst_last_name(self):
        """
        能够正确地处理像Janis Joplinz这样的姓名吗？
        :return:
        """
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEquals(formatted_name, 'Janis Joplin')


unittest.main()

