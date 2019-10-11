from six import add_metaclass
from abc import ABCMeta, abstractmethod, abstractproperty


@add_metaclass(ABCMeta)
class TestAll():
    @abstractproperty
    def k(self):
        pass

    @abstractmethod
    def v(self):
        pass

    def c(self):
        print("this is not abstract !")


class T(TestAll):
    k = "this is abstract abstract property"

    def v(self):
        print(self.k)
        print("this is abstract method!")


# Can't instantiate abstract class TestAll with abstract methods k, v
# TestAll()  # it is error
t = T()
t.v()
