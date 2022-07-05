
def size(cms):
    if cms < 38:
        return 'S'
    elif cms >= 38 and cms <= 42:
        return 'M'
    elif cms>=42 and cms<=45:
        return 'L'
    else cms >= 45 and cms <= 48:
        return 'XL'
    else:
        return "Invalid size"
 
def test_tshirt_size():
    assert(size(37) == 'S')
    assert(size(38) == 'M')
    assert(size(40) == 'M')
    assert(size(42) == 'M')
    assert(size(43) == 'L')
    assert(size(45) == 'XL')
    assert(size(100) == 'Invalid size')


test_tshirt_size()
print("All is well")
