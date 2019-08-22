import Gophisitor
from GopherTypes import *
ftype = {'float': float,
         'str': str,
         'bool': bool,
         'list': list,
         'any': (lambda x: x)}


def cnvrt(self: Gophisitor, val: dict, dt: str):
    retval = GopherNoVal()
    try:
        t = self.memory['this']
    except KeyError:
        pass
    try:
        self.memory['this'] = val
        retval = self.visit(val['__'+dt]['call']['block'])
        self.memory.pop('this')
    except KeyError:
        if dt in ftype.keys():
            retval = {'val': ftype[dt](val['val']), 'type': dt}
        elif val['type'] == dt:
            retval = val
        else:
            raise TypeError(f'can\'t convert {val["type"]} to {dt}')
            
    try:
        self.memory['this'] = t
    except:
        pass
    return retval


def assgn(self: Gophisitor, value: dict, id: str, dt: str, const=None):
    if (value['type'] != dt) and (dt != 'any'):
        value = cnvrt(self, value, dt)
    elif dt == 'any':
        value['type'] = dt
    try:
        isconst = self.memory[id]['const']
        if isconst:
            raise Exception('can\'t assign value to const')
        else:
            self.memory[id] = value
            return value
    except:
        self.memory[id] = value
        if const != None:
            self.memory[id]['const'] = True
        return value
