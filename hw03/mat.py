def readm(fname='A.csv'):
    f = open(fname, 'r') # w, b
    A = []
    for line in f.readlines():
        A.append( [ float(x) for x in line.strip().split(',') ] )
    f.close()
    return A

def printm(m):
    for row in m:
        print(' '.join([ f'{x:5.2}' for x in row ]) )
