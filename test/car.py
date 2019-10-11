"""一个可用于表示汽车的类"""


class Car(object):
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性名称"""
        long_name = str(self.year) + " " + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条消息，指出汽车的里程"""
        print("This car has %d miles on it." % self.odometer_reading)

    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        拒绝将里程表往回拨
        """
        # if mileage >= self.odometer_reading:
        #     self.odometer_reading = mileage
        # else:
        #     print("You can't roll back an odometer!")
        self.odometer_reading = mileage \
            if mileage >= self.odometer_reading \
            else print(
                "You can't roll back an odometer!"
            )

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles


"""一组用于表示燃油汽车和电动汽车的类"""


class Battery():
    """一次模拟电动汽车的简单尝试"""

    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a %s -KWh battery." % self.battery_size)

    def get_range(self):
        """打印一条描述电瓶续航里程的消息"""
        if self.battery_size == 70:
            range = 240

        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately %s" % range + " "
        message += "miles on a full charge."
        print(message)



