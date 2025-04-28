class A:
    def f(self):
        if False and True:
            print("NO")
        elif not False or False:
            print("YES")
        else:
            print("MAYBE")
a = A()
if print("Hi") is None:
    a.f()
else:
    print("42")
a.f2 = lambda x: x + 1
print(a.f2(41) in [1,2,42])

