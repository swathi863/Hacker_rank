#--------------calender-------------------
import calendar
'''x=2024
y=3
s=calendar.month(x,y)
print(s)'''
'''print(calendar.calendar(2018))'''
#print(calendar.Day(8-3-2018))
import datetime
'''n='8 5 2015'
day,month,year=(int(x) for x in n.split())
ans=datetime.date(year,day,month)
x=ans.strftime("%A")
print(x)'''
'''n='8 5 2015'
day,month,year=(int(x) for x in n.split())
ans=datetime.date(year,month,day)
x=ans.strftime("%A")
print(x)'''
#-------ASCII(American standard code international interchange)----------------------------
'''for i in range(65,91):
    print(chr(i),end=" ")
print('\n')
for j in range(97,123):
    print(chr(j),end=" ")'''
#---------------alphabetical patterns------------------------------------
'''A=65
Z=90'''
'''for i in range(65,70):
    for j in range(i,70):
        print(chr(i),end=" ")
    print()'''
'''for i in range(65,70):
    for j in range(i,70):
        print(chr(j),end=" ")
    print()'''
'''for i in range(65,70):
    for j in range(65,i+1):
        print(chr(i),end=" ")
    print()'''
'''for i in range(65,70):
    for j in range(65,i+1):
        print(chr(j),end=" ")
    print()'''
'''for i in range(65,70):
    for j in range(i,64,-1):
        print(chr(j),end="")
    print()'''
'''name=str(input("enter the name"))
#print(len(name))
for i in range(0,len(name)):
    for j in range(0,i+1):
        print(name[j],end="")
    print()'''
#----------numeric pattern-------------------
#n=7
'''for i in range(1,n+1):
    for j in range(1,i):
        print(j,end=" ")
    print()'''
'''for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()'''
'''for i in range(1,n+1):
    for j in range(1,i):
        print(i,end=" ")
    print()'''
'''for i in range(1,n+1):
    for j in range(i,n+1):
        print(i,end=" ")
    print()'''
'''for i in range(1,n+1):
    for j in range(1,i):
        print(i,end=" ")
    print()'''
#---------------------------------name in pattern------------
'''name=str(input("enter the  name"))
for i in range(0,len(name)):
    for j in range(0,i+1):
        print(name[j],end="")
    print()'''
#---------------------full diamond pattern-----------------
'''h=int(input("enter the height"))
for i in range(1,h,2):
    print(("*"*i).center(h))
if h%2==0:
    for i in range(h-1,-1,-2):
        print(("*"*(i-2)).center(h))
else:
    for i in range(h-2,-1,-2):
        print(("*"*(i-2)).center(h))'''
#----------------------half diamond pattern---------------
'''h=int(input("enter the height"))
for i in range(h):
    for j in range(0,i+1):
        print("*",end="")
    print()
for i in range(1,h):
    for j in range(i,h):
        print("*",end="")
    print()'''
#---------------itertools.product()-----------------------------------
'''a=[1,2]
b=[3,4]
z=tuple((x,y) for x in a for y in b)
print(z)'''
'''from itertools import product
a=list(map(int,input().split()))
b=list(map(int,input().split()))
print(*list(product(a,b)))'''
#-------------------set.add()----------------------------------------------
'''s=['uk','china','france','usa','france','newzealand','uk']'''
'''for i in range(len(n)):
    s.append(n)'''
'''w=(len(set(s)))
print(w)'''
    #----------------------input----------------
'''uk
    china
    france
    usa
    france
    newzealand
    uk'''
    #-------------------------5-------------
'''n=input()
    s=[]
    for i in range(int(n)):
        s.append(input())
    print(len(set(s))'''
#-------------------------minion game-----------
#u="banana"
'''def game(u):
    vowels="aeiou"
    s=0
    k=0
    len_str=len(u)
    for letter in u:
        points=len(u)
        #print(letter)
        if letter in vowels:
            k+=points
            print(k)
        else:
            s+=points
            print(s)
        len_str-=1
    #print(s)
    #print(k)
    if s>k:
        print(f'stuart{s}')
    elif k>s:
        print(f'kevin{k}')
    else:
        print("draw")
z=game('banana')'''
'''def minion_game(string):
    vowels = "AEIOU"
    stuart_points = 0
    kevin_points = 0
    len_string = len(string)
    for letter in string:
        points = len_string
        if letter in vowels:
            kevin_points += points
        else:
            stuart_points += points
        len_string -= 1
    if stuart_points == kevin_points:
        print("Draw")
        return

    winner = f"Stuart {stuart_points}" if stuart_points > kevin_points else f"Kevin {kevin_points}"
    print(winner)
minion_game('BANANA')'''

