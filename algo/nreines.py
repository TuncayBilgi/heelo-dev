import numpy as np
import sys
import time
import random

sys.setrecursionlimit(1200)

def moyenne(function,*args):
    meantime = 0
    for i in range(10):
        start= time.time()
        function(*args)
        end=time.time()
        meantime += (end-start)*1000
    meantime = meantime/10
    return f"La fonction {function.__name__} prend en moyenne {meantime} ms pour n={args[-1]}"
    
        

def cut(args,n):
    positions = [[],[]]
    for i in range(len(args)) :
        if (args[i] in positions[0]) or abs(i+1-args[i]) in positions[1] or args[i]>= n :
            return True
        else :
            positions[0].append(args[i])
            positions[1].append(abs(i+1-args[i]))
    return False

def backtrack(args,n):
    k = len(args)
    if k == 0 : 
        return None
    if cut(args,n) : 
        if args[-1] < n : 
            args[-1] += 1
            return backtrack(args,n)
        else : 
            args.pop()
            args[-1] += 1
            return backtrack(args,n)
    else : 
        if k==n : 
            return args
        else : 
            args.append(0)
            return backtrack(args,n)
        

def nreines_aléatoire(n) :
    res = [0 for i in range(n)]
    while cut(res,n) :
        res = []
        for i in range(n) :
            res.append(random.randint(0,n))
    return res


for i in [3,4,5,6,7] :
    print(moyenne(nreines_aléatoire,i))
    print(moyenne(backtrack,[0],i))
    print('')


