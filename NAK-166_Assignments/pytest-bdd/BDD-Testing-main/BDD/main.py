def incrementor(val: int):
    def f(x: int):
        return val + x
    return f
    