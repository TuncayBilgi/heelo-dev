import time
import random
import sys


sys.setrecursionlimit(4000)


def moyenne(function, args):
    meantime = 0
    for i in range(10):
        args_cpy = args[:]
        start = time.time()
        function(args_cpy)
        end = time.time()
        meantime += (end - start) * 1000
    meantime = meantime / 10
    return f"La fonction {function.__name__} prend en moyenne {meantime} ms pour n={len(args)}"


def divideAndConquer(lst):
    n = len(lst)
    return dAc(lst, 0, n - 1, n // 2)


def dAc(lst, debut, fin, indice_median):
    if debut == fin:
        return lst[debut]

    indice_pivot = partitionner(lst, debut, fin)

    if indice_median == indice_pivot:
        return lst[indice_median]
    elif indice_median < indice_pivot:
        return dAc(lst, debut, indice_pivot - 1, indice_median)
    else:
        return dAc(lst, indice_pivot + 1, fin, indice_median)


def partitionner(lst, debut, fin):
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
    return lst[len(lst) // 2]


# Exemple d'utilisation :


lst = [random.randint(1, 100) for x in range(10_000)]


print(moyenne(divideAndConquer, lst))
print(moyenne(quick_sort_median, lst))
print(moyenne(sort_median, lst))


# Python3 program of Quick Select

# Standard partition process of QuickSort().
# It considers the last element as pivot
# and moves all smaller element to left of
# it and greater elements to right
def partition(arr, l, r):

    x = arr[r]
    i = l
    for j in range(l, r):

        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[r] = arr[r], arr[i]
    return i


# finds the kth position (of the sorted array)
# in a given unsorted array i.e this function
# can be used to find both kth largest and
# kth smallest element in the array.
# ASSUMPTION: all elements in arr[] are distinct
def kthSmallest(arr, l, r, k):

    # if k is smaller than number of
    # elements in array
    if k > 0 and k <= r - l + 1:

        # Partition the array around last
        # element and get position of pivot
        # element in sorted array
        index = partition(arr, l, r)

        # if position is same as k
        if index - l == k - 1:
            return arr[index]

        # If position is more, recur
        # for left subarray
        if index - l > k - 1:
            return kthSmallest(arr, l, index - 1, k)

        # Else recur for right subarray
        return kthSmallest(arr, index + 1, r, k - index + l - 1)
    print("Index out of bound")


# Driver Code
meantime = 0
for i in range(10):

    lst = [random.randint(1, 100) for x in range(10_000)]
    n = len(lst)
    k = len(lst) // 2
    start = time.time()
    kthSmallest(lst, 0, n - 1, k)
    end = time.time()
    elapsed = end - start
    meantime += elapsed * 1000
meantime = meantime/10
print(f"La fonction Quickselect prend en moyenne {meantime} ms pour n={len(lst)}")
