class ItemAttrs:
    def __getitem__(self, k):
        d = list(self.__dict__.values())
        return d[k]

    def __setitem__(self, k, v):
        d = list(self.__dict__.keys())
        d[k] = v
        # setattr(self, d[k], v)


class Point(ItemAttrs):
    def __init__(self, x, y):
        self.x = x
        self.y = y


pt = Point(1, 2.5)
x = pt[0]  # 1
y = pt[1]  # 2.5
pt[0] = 10
print(*filter(lambda x: x.startswith(('__geti', '__seti')), dir(ItemAttrs)))  # __getitem__ __setitem__
