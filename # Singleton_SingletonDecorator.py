# Singleton/SingletonDecorator.py
class SingletonDecorator:
    def __init__(self,klass):
        self.klass = klass
        self.instance = None
        print "call init"
    def __call__(self,*args,**kwds):
    	print "call __call__"
        if self.instance == None:
            self.instance = self.klass(*args,**kwds)
        return self.instance
@SingletonDecorator
class foo: pass
#foo = SingletonDecorator(foo)


print "======"
x=foo()
y=foo()
z=foo()
x.val = 'sausage'
y.val = 'eggs'
z.val = 'spam'
print(x.val)
print(y.val)
print(z.val)
print(x is y is z)