# Singleton/SingletonPattern.py

class OnlyOne:
    class __OnlyOne:
        def __init__(self, arg):
            self.val = arg
        def __str__(self):
            #print "calling __str__"
            return repr(self) + self.val
    instance = None
    def __init__(self, arg):
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne(arg)
        else:
            OnlyOne.instance.val = arg

    def __getattr__(self, name):
    #    return self
        #return  "calling __getattr__",  self, name
        return getattr(OnlyOne.instance, name)

x = OnlyOne('sausage')
print(x)
#print(x.__getattr__('val'))
y = OnlyOne('eggs')
print(y)
z = OnlyOne('spam')
print(z)
print(x)
print(y)
print(`x`)
print(`y`)
print(`z`)
#output = '''
