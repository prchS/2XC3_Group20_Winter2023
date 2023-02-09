import random
import timeit
import matplotlib.pyplot as plot
from math import log

# Create a random list length "length" containing whole numbers between 0 and max_value inclusive
def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]

def create_near_sorted_list(length, max_value, swaps):
    L = create_random_list(length, max_value)
    L.sort()
    for _ in range(swaps):
        r1 = random.randint(0, length - 1)
        r2 = random.randint(0, length - 1)
        swap(L, r1, r2)
    return L

# I have created this function to make the sorting algorithm code read easier
def swap(L, i, j):
    L[i], L[j] = L[j], L[i]


# This is the traditional implementation of Insertion Sort.
def insertion_sort(L):
    for i in range(1, len(L)):
        insert(L, i)


def insert(L, i):
    while i > 0:
        if L[i] < L[i-1]:
            swap(L, i-1, i)
            i -= 1
        else:
            return


def swap(L, i, j):
    L[i], L[j] = L[j], L[i]


# ************ Quick Sort ************
def quicksort(L):
    copy = quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def quicksort_copy(L):
    if len(L) < 2:
        return L
    pivot = L[0]
    left, right = [], []
    for num in L[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    return quicksort_copy(left) + [pivot] + quicksort_copy(right)


# ************ Merge Sort *************

def mergesort(L):
    if len(L) <= 1:
        return
    mid = len(L) // 2
    left, right = L[:mid], L[mid:]

    mergesort(left)
    mergesort(right)
    temp = merge(left, right)

    for i in range(len(temp)):
        L[i] = temp[i]


def merge(left, right):
    L = []
    i = j = 0

    while i < len(left) or j < len(right):
        if i >= len(left):
            L.append(right[j])
            j += 1
        elif j >= len(right):
            L.append(left[i])
            i += 1
        else:
            if left[i] <= right[j]:
                L.append(left[i])
                i += 1
            else:
                L.append(right[j])
                j += 1
    return L



def timesorting(List, Alg,runs):
    total = 0
    for i in range(runs):
        L = List.copy()
        start = timeit.default_timer()
        Alg(L)
        end= timeit.default_timer()
        total += (end - start)
    return total/runs

def exp8_random():
    span = 50
    Merge = []
    Quick = []
    Insertion = []
    runs = 2000
    for i in range (0,span,1):
        List1 = create_random_list(i,100)
        List2 = List1.copy()
        List3 = List1.copy()
        Merge.append(timesorting(List1, mergesort, runs))
        Quick.append(timesorting(List2, quicksort, runs))
        Insertion.append(timesorting(List3, insertion_sort, runs))
    print("done!")
    plot.plot(Merge)
    plot.plot(Quick)
    plot.plot(Insertion)
    plot.legend(['Merge', 'Quick', 'Insertion'])
    plot.xlabel("List Length")
    plot.ylabel("Time")
    plot.show()


def exp8_sortness():
    span = 50
    Merge = []
    Quick = []
    Insertion = []
    runs = 1000
    for i in range (1,span,1):
        List1 = create_near_sorted_list(i,50,0)
        List2 = List1.copy()
        List3 = List1.copy()
        Merge.append(timesorting(List1, mergesort, runs))
        Quick.append(timesorting(List2, quicksort, runs))
        Insertion.append(timesorting(List3, insertion_sort, runs))
    print("done!")
    plot.plot(Merge)
    plot.plot(Quick)
    plot.plot(Insertion)
    plot.legend(['Merge', 'Quick', 'Insertion'])
    plot.xlabel("List Length")
    plot.ylabel("Time")
    plot.show()

exp8_random()


