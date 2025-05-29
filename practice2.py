# 0
# 1
# 1
# 2
# 3
# 5
# 8


# def fib(n):
#     if n==1:
#         return 1
#     elif n==0:
#         return 0
#     else:
#         return fib(n-1)+fib(n-2)
# r=fib(9)
# print(r)







def fib(n_terms, n1=0, n2=1, count=0):
    if n_terms == count: # 9 != 8
       return n1
    
    # print(n1) #0 1 1  
    next_term = n1+n2 #1 2 3
    n1      = n2 #1 1 2
    n2 = next_term #1 2 3
    count+=1 #1 2 3
    return fib(n_terms, n1, n2, count)




n_terms = 9
print(fib(n_terms))





# def fac(n):
#     if n<=1:
#         return 1
#     return n*fac(n-1)

# def fac1(n):
#     return n*fac1(n-1) if n>1 else 1

# print(fac1(7))








# 0!=1
# 1!=1
#2!=2
#3!=6

# 5!=120
# 6!=720
# 7!=5040
# 8!=40320

class Mridul:
    def fac(self, n):
        if n<=1:
            return 1
        return n*self.fac(n-1)
    
    def solution(self, n, add):
        return add + self.fac(n)


class Mridul:
    def fac(self, n: int) -> int:
        """
        Calculate the factorial of a given number n recursively.
        
        Parameters:
        n (int): The number to calculate the factorial of.
        
        Returns:
        int: Factorial of n.
        """
        if n <= 1:
            return 1
        return n * self.fac(n - 1)
    
    def solution(self, n: int, add: int) -> int:
        """
        Compute the sum of a given integer 'add' and the factorial of 'n'.
        
        Parameters:
        n (int): The number to compute the factorial of.
        add (int): The number to add to the factorial.
        
        Returns:
        int: The result of add + fac(n).
        """
        return add + self.fac(n)

n = 7
add = 60

obj1 = Mridul()
answer = obj1.solution(n, add)
print(answer)