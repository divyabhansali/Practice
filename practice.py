# numbers=[0,4,3,2,1]
# #numbers=[0,4,2,1]
# flag=True
# j=0
# k=len(numbers)-1
# g=k+1
# arr=[0]*g
# for i in range(0,len(arr)):
#     if j<=k:
#         if flag:
#             arr[i]=numbers[j]
#             j+=1
#             flag=False
#         else:
#             arr[i]=numbers[k]
#             k-=1
#             flag=True       

# print(arr)


# commands=["ls","cp","mv","mv","mv","!1","!3","!6"]

# d={}
# def rotate(k,commands):
#     for i in range(k+1):
#         l=commands[i]
#         print(l)
#         if l.startswith("!"):
#             g=l[-1]
#             rotate(int(g),commands)
#         else:
#             return l

# for i in commands:
#     k=i[-1]
#     if i.startswith("!"):
#         print(k,"k")
#         s=rotate(int(k),commands)
#         print(s)
#         if s in d.keys():
#             d[s]+=1
#         else:
#             d[s]=1        
#     else:
#         if i in d:
#             d[i]+=1
#         else:
#             d[i]=1
#         print(d)

# print(d)  
# g = list(d.values())
# g.sort()
# print(g)


#matrix

def spiral(matrix):
    rows,cols=len(matrix),len(matrix[0])
    result=[]
    left,right,top,bottom=0,cols-1,0,rows-1

    while left<=right and top<=bottom:
        for i in range(left,right+1):
            result.append(matrix[top][i])
        top+=1

        for j in range(top,bottom+1):
            result.append(matrix[j][right])
        right-=1

        if top<=bottom:
            for k in range(right,left-1,-1):
                result.append(matrix[bottom][k])
            bottom-=1

        if left<=right:
            for l in range(bottom,top-1,-1):
                result.append(matrix[l][left])
            left+=1

    print(result)
    sum=0
    for i in range(0,len(result),3):
        sum=sum+result[i]
    return sum

m=[
    [1,2,3,5,6,7],
    [4,5,6,10,9,7],
    [7,8,9,1,2,3]
]

# 1+5+7+1+7+6
k=spiral(m)
print(k)

import numpy as np

# Example 2D matrix (image)
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Rotate 90° clockwise using transpose + flip
rotated = np.transpose(matrix)[::-1]
print(rotated)

