#!/usr/local/bin/python3

'''
 ********************************************
 * Description : 
 * Date        : 2018-10-15
 * Author      : liuyy
 * E-mail      : yyliu@dmo-sys.com
 ********************************************
'''

def initprob(f):
    pre_pro = []
    classtypes = {}

    with open(f) as fp:
        line = fp.readline()
        line = fp.readline()

        while len(line) != 0:
            tmp = line.rstrip().split()[1:]

            classtype = tmp[-1]
            if classtype not in classtypes:
                classtypes[classtype] = 0
            classtypes[classtype] += 1

            tmp = tmp[:-1]
            if len(pre_pro) == 0:
                pre_pro = [{} for i in range(len(tmp))]

            for i in range(len(tmp)):
                attr = tmp[i]

                k = (attr, classtype)
                if k not in pre_pro[i]:
                    pre_pro[i][k] = 0
                pre_pro[i][k] += 1
    
            line = fp.readline()
    print(classtypes)
    res = [{k: v/classtypes[k[1]] for k, v in i.items()} for i in pre_pro]

    return (classtypes, res)

(cts, pre_prob) = initprob("input.txt")
for i in pre_prob:
    print(i)

def get_test(to_test, cts, pre_prob):
    def _get_test(tmp, pre_prob, ct):
        m = 1.0
        for i in range(len(tmp)):
            m *= pre_prob[i].get((tmp[i], ct), 1.0)

        return m
    
    values = to_test.split()
    re = [(_get_test(values, pre_prob, i), i) for i in cts.keys()]
    return max(re, key = lambda x: x[0])[1]

to_test = "Youth Medium Yes Fair"
print(to_test, end = ": ")
print(get_test(to_test, cts, pre_prob))
