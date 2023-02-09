"""
This file corresponds to the first graded lab of 2XC3.
Feel free to modify and/or add functions to this file.
"""
import random
import timeit
import matplotlib.pyplot as plot

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

def selection_sort2(L):
    m = len(L)
    a = ()
    
    for i in range(m):
            a = find_min_index2(L,i,m)
            min_index = a[0]
            max_index = a[1]
            m=m-1
            swap2(L, i, min_index)
            if(m>(len(L)/2)): 
                swap2(L,m, max_index)
            
            
                
def find_min_index2(L, n ,m):
    min_index = n
    max_index = n
    for i in range(n+1, m):
        if L[i] < L[min_index]:
            min_index = i
        if L[i] >= L[max_index]:
            max_index = i
            
            
    return (min_index,max_index)

def swap2(L, i, j):
    L[i], L[j] = L[j], L[i]


def find_min_index(L, n):
    min_index = n
    for i in range(n+1, len(L)):
        if L[i] < L[min_index]:
            min_index = i
    return min_index


def bubble_sort2(L):
    for i in range(len(L)):
        counter=0
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                var = L[j]
                L[j] = L[j+1]
                L[j+1] = var
                counter = 1
        if counter == 0:
            break

def create_random_list(length, max_value):
    L = []
    for _ in range(length):
        L.append(random.randint(0, max_value))
    return L

total1 = 0
total2 = 0
total3 = 0
data = []
runs = 10
len1 = 5
val1= 1000
select1=[]
select2=[]
lenn=[]
percent=0
 
def runperiter(List1,func1,runs) :
    total1=0
    for _ in range(runs) :
        L1=List1.copy()
        start = timeit.default_timer()
        func1(L1)
        end = timeit.default_timer()
        total1+=(end-start)

    return total1/runs

# for i in range(200):

#     if(len1<1000):
#         len1+=10
#     if(((i/runs)*100)>percent and percent<=200):
#         percent+=1
#         print(percent,"%" + " is complete")
    
#     A1=create_random_list(len1,val1)

#     select1.append(runperiter(A1, selection_sort, runs))
#     select2.append(runperiter(A1, selection_sort2, runs))
#     lenn.append(len1)


# ax = plot.gca()
# ax.set_xlim([0,1000])
# ax.set_ylim([0,0.050])
# plot.plot(lenn,select1, label="selection_sort1") 
# plot.plot(lenn,select2 , label = "Selection_sort2") 
# plot.legend(loc="upper left")
# plot.xlabel("Length of the list : ")
# plot.ylabel("Time taken : ")
# plot.title("Experiment 2")
# plot.show()


def SelectExp2(max_runs,max_iter,max_length,max_value) :
    len1 = 5
    select1=[]
    select2=[]
    lenn=[]
    percent=0
    for i in range(max_iter):

        if(len1<max_length):
            len1+=10
        if(((i/max_iter)*100)>percent and percent<=100):
            percent+=1
            print(percent,"%" + " is complete")
    
        A1=create_random_list(len1,max_value)

        select1.append(runperiter(A1, selection_sort, runs))
        select2.append(runperiter(A1, selection_sort2, runs))
        lenn.append(len1)

    ax = plot.gca()
    ax.set_xlim([0,max_length])
    plot.plot(lenn,select1, label="selection_sort1") 
    plot.plot(lenn,select2 , label = "Selection_sort2") 
    plot.legend(loc="upper left")
    plot.xlabel("Length of the list : ")
    plot.ylabel("Time taken : ")
    plot.title("Experiment 2")
    plot.show()
def bubbleExp2(max_runs,max_iter,max_length,max_value) :
    len1 = 5
    select1=[]
    select2=[]
    lenn=[]
    percent=0
    for i in range(max_iter):

        if(len1<max_length):
            len1+=10
        if(((i/max_iter)*100)>percent and percent<=100):
            percent+=1
            print(percent,"%" + " is complete")
    
        A1=create_random_list(len1,max_value)

        select1.append(runperiter(A1, bubble_sort, runs))
        select2.append(runperiter(A1, bubble_sort2, runs))
        lenn.append(len1)

    ax = plot.gca()
    ax.set_xlim([0,max_length])
    plot.plot(lenn,select1, label="bubble_sort1") 
    plot.plot(lenn,select2 , label = "bubble_sort2") 
    plot.legend(loc="upper left")
    plot.xlabel("Length of the list : ")
    plot.ylabel("Time taken : ")
    plot.title("Experiment 2")
    plot.show()
bubbleExp3(10,200,500,40)