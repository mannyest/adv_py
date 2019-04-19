

def doubleit(arg):
    if not isinstance(arg, (int, float)):
        raise TypeError
    darg = arg * 2
    return darg


def halveit(arg):
    harg = arg / 2
    return arg


