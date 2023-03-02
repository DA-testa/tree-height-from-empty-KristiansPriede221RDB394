# python3
import sys
import threading
check=input()
if check.startswith('I')or check.startswith('F'):
     n=int(input())
     parents=list(map(int,input().split(' ')))
class Tree():
    def get(self,n,parents):
            self.n=n
            self.parents=parents
            pass

    def compute_height(self,n,parents):
        max_heigth=0
        for i in range(self.n):
            val=0
            j=i
            while j!=-1:
                val=val+1
                j=self.parents[j]
            max_heigth=max(max_heigth,val)   

        return max_heigth 
    pass
def main():
    t=Tree()
    t.get(n,parents)
    rez=t.compute_height(n,parents)
    print(rez)
pass
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
