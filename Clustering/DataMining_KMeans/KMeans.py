#!/usr/local/bin/python3

'''
 ********************************************
 * Description : 
 * Date        : 2018-10-16
 * Author      : liuyy
 * E-mail      : yyliu@dmo-sys.com
 ********************************************
'''

from functools import reduce

def calc_center(l):
    p = reduce(lambda x, y: (x[0] + y[0], x[1] + y[1]), l)
    return (p[0] / len(l), p[1] / len(l))

def dist(a, b):
    return (a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1])

def iterate(ps, points):
    res = [[i[0]] for i in ps]
    
    for p in points:
        min_dist = dist(p, res[0][0])
        min_class = res[0]

        for i in res:
            d = dist(p, i[0])
            if d < min_dist:
                min_dist = d
                min_class = i
        
        min_class.append(p)

    return res

def init(f):
    points = []

    with open(f) as fp:
        line = fp.readline()

        while len(line) != 0:
            (x, y) = line.rstrip().split()
            points.append((int(x), int(y)))

            line = fp.readline()

    return points

first_ps = [[(0, 0)], [(10, 10)]]
points = init("input.txt")
res = []

for i in range(10):
    res = iterate(first_ps, points)
    first_ps = [[calc_center(i[1:])] for i in res]


print(res)
