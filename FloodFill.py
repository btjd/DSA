from random import randint

def flood_fill(bitmap, start):
    x = start[1]
    y = start[0]
    zero = 0
    one = 1
    _flood_fill(bitmap, x, y, zero, one)

def _flood_fill(bitmap, x, y , zero, one):
    height = len(bitmap)
    width = len(bitmap[0])
    # Base case
    if bitmap[x][y] != zero:
        return
    else:
        bitmap[x][y] = one
    if x > 0:
        _flood_fill(bitmap, x-1, y, zero, one)
    if x < width - 1:
        _flood_fill(bitmap, x+1, y, zero, one)
    if y > 0:
        _flood_fill(bitmap, x, y-1, zero, one)
    if y < height - 1:
        _flood_fill(bitmap, x, y+1, zero, one)

# Create 5 x 5 bitmap
bmap = [[randint(0, 1) for x in range(5)] for y in range(5)]
print "Original: ", bmap
# s = [1, 2]
# Pick random starting coordinate in [row, col] format
s = [randint(0, len(bmap[0])-1), randint(0, len(bmap)-1)]
print "Starting at coordinates row = %d, col = %d: " % (s[1], s[0])
flood_fill(bmap, s)
print "Filled: ", bmap