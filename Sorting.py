#Bubble Sort
#Time - O(n^2)
#Space - O(1)

# A=[-5,2,-3,2,3,-2,-3,7,4,3]

# def bubble(arr):
#     n=len(arr)
#     flag=True

#     while flag:
#         flag = False
#         for i in range(1,n):
#             if arr[i]<arr[i-1]:
#                 flag=True
#                 arr[i],arr[i-1]=arr[i-1],arr[i]
# bubble(A)
# print(A)

#Insertion Sort
#Time - O(n^2)
#Space - O(1)

# B=[-5,2,-3,2,3,-2,-3,7,4,3]

# def insertion_sort(arr):
#     n=len(arr)
#     for i in range(1,n):
#         for j in range(i,0,-1):
#             if arr[j]>arr[j-1]:
#                 arr[j],arr[j-1]=arr[j-1],arr[j]

# insertion_sort(B)
# print(B)


#Selection Sort
#Time - O(n^2)
#Space - O(1)

# C=[-5,2,-3,2,3,-2,-3,7,4,3]

# def selection_sort(arr):
#     n=len(arr)
#     for i in range(n):
#         min_index=i
#         for j in range(i+1,n):
#             if arr[j]<arr[min_index]:
#                 min_index=j
#         arr[i],arr[min_index]=arr[min_index],arr[i]

# selection_sort(C)
# print(C)

#Merge Sort
#Time - O()
#Space - O()

D=[-5,2,-3,2,3,-2,-3,7,4,3]

def merge_sort(arr):
    n=len(arr)

    if n==1:
        return arr
    m=len(arr)//2

    L=arr[:m]
    R=arr[m:]

    L=merge_sort(L)
    R=merge_sort(R)
    l,r=0,0
    L_len = len(L)
    #print(L_len)
    R_len = len(R)
    #print(R_len)
    
    sorted_arr= [0] * n
    i=0

    while l < L_len and r < R_len:
        if L[l] < R[r]:
            sorted_arr[i]=L[l]
            l+=1
        else:
            sorted_arr[i]=R[r]
            r+=1

        i+=1
    while l < L_len:
        sorted_arr[i]=L[l]
        l+=1
        i+=1
    
    while r < R_len:
        sorted_arr[i]=R[r]
        r+=1
        i+=1

merge_sort(D)
print(D)


#Quick Sort
#Time - O(n log n)
#Space - O(n)

# E=[-5,2,-3,2,3,-2,-3,7,4,3]

# def quicksort(arr):
#     if len(arr)<=1:
#         return arr
#     p=arr[-1]

#     L = [x for x in arr[:-1] if x <= p]
#     R = [x for x in arr[:-1] if x > p]

#     L= quicksort(L)
#     print(L,"L")
#     R=quicksort(R)
#     print(R,"R")
#     return L +[p] + R

# s=quicksort(E)
# print(s)
