def clear_bit(x, position):
    # mask is 00100000
    mask = 1 << position
    print "Mask is :", bin(mask)
    return x & ~mask

def set_bit(x, position):
    mask = 1 << position
    return x | mask

def flip_bit(x, position):
    mask = 1 << position
    return x ^ mask


x = 00000110
print bin(clear_bit(x, 5))
print bin(set_bit(x, 5))
print bin(flip_bit(x, 5))
