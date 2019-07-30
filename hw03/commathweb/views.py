from django.shortcuts import render
from django.http import HttpResponse

def index(req):
    return render(req,'commathweb/baseTemplate/base.html')

def decto32fp(req):
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

def decto64fp(req):
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
        print(len(b))
        result = {'answer':b, 'x':x}
    except :
        result = {'answer':"ข้อมูลไม่ถูกต้อง กรุณากรอกค่าใหม่"}

    return render(req,'commathweb/double.html',result)


def solve(A, b):
    import numpy as np
    a,b = np.array(A), np.array(b)
    n= len(A[0])
    x = np.array([0]*n)

    for k in range(0, n-1):
#1
        for j in range(k+1, n):
            if a[j,k] != 0.0:
                lam = a[j][k]/a[k][k]
                a[j,k:n] = a[j, k:n] - lam*a[k,k:n]
                b[j] = b[j] - lam*b[k]
#2
    for k in range(n-1,-1,-1):
        x[k] = (b[k] - np.dot(a[k,k+1:n], x[k+1:n]))/a[k,k]
    return x.flatten()

def linear(req):
    if req.method == 'POST':
        matrix_y=[]
        matrix_x=[]
        data= req.POST.get('name1')
		#x = data.split(',')
        data2 = data.split('\n')
        for i in data2:
            y=[float( i.split('=')[-1] )]
            matrix_y.append(y)
            x = (i.split('=')[0]).split(',')
            matrix_x.append(list(map(float, x)))
        
        results=solve(matrix_x,matrix_y)
        mylist = zip(matrix_x,matrix_y)
    try:
        return render(req,'commathweb/solve.html',{'mylist':mylist,'results':results})
    except:
        return render(req,'commathweb/solve.html')
		