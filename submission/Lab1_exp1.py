"""
This file corresponds to the first graded lab of 2XC3.
Feel free to modify and/or add functions to this file.
"""
import random
import timeit
import matplotlib.pyplot as plot
import matplotlib.animation as animation


# Create a random list length "length" containing whole numbers between 0 and max_value inclusive
def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]


# Creates a near sorted list by creating a random list, sorting it, then doing a random number of swaps
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


# ******************* Insertion sort code *******************

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


# This is the optimization/improvement we saw in lecture
def insertion_sort2(L):
    for i in range(1, len(L)):
        insert2(L, i)


def insert2(L, i):
    value = L[i]
    while i > 0:
        if L[i - 1] > value:
            L[i] = L[i - 1]
            i -= 1
        else:
            L[i] = value
            return
    L[0] = value


# ******************* Bubble sort code *******************

# Traditional Bubble sort
def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                swap(L, j, j+1)


# ******************* Selection sort code *******************

# Traditional Selection sort
def selection_sort(L):
    for i in range(len(L)):
        min_index = find_min_index(L, i)
        swap(L, i, min_index)


def find_min_index(L, n):
    min_index = n
    for i in range(n+1, len(L)):
        if L[i] < L[min_index]:
            min_index = i
    return min_index


# ***********************************************************
# *********************** Experiment-1 **********************
# ***********************************************************



def test1(length,step,runs,max_value):
    times1 = []
    times2 = []
    times3 = []
    len = []
    for i in range(0,length+1,step):
        time1 = 0
        time2 = 0
        time3 = 0
        for j in range(runs):
            arr = create_random_list(i,max_value)
            arr2 = arr.copy()
            arr3 = arr.copy()

            start = timeit.default_timer()
            bubble_sort(arr)
            end = timeit.default_timer()
            time1 += end - start

            start = timeit.default_timer()
            insertion_sort(arr2)
            end = timeit.default_timer()
            time2 += end - start

            start = timeit.default_timer()
            selection_sort(arr3)
            end = timeit.default_timer()
            time3 += end - start

        times1.append(time1/runs)
        times2.append(time2/runs)
        times3.append(time3/runs)
        len.append(i)
        if (i*100/length) % 10 == 0:
            print(str(int(i*100/length)) + "%" + " completed")
    return times1,times2,times3,len

def test2(length,step,runs,max_value,swaps):
    times1 = []
    times2 = []
    times3 = []
    len = []
    for i in range(1,length+1,step):
        time1 = 0
        time2 = 0
        time3 = 0
        for j in range(runs):
            arr = create_near_sorted_list(i,max_value,swaps)
            arr2 = arr.copy()
            arr3 = arr.copy()

            start = timeit.default_timer()
            bubble_sort(arr)
            end = timeit.default_timer()
            time1 += end - start

            start = timeit.default_timer()
            insertion_sort(arr2)
            end = timeit.default_timer()
            time2 += end - start

            start = timeit.default_timer()
            selection_sort(arr3)
            end = timeit.default_timer()
            time3 += end - start

        times1.append(time1/runs)
        times2.append(time2/runs)
        times3.append(time3/runs)
        len.append(i)
        if ((i-1)*100/length) % 10 == 0:
            print(str(int(i*100/length)) + "%" + " completed")
    return times1,times2,times3,len

#result = test1(100,1,5_000,100)                   
#result = test1(10_000,500,10,10_000)               
#result = test1(20_000,1000,5,100)                   
#result = test2(1000,1,50,100,10)                  
result = test2(1000,10,100,1000,1)                 

plot.plot(result[3],result[0],color='r', label='bubble_sort')
plot.plot(result[3],result[1],color='g', label='insertion_sort')
plot.plot(result[3],result[2],color='b', label='selection_sort')
plot.xlabel("List_Length")
plot.ylabel("Time")
plot.title("Experiment-1")
plot.legend()
plot.show() 