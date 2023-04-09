class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size


mp = MaxPooling(step=(2, 2), size=(2, 2))
res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])  # [[6, 8], [9, 7]]
