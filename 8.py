
import abc


class GetterSetter():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def set_val(self, value):
        return

    @abc.abstractmethod
    def get_val(self):
        return


class MyClass(GetterSetter):

    def set_val(self, value):
        self.val = value

    def get_val(self):
        return self.val


x = MyClass()
print(x)


