class GopherStr(str):
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        if isinstance(other, GopherStr):
            return GopherStr(self.val + other.val)
        else:
            return GopherStr(self.val + str(other))
    
    def __str__(self):
        return self.val
    
    def __float__(self):
        return float(self.val)
    
    def __mul__(self, other):
        return GopherStr(other * self.val)


class GopherNum(float):
    def __init__(self, al):
        
