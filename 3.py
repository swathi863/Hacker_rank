#------------numpy---arrays--------
#---------input------
'''
1 2 3 4 -8 -10
'''
#-------output--------
'''
[-10 -8 4 3 2 1]
'''
'''
import numpy
def array(arr):
    arr=list(map(float,arr))
    arr.reverse()
    return numpy.array(arr,float)
arr=input().strip().split('')
res=array(arr)
print(res)
'''
#------shape-and-reshape----------------------
#-----------input----------
#1 2 3 4 5 6 7 8 9
'''
import numpy
array=numpy.array(input().split(),int)
array.shape=(3,3)
print(array)
'''
'''
my_array = numpy.array([1,2,3,4,5,6])
print numpy.reshape(my_array,(3,2))
'''
#-------------transpose--flatten()------
#-----input-----
'''
2 2
1 2
3 4
'''
#------output----
'''
[[1 3]
 [2 4]]
[1 2 3 4]
'''
'''
import numpy
n,m=map(int,input().split())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
arr=numpy.array(a)
print(numpy.transpose(arr))
print(arr.flatten())
'''
#----------------concatenate-------------------
#----------input-----------
'''
4 3 2
1 2
1 2 
1 2
1 2
3 4
3 4
3 4 
'''
#-----output-------------
'''
[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]] 
'''
'''
import numpy
n=list(map(int,input().split()))
N=n[0]
M=n[1]
P=n[2]
a=[]
for i in range(N+M):
    a.append(list(map(int,input().split())))
arr=numpy.array(a)
print(arr)
'''
'''
    n, m, p = [*map(int, input().rstrip().split())]
    arr1 = []
    arr2 = []
    for i in range(n):
        arr1.append([*map(int, input().rstrip().split())])
    for i in range(m):
        arr2.append([*map(int, input().rstrip().split())])
    print(np.concatenate((arr1, arr2), axis=0))
'''
#-------collections-----------------
#defaultdict---------------
'''
from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print(i)
'''
#------------------input-------------------
'''
STDIN   Function
-----   --------
5 2     group A size n = 5, group B size m = 2
a       group A contains 'a', 'a', 'b', 'a', 'b'
a
b
a
b
a       group B contains 'a', 'b'
b
'''
'''
from collections import defaultdict
n,m=map(int,input().split())
d=defaultdict(list)
for i in range(1,n+1):
    d[input()].append(str(i))
for i in range(m):
    word=input()
    if word in d:
        print(" ".join(d[word]))
    else:
        print("-1")
'''
#----------------namedtuple-------------
'''
from collections import namedtuple
Point = namedtuple('Point','x,y')
pt1 = Point(1,2)
pt2 = Point(3,4)
dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
print(dot_product)
'''
#-------------------input-----------------
'''
5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6   
'''
'''
from collections import namedtuple
n=int(input())
list=input().split()
total=0
for i in range(n):
    stud=namedtuple('students',list)
    MARKS,CLASS,NAME,ID=input().split()
    students=stud(MARKS,CLASS,NAME,ID)
    total+=int(students.MARKS)
print(total/n)
'''









            