#-------------------------------merge tools----------------
'''   STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3
Sample Output

AB
CA
AD'''
#----------------------------code------------------------
'''def merge(string,k):
    for i in range(0,len(string),k):
        substr=[]
        for j in string[i:i+k]:
            if j not in substr:
                substr.append(j)
        print("".join(substr))
merge('aabcaaada',3)'''
#-------------------countercollections--------------
#---------------------example------------------------
'''>>> from collections import Counter
>>> 
>>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
>>> print Counter(myList)
Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
>>>
>>> print Counter(myList).items()
[(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
>>> 
>>> print Counter(myList).keys()
[1, 2, 3, 4, 5]
>>> 
>>> print Counter(myList).values()
[3, 4, 4, 2, 1]
#----------code-----------------
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
#------------output--------------
200
Customer 1: Purchased size 6 shoe for $55.
Customer 2: Purchased size 6 shoe for $45.
Customer 3: Size 6 no longer available, so no purchase.
Customer 4: Purchased size 4 shoe for $40.
Customer 5: Purchased size 18 shoe for $60.
Customer 6: Size 10 not available, so no purchase.

Total money earned =  55+45+40+60=200'''

#------------------triangle quest----------------
'''
n=int(input("enter the number"))
for i in range(1,n):
    print(i*(pow(10,i)//9))
'''

#-----------------------triangle quest2-----------------
'''
n=int(input("enter the number"))
for i in range(1,n):
    print(((10**i-1)//9)**2)
'''

#-----------divmod--------------------------------------
#it is a one of bulit in function of python
#177/10  177%10
'''
a=int(input("enter value of a"))
b=int(input("enter value of b"))
print(int(a/b))
print(int(a%b))
print(divmod(a,b))
'''

#-----------power-mod-power-----------
#pow(5,4,2)=(5*5*5*5)%2
'''
a=int(input("enter value of a"))
b=int(input("enter value of b"))
c=int(input("enter value of c"))
res=pow(a,b)
res1=pow(a,b,c)
print(res)
print(res1)
'''
#---------integer comes in all size------------------
'''
a=int(input("enter value of a"))
b=int(input("enter value of b"))
c=int(input("enter value of c"))
d=int(input("enter value of d"))
res=pow(a,b)
res1=pow(c,d)
print(res+res1)
'''

#-----------------fibonacci series------------------------
#--------------recursiv----------------------
'''
def recur_fib(n):
    if n<=1:
        return n
    else:
        return(recur_fib(n-1)+recur_fib(n-2))
n=int(input("enter valid answer"))
if n<=0:
    print("enter valid numbers")
else:
    for i in range(n):
        print(recur_fib(i))
'''
#----------non-recursive------------------------
'''
a=int(input("enter first number of series"))
b=int(input("enter second number in series"))
n=int(input("enter number of terms needed"))
print(a,b,end=" ")
while n-2:
    c=a+b
    a=b
    b=c
    print(c,end=" ")
    n=n-1
'''
'''
first = 0
second = 1
print(first)
print(second)
for x in range(1,9):
    third = first + second
    print(third)
    first,second=second,third
'''
#--------------------map and lambda functions-------------------------------
'''
def fibonacci(n):
    a=0
    b=1
    c=1
    list=[]
    for _ in range(n):
        list.append(a)
        a=b
        b=c
        c=a+b
    return list
n=int(input("enter value"))
value=lambda x:x**3 #lambda print statement map ans list we must and should
print(fibonacci(n))
print(list(map(value,fibonacci(n))))
'''

#-------------------------exceptions----------------
#1/0=zeodivisionerror 1/# =value error----
#-------input----------
'''
2
1 0
1 $
'''
'''
n=int(input("enter value for n"))
#a,b=map(int,input("enter values of a,b").split())
for i in range(n):
    try:
        a,b=map(int,input("enter values of a,b").split())
        print(a//b)
    except Exception as e:
        print("error code:",e)
'''


