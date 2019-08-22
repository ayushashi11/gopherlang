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
        pass


class GopherNoVal:
    def __init__(self):
        pass

    def __delattr__(self):
        self.err()

    def __dir__(self):
        self.err()

    def __getattribute__(self, attr):
        if attr != 'err':
            print(attr)
            self.err()
        else:
            raise NotImplementedError("No value has yet been declared")

    def __setattr__(self, attr, val):
        self.err()

    def __str__(self):
        self._
    
    def __int__(self):
        self._

    def __repr__(self):
        self._
    
    def __sizeof__(self):
        self._
    
    def __bool__(self):
        return False
