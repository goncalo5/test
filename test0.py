class FooBase(object):
    def __init__(self): pass

class A(FooBase):
    def __init__(self, **kwargs):
        # super().__init__()
        print('A.__init__()', kwargs)

class B(FooBase):
    def __init__(self, **kwargs):
        # super().__init__()
        print('B.__init__()', kwargs)

class C(A, B):
    def __init__(self, **kwargs):
        # super().__init__(**kwargs)
        A.__init__(self, **kwargs)
        B.__init__(self, **kwargs)
        print('C.__init__()', kwargs)

C(a=1)