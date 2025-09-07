class C:

        def foo(x, y):
            print "staticmethod", x, y
        foo = staticmethod(foo)

    C.foo(1, 2)
    c = C()
    c.foo(1, 2)