#------------------numpy-------------------------
#--------------------array mathematics------------
#input----------
'''
1 4
1 2 3 4
5 6 7 8
'''
'''
import numpy
n,m=map(int,input("enter n,m values").split())
a=numpy.array([input("enter elements in a").split() for _ in range(n)],int)
b=numpy.array([input("enter elements in b").split() for _ in range(n)],int)
print(numpy.add(a,b))
print(numpy.subtract(a,b))
print(numpy.multiply(a,b))
print(a//b)
print(numpy.mod(a,b))
print(numpy.power(a,b))
'''
#------floor-ceil-rint---------------
#input-----
'''
1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9
'''
#output---------
'''
 1.  2.  3.  4.  5.  6.  7.  8.  9.]
[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
[  1.   2.   3.   4.   6.   7.   8.   9.  10.]
'''
'''
import numpy
numpy.set_printoptions(legacy='1.13')
n=numpy.array(input().split(),float)
print(numpy.floor(n))
print(numpy.ceil(n))
print(numpy.rint(n))
'''
#---------sum-prod------
#----------input-------
'''
2 2#n,m no.of elements in one set
1 2
3 4
'''
#-----------output----
#24
'''
import numpy
n,m=map(int,input("enter n,m values").split())
a=[]
for i in range(n):
    a.append(list(map(int,input("enter elements in array").split())))
arr=numpy.array(a)
print(numpy.sum(arr,axis=0))
print(numpy.prod(numpy.sum(arr,axis=0)))#adding horizentally
'''
#-----itertools.combinations-------------
#input----
#hack 2
'''
from itertools import combinations
word,n=input("enter word and range").split()
for i in range(1,int(n)+1):
    for j in combinations(sorted(word),i):
        print(''.join(j))
'''
#---------itertools.combinations_with_replacement-----
'''
from itertools import combinations_with_replacement
print(list(combinations_with_replacement('12345',2)))
'''
#---input-----
#hack 2
''''
from itertools import combinations_with_replacement
word,n=input("enter word and numbeer").split()
for i in combinations_with_replacement(sorted(word),int(n)):
    print(''.join(i))
'''
#----------compress the string--------------
#----input----------------------
#1222311
'''
from itertools import groupby
s=input("enter the list of numbers")
groups=groupby(s)
res=[]
for char,g in groups:
    count=len(list(g))
    res.append(f"({count}, {char})")
result=' '.join(res)
print(result)
'''
#--------------maximize it----------
#input-------------------
'''
3 1000#5**2+9**2+10**2%1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 
'''
'''
from itertools import product
n,m=map(int,input("enter m n").split())
ans=[]
for i in range(n):
    a=(list(map(int,input("enter the list").split())))
    ans.append(a[1:])
print(max([sum([x**2 for x in item]) % m  for item in product(*ans)]))
'''
#--------------------Iterables and Iterators---------------------------
#-----------input------4--a a c d----2------
#-----------output-----------------0.8333333333333333----------
'''
from itertools import combinations
n=int(input())
lst=list(map(str,input().split()))
num=int(input())
c=0
com=list(combinations(lst,num))
l=len(com)
for i in com:
    if "a" in i:
        c=c+1
print(c/l)
print(l)
print(c)
'''
#------------pilling up-------------------
#---input-------------
'''
2            T = 2
6            blocks[] size n = 6
4 3 2 1 3 4  blocks = [4, 3, 2, 1, 3, 4]
3            blocks[] size n = 3
1 3 2        blocks = [1, 3, 2]
Sample Output
'''
#-----output-----------yes---no--------
'''
t = int(input())
for _ in range(t):
    num, cubes = int(input()), list(map(int,input().split()))
    yes_no = "Yes"
    while len(cubes) > 1:
        if cubes[0] >= cubes[-1]:
            larger_num = cubes[0]
            cubes.pop(0)     
        else:
            larger_num = cubes[-1]
            cubes.pop(-1)  
        if larger_num < cubes[0] or larger_num < cubes[-1]:
            yes_no = 'No'
            break
    print(yes_no)
'''

#-------python evaluation--------------------------------
#--input--print("3+4")--------
#---output------7--------
'''s=input("enter the data")
eval(s)
'''
#from __future__ import print_function
#print(type(eval("len")))
#----any  and all------------------------------------------
#any--> if any condition  true it returns true
#all->all  conditions need to  be true
#question--all number  to be positive and any number is pallindrome
n=int(input())
l=list(map(int,input().split()))
print(all(a>0 for a in l) and any(str(a)==str(a)[::-1] for a in l))










    






























        











