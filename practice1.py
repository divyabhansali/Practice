# def leng(a):
#     k=len(a)
#     return k

# print(leng(list(map(int,input().split()))))


# def find_sum(n):
#     if n==1:
#         print(n)
#         return 1
#     print(n)
#     return n+find_sum(n-1)

# print(find_sum(4))

# # 4+ find_sum(3) 
# 4+3+find_sum(2)
# # 4+3+2+1


# number=int(input())

# def fac(n,ans=1):
#     print("fun")
#     if n==0:
#         print("why")
#         return 1
#     else:
#         while n>0:
#             print("hi")
#             ans=ans*n
#             n-=1
#     return ans
# print(fac(number))


class Student:
    def __init__(self,name,marks):
        self.name= name
        self.marks=marks

    def get_avg(self):
        sum =0
        for val in self.marks:
            sum+=val
        print("hi",self.name, "you received:",sum/3,"marks")

s1=Student("divya",[98,99,97])
s1.get_avg()
