class Solution():
    def __init__(self):
        self.cache = {}
    
    def fib(self, n):
        if n <= 2:
            return n
        
        if n not in self.cache:
            self.cache[n] = self.fib(n-1) + self.fib(n-2)

        return self.cache[n]

a = Solution()
print(a.fib(40))


def fib(self,N):
    cache={}
    def recur_fib(self,N):
        if N in cache:
            return cache[N]
        
        if N<2:
            result= N
        else:
            return recur_fib(N-1)+recur_fib(N-2)
        
        cache[N]=result
        return result
    recur_fib(5)