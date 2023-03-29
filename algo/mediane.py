import time
import random

def moyenne(function,args):
    meantime = 0
    for i in range(10):
        args_cpy = args[:]
        start= time.time()
        function(args_cpy)
        end=time.time()
        meantime += (end-start)*1000
    meantime = meantime/10
    return f"La fonction {function.__name__} prend en moyenne {meantime} ms pour n={len(args)}"
    

def divideAndConquer(lst):
    n = len(lst)
    return dAc(lst, 0, n-1, n // 2)

def dAc(lst, debut, fin, indice_median):
    if debut == fin:
        return lst[debut]
    
    indice_pivot = partition(lst, debut, fin)
    
    if indice_median == indice_pivot:
        return lst[indice_median]
    elif indice_median < indice_pivot:
        return dAc(lst, debut, indice_pivot-1, indice_median)
    else:
        return dAc(lst, indice_pivot+1, fin, indice_median)

def partition(lst, debut, fin):
    pivot = lst[fin]
    indice_pivot = debut
    
    for i in range(debut, fin):
        if lst[i] <= pivot:
            lst[i], lst[indice_pivot] = lst[indice_pivot], lst[i]
            indice_pivot += 1
    
    lst[fin], lst[indice_pivot] = lst[indice_pivot], lst[fin]
    return indice_pivot


def quick_sort_median(lst):
    n = len(lst)
    if n == 1:
        return lst[0]

    pivot = lst[-1]
    smaller, equal, larger = [], [], []

    for elem in lst:
        if elem < pivot:
            smaller.append(elem)
        elif elem == pivot:
            equal.append(elem)
        else:
            larger.append(elem)

    nb_smaller = len(smaller)
    nb_equal = len(equal)
    nb_larger = len(larger)
    
    if nb_smaller <= n // 2 < nb_smaller + nb_equal:
        return pivot
    elif nb_smaller > n // 2:
        return quick_sort_median(smaller)
    else:
        return quick_sort_median(larger)
    

def sort_median(lst):
    lst.sort()
    return lst[len(lst)//2]

# Exemple d'utilisation :





# Exemple d'utilisation :
# lst = [3, 5, 1, 2, 6, 7, 8]
# print(trouver_mediane_div_conq(lst))
# lst = [3, 5, 1, 2, 6, 7, 8]
# print(quick_sort_median_elem(lst))

lst = [random.randint(1,100) for x in range(50000)]

print(moyenne(divideAndConquer,lst))
print(moyenne(quick_sort_median,lst))
print(moyenne(sort_median,lst))