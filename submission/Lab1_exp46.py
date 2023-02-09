import math
import random
import timeit
import matplotlib.pyplot as plot
import matplotlib.animation as animation

"""
This file corresponds to the first graded lab of 2XC3.
Feel free to modify and/or add functions to this file.

In contains traditional implementations for:
1) Quick sort
2) Merge sort
3) Heap sort

Author: Vincent Maccio
"""

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

# *************************************


# *********** Quick Sort-2 ************
def dual_quicksort(L):
    copy = dual_quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]

def dual_quicksort_copy(L):
    if len(L) < 2:
        return L
    if L[0] > L[1]: pivot1,pivot2 = L[1],L[0] 
    else: pivot1,pivot2 = L[0],L[1]
    left,middle,right = [],[],[]
    for num in L[2:]:
        if num < pivot1 and num < pivot2:
            left.append(num)
        elif num > pivot1 and num > pivot2:
            right.append(num)
        else: middle.append(num)
    return dual_quicksort_copy(left) + [pivot1] + dual_quicksort_copy(middle) + [pivot2] + dual_quicksort_copy(right)


# *************************************


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

# *************************************

# ************* Heap Sort *************

def heapsort(L):
    heap = Heap(L)
    for _ in range(len(L)):
        heap.extract_max()

class Heap:
    length = 0
    data = []

    def __init__(self, L):
        self.data = L
        self.length = len(L)
        self.build_heap()

    def build_heap(self):
        for i in range(self.length // 2 - 1, -1, -1):
            self.heapify(i)

    def heapify(self, i):
        largest_known = i
        if self.left(i) < self.length and self.data[self.left(i)] > self.data[i]:
            largest_known = self.left(i)
        if self.right(i) < self.length and self.data[self.right(i)] > self.data[largest_known]:
            largest_known = self.right(i)
        if largest_known != i:
            self.data[i], self.data[largest_known] = self.data[largest_known], self.data[i]
            self.heapify(largest_known)

    def insert(self, value):
        if len(self.data) == self.length:
            self.data.append(value)
        else:
            self.data[self.length] = value
        self.length += 1
        self.bubble_up(self.length - 1)

    def insert_values(self, L):
        for num in L:
            self.insert(num)

    def bubble_up(self, i):
        while i > 0 and self.data[i] > self.data[self.parent(i)]:
            self.data[i], self.data[self.parent(i)] = self.data[self.parent(i)], self.data[i]
            i = self.parent(i)

    def extract_max(self):
        self.data[0], self.data[self.length - 1] = self.data[self.length - 1], self.data[0]
        max_value = self.data[self.length - 1]
        self.length -= 1
        self.heapify(0)
        return max_value

    def left(self, i):
        return 2 * (i + 1) - 1

    def right(self, i):
        return 2 * (i + 1)

    def parent(self, i):
        return (i + 1) // 2 - 1

    def __str__(self):
        height = math.ceil(math.log(self.length + 1, 2))
        whitespace = 2 ** height
        s = ""
        for i in range(height):
            for j in range(2 ** i - 1, min(2 ** (i + 1) - 1, self.length)):
                s += " " * whitespace
                s += str(self.data[j]) + " "
            s += "\n"
            whitespace = whitespace // 2
        return s

# *************************************

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




# ***********************************************************
# *********************** Experiment-4 **********************
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
            quicksort(arr)
            end = timeit.default_timer()
            time1 += end - start

            start = timeit.default_timer()
            mergesort(arr2)
            end = timeit.default_timer()
            time2 += end - start

            start = timeit.default_timer()
            heapsort(arr3)
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
            quicksort(arr)
            end = timeit.default_timer()
            time1 += end - start

            start = timeit.default_timer()
            mergesort(arr2)
            end = timeit.default_timer()
            time2 += end - start

            start = timeit.default_timer()
            heapsort(arr3)
            end = timeit.default_timer()
            time3 += end - start

        times1.append(time1/runs)
        times2.append(time2/runs)
        times3.append(time3/runs)
        len.append(i)
        if ((i-1)*100/length) % 10 == 0:
            print(str(int(i*100/length)) + "%" + " completed")
    return times1,times2,times3,len


#result = test1(100,1,10_000,100)                   
#result = test1(10_000,20,100,10_000)               
#result = test1(50_000,100,1,100)                   
#result = test2(1000,1,100,100,10)                  
result = test2(1000,10,100,1000,1)                 

plot.plot(result[3],result[0],color='r', label='quicksort')
plot.plot(result[3],result[1],color='g', label='mergesort')
plot.plot(result[3],result[2],color='b', label='heapsort')
plot.xlabel("List_Length")
plot.ylabel("Time")
plot.title("Experiment-4")
plot.legend()
plot.show()



# ***********************************************************
# *********************** Experiment-6 **********************
# ***********************************************************


def test3(length,step,runs,max_value):
    times1 = []
    times2 = []
    len = []
    for i in range(0,length+1,step):
        time1 = 0
        time2 = 0
        for j in range(runs):
            arr = create_random_list(i,max_value)
            arr2 = arr.copy()

            start = timeit.default_timer()
            quicksort(arr)
            end = timeit.default_timer()
            time1 += end - start

            start = timeit.default_timer()
            dual_quicksort(arr2)
            end = timeit.default_timer()
            time2 += end - start

        times1.append(time1/runs)
        times2.append(time2/runs)
        len.append(i)
        if (i*100/length) % 10 == 0:
            print(str(int(i*100/length)) + "%" + " completed")
    return times1,times2,len

def test4(length,step,runs,max_value,swaps):
    times1 = []
    times2 = []
    len = []
    for i in range(1,length+1,step):
        time1 = 0
        time2 = 0
        for j in range(runs):
            arr = create_near_sorted_list(i,max_value,swaps)
            arr2 = arr.copy()

            start = timeit.default_timer()
            quicksort(arr)
            end = timeit.default_timer()
            time1 += end - start

            start = timeit.default_timer()
            dual_quicksort(arr2)
            end = timeit.default_timer()
            time2 += end - start

        times1.append(time1/runs)
        times2.append(time2/runs)
        len.append(i)
        if ((i-1)*100/length) % 10 == 0:
            print(str(int(i*100/length)) + "%" + " completed")
    return times1,times2,len


#result6 = test3(100_000,1000,10,100_000)   
#result6 = test3(50_000,100,1,100)          
#result6 = test4(1000,1,100,100,10)         
result6 = test4(1000,10,100,1000,1)        

plot.plot(result6[2],result6[0],color='r', label='quicksort')
plot.plot(result6[2],result6[1],color='orange', label='dual_quicksort')
plot.xlabel("List_Length")
plot.ylabel("Time")
plot.title("Experiment-6")
plot.legend()
plot.show()