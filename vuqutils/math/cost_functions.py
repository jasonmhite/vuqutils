import numpy as np
import collections

__all__ = ['add_ssq']

def add_ssq(Y):
    """Take a function f(x) and add a sum-of-squares method. x can be
    any type, e.g. a vector, scalar, namedtuple etc.

    Will add a method f.ssq(X), where X is expected to be an iterable
    with iterates of the same type as x.

    f: function to decorate
    Y: reference value(s), must be able to subtract f(x) - Y
    """

    def attach_ssq(f):
        def ssq(X):
            if isinstance(X, collections.Iterable):
                Yh = Y - np.array([f(xi) for xi in X])
            else: 
                Yh = Y - f(X)
            ss = ((Y - Yh) ** 2).sum(axis=0)
            return(ss)

        f.ssq = ssq
        return(f)

    return(attach_ssq)

