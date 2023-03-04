# python3
import sys
import threading
import numpy as np
path="/home/runner/work/tree-height-from-empty-KristiansPriede221RDB394/tree-height-from-empty-KristiansPriede221RDB394/test/"
##path="C:\\Users\\Kristians\\Desktop\\pitons_vs\\tree-height-from-empty-KristiansPriede221RDB394\\test\\"
check=input()
if check.startswith('I'):
     n=int(input())
     parents=(list(map(int,input().split(' '))))
elif check.startswith('F'):
     filename=input()
     if filename.__contains__("a")==False:
               ptf=path+filename
               count=0
               with open(ptf,'r')as file:
                      fl=file.readlines()
                      n=int(fl[0])
                      parents_ar=fl[1].split(' ')
                      parents=list(map(int,parents_ar))
                                
class Tree():
    def get(k,n,parents):
            k.n=n
            k.parents=parents
            pass
    def compute_height(k,n,parents):
        max_heigth=0
        for i in range(k.n):
            val=0
            j=i
            while j!=-1:
                val=val+1
                j=k.parents[j]
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
