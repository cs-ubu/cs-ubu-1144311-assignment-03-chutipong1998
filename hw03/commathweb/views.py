from django.shortcuts import render
from django.http import HttpResponse
import csv

# from mat import *
# import numpy as np 

# def readm(fname='A.csv'):
#     f = open(fname, 'r') # w, b
#     A = []
#     for line in f.readlines():
#         A.append( [ float(x) for x in line.strip().split(',') ] )
#     f.close()
#     return A

# def printm(m):
#     for row in m:
#         print(' '.join([ f'{x:5.2}' for x in row ]) )

# C = readm('A.csv')
# d = readm('b.csv')

# def solve(C, d):
#     import numpy as np
#     n = len(C[0])
#     x = np.array([0]*n)

#     # 1.elimination
#     for k in range(n-1): #pivot equation
#         for j in range(k+1, n): #eleminate eq j
#             lam = C[j][k]/C[k][k]
#             # update A[j][k เป็นต้นไป]
#             C[j][k] = C[j][k] - lam*C[k][k]
#             # C[j,k:n] = C[j,k:n] - lam*C[k,k:n]
#             # update b[j]
#             d[j] = d[j] - lam*d[k] 

#     # 2.back substitution
#     for k in range(n-1, -1, -1):
#         x[k] = (d[k] - np.dot(C[k,k+1:n], x[k+1:n]))/C[k,k]
    
#     return x.flatten()

# print( solve(C, d) )

# def index(req):
#     # แปลงเลขหน้าทศนิยมให้เป็น bit
#     try:
#         r = ''
#         d = req.GET.get('num')
#         d = float(d)
#         print(type(d))
        
#         nb = bin(int(d))
#         nb = nb[2:]
#         print(nb)
#         lung = d-int(d)   
#         while lung>0:
#             lung = lung*2
#             r += str(int(lung))
#             lung -= int(lung) 
#         print("r=",r)
        
#         e = len(nb)-1
#         s = '0' if d >= 0 else '1'
        
#         e += 127
#         bie = bin(e)
#         bie = bie[2:]
#         nbbilung = nb+r
#         nbbilung = nbbilung[1:]
#         b = s+bie+nbbilung
#         b = b + '0'*(32-len(b))
#         print(b)
#         result = {'answer':b}
#     except :
#         result = {'answer':"ข้อมูลไม่ถูกต้อง กรุณากรอกค่าใหม่"}
    
#     return render(req,'commathweb/index.html',result)

def index(req):
    return render(req,'commathweb/base1.html')

def single(req):
    try:
        r = ''
        d = req.GET.get('num')
        d = float(d)
        print(d, type(d))
        
        nb = bin(int(d))
        nb = nb[2:]
        print(nb)
        lung = d-int(d)   
        while lung>0 and len(nb) + len(r) < 31:
            lung = lung*2
            r += str(int(lung))
            lung -= int(lung) 
        print("r=",r)
        
        e = len(nb)-1
        s = '0' if d >= 0 else '1'
        
        e += 127
        bie = bin(e)
        bie = bie[2:]
        nbbilung = nb+r
        nbbilung = nbbilung[1:]
        b = s+bie+nbbilung
        b = b + '0'*(32-len(b))
        print(b)
        result = {'answer':b, 'd':d}
    except :
        result = {'answer':"ข้อมูลไม่ถูกต้อง กรุณากรอกค่าใหม่"}

    return render(req,'commathweb/single.html',result)

def double(req):
    try:
        # r = ''
        x = req.GET.get('num')
        x = float(x)
        print(type(x))
        w = int(x)
        d = x - w
        bw = bin(w)[2:]
        bd = ''
        while d != 0:
            d  *= 2
            bd += str(int(d))
            d  -= int(d)
        bwbd = bw+bd
        t = len(bw) - 1
        m = bwbd[1:]
        s = 0 if d >= 0 else 1
        e = 1023 + t
        be = bin(e)[2:]
        b = str(s) + be + m
        b += '0'*(64-len(b))
        l = '0'*32
        print(len(b))
        result = {'answer':b, 'x':x, 'l':l}
    except :
        result = {'answer':"ข้อมูลไม่ถูกต้อง กรุณากรอกค่าใหม่"}

    return render(req,'commathweb/double.html',result)

def linear(req):

    # C = readm('A.csv')
    # d = readm('b.csv')
    # u = solve(C, d)
    # print(u)

    
    return render(req,'commathweb/linear.html')

def solve(req):
    name1 = req.GET.get('name1')
    # o = float(name1)
    # o = int(o)
    # print(o, type(o))
    a = []
    for i in range(int(name1)-1):
        a.append('[input id="name" class="input300" type="text" name="equation" placeholder="กรุณาใส่สมการ"]') 

    print('a=',a)
    print('i=',i)

    m = {
        'y' : a,
        'x' : name1
    }

    # A = []
    # b = []
    eqA = req.GET.get('eq')
    eqb = req.GET.get('eqb')
    # A.append(eqA)
    # b.append(eqb)
    print(eqA)
    print("=======================")
    print(eqb)
    # a = ['input id="name" class="input300" type="text" name="name" placeholder="Full name"']
    # for i in range()
    
    # p = {'name1':name1}
    # print(m)
    return render(req,'commathweb/solve.html',m)