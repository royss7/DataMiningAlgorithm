#!/usr/local/bin/python3

'''
 ********************************************
 * Description : 
 * Date        : 2018-10-12
 * Author      : liuyy
 * E-mail      : yyliu@dmo-sys.com
 ********************************************
'''
import math

def readfile(f, hasType = False):
    res = []
    
    with open(f) as fp:
        line = fp.readline()

        while line:
            line = line.rstrip()
            tmp = line.split()

            if hasType:
                res.append((tmp[0], [int(i) for i in tmp[1:]]))
            else:
                res.append([int(i) for i in tmp])
            
            line = fp.readline()
    return res

trained=readfile("trainInput.txt", hasType = True)
tested=readfile("testInput.txt")
print(tested)
print(trained)

def classify(case, trained):
    def dist(i, j):
        s = 0
        for v in zip(i, j):
            s += pow(v[0] - v[1], 2)

        return math.sqrt(s)

    return [(i[0], dist(case, i[1])) for i in trained]

def get_class(first_k):
    res = {}
    for i in first_k:
        if i[0] not in res:
            res[i[0]] = 0
        res[i[0]] += 1
    
    return sorted(res.items(), key = lambda x: x[1], reverse = True)[0]

for case in tested:
    ct = classify(case, trained)
    print(ct)
    first_k = sorted(ct, key = lambda i: i[1])[:3]
    print(str(case) + " " + str(get_class(first_k)))



