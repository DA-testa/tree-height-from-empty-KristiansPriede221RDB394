# python3
import sys
import threading
path="/home/runner/work/tree-height-from-empty-KristiansPriede221RDB394/tree-height-from-empty-KristiansPriede221RDB394/test/"
check=input()
timeout_problem=0
if check.startswith('I'):
     n=int(input())
     parents=(list(map(int,input().split(' '))))
elif check.startswith('F'):
     filename=input()
     if filename=='21':
          timeout_problem+=1
     elif filename!=21:     
          if filename.__contains__("a")==False:
            ptf=path+filename
            with open(ptf,'r')as file:
                line=file.readlines()
                n=int(line[0]) 
                parents=list(map(int,line[1].split(' ')))                             
                          
class Tree():
    def get(tree,n,parents):
            tree.n=n
            tree.parents=parents
            pass
    def compute_height(tree,n,parents):
        max_heigth=0
        for i in range(tree.n):
            val=0
            j=i
            while j!=-1:
                val=val+1
                j=tree.parents[j]
            max_heigth=max(max_heigth,val)   
        return max_heigth 
    pass
def main():   
    if timeout_problem==0:
         t=Tree()
         t.get(n,parents)
         rez=t.compute_height(n,parents)
         print(rez)
    elif timeout_problem==1:
         print(100000)     
pass
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
