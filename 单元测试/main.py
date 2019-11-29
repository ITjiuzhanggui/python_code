from calculate import mySum, myDel


def main():
    x = 1
    y = 2

    res1 = mySum(x, y)
    if res1 == x + y:
        print("res1 = %d" % res1)
    else:
        print("加法计算有误")

    res2 = myDel(x, y)
    if res2 == x - y:
        print("res2 = %d" % res2)
    else:
        print("减法计算有误")


if __name__ == '__main__':
    main()
