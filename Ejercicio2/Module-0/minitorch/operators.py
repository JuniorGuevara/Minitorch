import numpy as np
#  Task 0.1
#  Mathematical operators


def mul(x, y):
    ":math:`f(x, y) = x * y`"
    # TODO: Implement for Task 0.1.
    return x * y
    raise NotImplementedError('Need to implement for Task 0.1')


def id(x):
    ":math:`f(x) = x`"
    # TODO: Implement for Task 0.1.
    return x
    raise NotImplementedError('Need to implement for Task 0.1')


def add(x, y):
    ":math:`f(x, y) = x + y`"
    # TODO: Implement for Task 0.1.
    return x + y
    raise NotImplementedError('Need to implement for Task 0.1')


def neg(x):
    ":math:`f(x) = -x`"
    # TODO: Implement for Task 0.1.
    return -x
    raise NotImplementedError('Need to implement for Task 0.1')


def lt(x, y):
    ":math:`f(x) =` 1.0 if x is less than y else 0.0"
    # TODO: Implement for Task 0.1.
    return 1.0 if x < y else 0.0
    raise NotImplementedError('Need to implement for Task 0.1')


def eq(x, y):
    ":math:`f(x) =` 1.0 if x is equal to y else 0.0"
    # TODO: Implement for Task 0.1.
    return 1.0 if x == y else 0.0
    raise NotImplementedError('Need to implement for Task 0.1')


def max(x, y):
    ":math:`f(x) =` x if x is greater than y else y"
    # TODO: Implement for Task 0.1.
    return x if x > y else y
    raise NotImplementedError('Need to implement for Task 0.1')


def sigmoid(x):
    r"""
    :math:`f(x) =  \frac{1.0}{(1.0 + e^{-x})}`

    (See `<https://en.wikipedia.org/wiki/Sigmoid_function>`_ .)

    Calculate as

    :math:`f(x) =  \frac{1.0}{(1.0 + e^{-x})}` if x >=0 else
    :math:`\frac{e^x}{(1.0 + e^{x})}`

    for stability.

    """
    # TODO: Implement for Task 0.1.
    return 1 / 1 - np.exp(-x)
    raise NotImplementedError('Need to implement for Task 0.1')


def relu(x):
    """
    :math:`f(x) =` x if x is greater than 0, else 0

    (See `<https://en.wikipedia.org/wiki/Rectifier_(neural_networks)>`_ .)
    """
    # TODO: Implement for Task 0.1.
    return x if x > 0 else 0
    raise NotImplementedError('Need to implement for Task 0.1')


def relu_back(x, y):
    ":math:`f(x) =` y if x is greater than 0 else 0"
    # TODO: Implement for Task 0.1.
    return y if x > 0 else 0
    raise NotImplementedError('Need to implement for Task 0.1')


EPS = 1e-6


def log(x):
    ":math:`f(x) = log(x)`"
    return np.log(x + EPS)


def exp(x):
    ":math:`f(x) = e^{x}`"
    return np.exp(x)


def log_back(a, b):
    return b / (a + EPS)


def inv(x):
    ":math:`f(x) = 1/x`"
    return 1.0 / x


def inv_back(a, b):
    return -(1.0 / a ** 2) * b


# Task 0.3
# Higher-order functions.


def map(fn):
    """
    Higher-order map.

    .. image:: figs/Ops/maplist.png


    See `<https://en.wikipedia.org/wiki/Map_(higher-order_function)>`_

    Args:
        fn (one-arg function): process one value

    Returns:
        function : a function that takes a list and applies `fn`
                   to each element
    """
    # TODO: Implement for Task 0.3.
    def fn_map(ls):
        new_ls = []
        for value in ls:
            new_ls.append(fn(value))
        return new_ls

    return lambda ls: fn_map(ls)
    raise NotImplementedError('Need to implement for Task 0.3')


def negList(ls):
    "Use :func:`map` and :func:`neg` to negate each element in `ls`"
    return map(neg)(ls)


def zipWith(fn):
    """
    Higher-order zipwith (or map2).

    .. image:: figs/Ops/ziplist.png

    See `<https://en.wikipedia.org/wiki/Map_(higher-order_function)>`_

    Args:
        fn (two-arg function): combine two values

    Returns:
        function : takes two equally sized lists `ls1` and `ls2`, produce
        a new list by applying fn(x, y) one each pair of elements.

    """
    # TODO: Implement for Task 0.3.
    def fn_map(iterable_l1, iterable_l2):
        new_ls = []
        for value_1, value_2 in zip(iterable_l1, iterable_l2):
            new_ls.append(fn(value_1, value_2))
        return new_ls

    return lambda l1, l2: fn_map(l1, l2)
    raise NotImplementedError('Need to implement for Task 0.3')


def addLists(ls1, ls2):
    "Add the elements of `ls1` and `ls2` using :func:`zipWith` and :func:`add`"
    return zipWith(add)(ls1, ls2)


def reduce(fn, start):
    r"""
    Higher-order reduce.

    .. image:: figs/Ops/reducelist.png


    Args:
        fn (two-arg function): combine two values
        start (float): start value :math:`x_0`

    Returns:
        function : function that takes a list `ls` of elements
        :math:`x_1 \ldots x_n` and computes the reduction
        :math:`fn(x_3, fn(x_2, fn(x_1, x_0)))`

    """
    # TODO: Implement for Task 0.3.
    def fn_reduce(ls):
        it = iter(ls)
        if start is None:
            value = next(it)
        else:
            value = start
        for element in it:
            value = fn(value, element)
        return value

    return lambda ls: fn_reduce(ls)
    raise NotImplementedError('Need to implement for Task 0.3')


def sum(ls):
    """
    Sum up a list using :func:`reduce` and :func:`add`.
    """
    # TODO: Implement for Task 0.3.
    return reduce(add, 0)(ls)
    raise NotImplementedError('Need to implement for Task 0.3')


def prod(ls):
    """
    Product of a list using :func:`reduce` and :func:`mul`.
    """
    # TODO: Implement for Task 0.3.
    return reduce(mul, 1)(ls)
    raise NotImplementedError('Need to implement for Task 0.3')
