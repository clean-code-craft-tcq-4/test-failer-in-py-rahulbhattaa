
def size(cms):
    if cms < 38:
        return 'S'
    elif cms > 38 and cms < 42:
        return 'M'
    else:
        return 'L'

def size_define():
    assert(size(37) == 'S')
    assert(size(40) == 'M')
    assert(size(38) == 'M')
    assert(size(43) == 'L')

size_define()
print("All is well (maybe!)\n")
