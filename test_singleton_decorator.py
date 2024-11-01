from singleton_decorator import SingletonDecorator

@SingletonDecorator
class MyClass:
    name = ''
    @staticmethod
    def test_static_method(name):
        print(name)
        
    @classmethod
    def test_class_method(cls, name):
        cls.name = name
        print(cls.name)
        
    def test_instance_method(self, name):
        print(name)
        MyClass.test_class_method('call the class method from an instance method')
        MyClass.test_static_method('call the static method from an instance method')


def test_singleton_decorator():
    mc = MyClass()
    MyClass.test_class_method("test class method")
    MyClass.test_static_method('test static class')
    mc.test_instance_method('test instance method')


if __name__ == "__main__":
    test_singleton_decorator()
