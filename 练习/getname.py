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


while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break

    last = input("\nPlease give me a last name: ")
    if last == 'q':
        break

    formatted_names = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_names + ".")