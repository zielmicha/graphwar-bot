from __future__ import division
import os

def join_func(a, b):
    # ' f: (x<0: a(x)), (x=0: 0), (x>0: b(x)) '
    return '((abs(x)-x)^0.00001 * (%s) + (abs(x)+x)^0.00001 * (%s))' % (a, b)

def plot(f):
    os.system('kmplot -f \'f(x)=%s\' >/dev/null 2>&1' % f)

def move_right(a, x):
    return a.replace('x', '(x-(%s))' % x)

def move_up(a, y):
    return '(%s+(%s))' % (a, y)

def polygon(points):
    if len(points) == 2:
        (x0, y0), (x1, y1) = points
        a = ((y1-y0)/(x1-x0))
        return move_up(move_right('%s*x' % a, x0), y0)
    else:
        curr = points[0]
        next = points[1]
        rest = [ (p[0]-next[0], p[1]-next[1]) for p in points[1:] ]
        right_side = polygon(rest)
        currm = curr[0]-next[0], curr[1]-next[1]
        left_side = polygon([currm, (0,0)])
        return move_right(move_up(join_func(left_side, right_side), next[1]), next[0])

if __name__ == '__main__':
    poly = [(1, 1), (2, 2), (3, 2), (5, 5), (6, -2), (10, 5)]
    fun = polygon(poly)
    print fun
    plot(fun)
