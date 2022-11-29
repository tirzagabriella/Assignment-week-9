#number 1
class object:
    pass

class X(object):
    pass

class Y(object):
    pass

class Z(object):
    pass

class A(X,Y):
    pass

class B(Y,Z):
    pass

class M(B,A,Z):
    pass
