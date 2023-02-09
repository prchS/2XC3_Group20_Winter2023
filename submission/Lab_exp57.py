import timeit
import random
import matplotlib.pyplot as plot
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
    return L

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
def swap(L,i,j):
    L[i], L[j] = L[j], L[i]

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
    
#======================================
#Experiment 5
# Creates a near sorted list by creating a random list, sorting it, then doing a random number of swaps
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
def runperiter(List1,func1,runs) :
    total1=0
    for _ in range(runs) :
        L1=List1.copy()
        start = timeit.default_timer()
        func1(L1)
        end = timeit.default_timer()
        total1+=(end-start)

    return total1/runs



#===============================================================================================================================


 
def bottom_up_mergesort(arr):
    n = len(arr)
    size = 1
    while size < n:
        for start in range(0, n, 2*size):
            midpoint = start + size - 1
            end = min(start + 2*size - 1, n-1)
            left_half = arr[start:midpoint+1]
            right_half = arr[midpoint+1:end+1]
            arr[start:end+1] = merge(left_half, right_half)
        size *= 2
    return arr



#==============================================================================================================================

# runs =100
# len1 = 250
# val1=1000
# total1=0
# total2=0
# percent=0
# select1=[]
# heap=[]
# select2=[]
# swp2=[]
# swp=1
# lenn=[]
# quicksort1=[]
# merge1=[]

# for i in range(0,200):
#     List1= create_near_sorted_list(len1, val1, swp)
#     if(swp<200):
#         swp+=1
#     if(((i/runs)*100)>percent and percent<=200):
#         percent+=1
#         print(percent,"%" + " is complete")


#     quicksort1.append(runperiter(List1, quicksort, runs))
#     merge1.append(runperiter(List1, mergesort, runs))
#     heap.append(runperiter(List1, heapsort, runs))
#     swp2.append(swp)

# for i in range(200):

#     if(len1<1000):
#         len1+=5
#     if(((i/runs)*100)>percent and percent<=200):
#         percent+=1
#         print(percent,"%" + " is complete")
    
#     A1=create_random_list(len1,val1)

#     select1.append(runperiter(A1, mergesort, runs))
#     select2.append(runperiter(A1, bottom_up_mergesort, runs))
#     lenn.append(len1)

    

# ax = plot.gca()
# ax.set_xlim([-50,200])
# # ax.set_ylim([0,0.0025])
# plot.plot(swp2,quicksort1, label="quicksort") 
# plot.plot(swp2,heap , label = "heapsort") 
# plot.plot(swp2,merge1 , label = "mergesort") 
# plot.legend(loc="upper left")
# plot.xlabel("Amount of swaps: ")
# plot.ylabel("Time taken : ")
# plot.title("Experiment 5")
# plot.show()

def exp5(max_iter,runs,max_length,max_value,max_swaps):
    percent=0
    select1=[]
    heap=[]
    select2=[]
    swp2=[]
    swp=1
    lenn=[]
    quicksort1=[]
    merge1=[]

    for i in range(0,max_iter):
        List1= create_near_sorted_list(max_length, max_value, swp)
        if(swp<max_swaps):
            swp+=1
        if(((i/max_iter)*100)>percent and percent<=100):
            percent+=1
            print(percent,"%" + " is complete")


        quicksort1.append(runperiter(List1, quicksort, runs))
        merge1.append(runperiter(List1, mergesort, runs))
        heap.append(runperiter(List1, heapsort, runs))
        swp2.append(swp)
    ax = plot.gca()
    ax.set_xlim([-50,max_swaps])
    # ax.set_ylim([0,0.0025])
    plot.plot(swp2,quicksort1, label="quicksort") 
    plot.plot(swp2,heap , label = "heapsort") 
    plot.plot(swp2,merge1 , label = "mergesort") 
    plot.legend(loc="upper left")
    plot.xlabel("Amount of swaps: ")
    plot.ylabel("Time taken : ")
    plot.title("Experiment 5")
    plot.show()

def exp7(max_iter,runs,max_length,max_value):
    percent=0
    select1=[]
    heap=[]
    select2=[]
    length=1
    lenn=[]
    quicksort1=[]
    merge1=[]

    for i in range(0,max_iter):
        List1= create_random_list(length, max_value)
        if(length<max_length):
            length+=1
        if(((i/max_iter)*100)>percent and percent<=100):
            percent+=1
            print(percent,"%" + " is complete")


        quicksort1.append(runperiter(List1, bottom_up_mergesort, runs))
        merge1.append(runperiter(List1, mergesort, runs))
        lenn.append(length)
    ax = plot.gca()
    ax.set_xlim([-10,max_length])
    # ax.set_ylim([0,0.0025])
    plot.plot(lenn,quicksort1, label="bottom_up_mergesort") 
    plot.plot(lenn,merge1 , label = "mergesort") 
    plot.legend(loc="upper left")
    plot.xlabel("length of the list")
    plot.ylabel("Time taken : ")
    plot.title("Experiment 7")
    plot.show()

exp7(1000,50,200,1000)

