def printlist(lis, tab='', end='\n'):
    print(tab+"[")
    for item in lis['val']:
        printitem(item, end='', tab=tab+'\t')
        print(',')
    print(tab+"]", end=end)


def printitem(item, end='\n', tab='') -> (None, int):
    try:
        fmstr = tab+"{0}"
        if item['type'] == "list":
            printlist(item, tab=tab, end=end)
        elif item['type'] == "float":
            if item["val"] == int(item["val"]):
                print(fmstr.format(int(item["val"])), end=end)
            else:
                print(fmstr.format(item["val"]), end=end)
        elif item['type'] == 'null':
            print(fmstr.format('null'), end=end)
        elif item['type'] == 'bool':
            print(fmstr.format(str(item['val']).lower()), end=end)
        elif item['type'] in ['any', 'str']:
            print(fmstr.format(item['val']), end=end)
        else:
            return 12
    except:
        return 12


def pythonify_lis(lis: list):
    ret = []
    for i in lis:
        ret.append(i['val'])
    return ret
