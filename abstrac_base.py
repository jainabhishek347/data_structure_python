from abc import ABCMeta,abstractmethod
class Foo(object):
    def __getitem__(self, index):
        print "foo __getitem__"

    def __len__(self):
        print "foo __len__"

    def get_iterator(self):
        print "foo get_iterator"
        return iter(self)

class MyIterable:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __iter__(self):
        while False:
            yield None

    def get_iterator(self):
        print "MyIterable get_iterator"
        return self.__iter__()

    @classmethod
    def __subclasshook__(cls, C):
        if cls is MyIterable:
            if any("__iter__" in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented

MyIterable.register(Foo)
obj = Foo()
print obj.get_iterator()