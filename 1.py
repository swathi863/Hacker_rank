#-----------nested lists-----------------------
'''names=['swathi','siri','niki','devanshika','venky']
score=['37.21','37.21','37.2','41','39']
s=list(zip(names,score))
#print(s)
check=sorted(y[1] for y in s)[1]
#print(check)
result=sorted(i[0] for i in s if i[1]==check)
print('\n'.join(result))'''
#--------finding_percentage----------------------------------
'''l={'harsha':[23,8.0,7],'swathi':[5,9,5]}
key='swathi'
val=l[key]
s=0
for i in range(0,len(val)):
    s=s+val[i]
    print(s)
avg=s/len(val)
print("{:.2f}".format(avg))'''
#----------------hash-----------------------------------------------
'''l=(1,2)
print(hash(1))
t=tuple(map(int,l.split()))
print(hash(t))'''
#----------------dimensions------------------
'''x=1
y=1
z=1
n=2
print(list([i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k !=n))'''
#-----------------------------string formatting----------------------
#------------------------------output--------------------------------
'''    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001'''
#----------------------------program-------------------------------
''''number=17
for i in range(1,number+1):
    width=len(bin(number)[2:])
    deci=str(i)
    octa=oct(i)[2:]
    hexa=hex(i)[2:].upper()
    bina=bin(i)[2:]
    print(deci.rjust(width),octa.rjust(width),hexa.rjust(width),bina.rjust(width))'''
#--------------------------------ljust(),rjust(),center()----------------------------------
'''s='swathi'
l=13
char='*'
print("rjust with char:",s.rjust(l,char))
print("rjust without char:",s.rjust(l))
print("ljust with char:",s.ljust(l,char))
print("center with char:",s.center(l,char))'''
#--------------------------door-mat-----------------------------------------------------
'''h=int(input("enter the height"))
dis=int(input("enter the distance"))
for i in range(1,h,2):
    print((".|."*i).center(dis,'-'))
print('welcome'.center(dis,'-'))
if(h%2!=0):
    for i in range(h-2,-1,-2):
        print(('.|.'*i).center(dis,'-'))
else:
    for i in range(h-1,-1,-2):
        print(('.|.'*i).center(dis,'-'))'''
#------------------set.discard(),remove(),pop()--------------------------
#input----------
'''9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop
discard 6
remove 5
pop
discard 5'''
#code-------------
'''n=int(input("enter your input"))#n=int(input())
s=set(input("enter the numbers in set"))#s=set(map(int,input().split())
for i in range(n):
    x=input("enter your input").split()#x=input().split()
    if x[0]=='pop':#pop first element from set
        s.pop()
    elif x[0]=='remove':#remove an element from set
        s.remove((x[1]))
    elif x[0]=='discard':#discard an element from set
        s.discard((x[1]))
print(s)#sum s
'''
#word count ---debugging-------------------------------
#if number of vowels in word is odd then consider else even means consider as 2
'''def is_vowel(letter):
    return letter in ['a','e','i','o','u','y']
def score_words(words):
    score=0
    for word in words:
        num_vowels=0
        for letter in word:
            if is_vowel(letter):
                num_vowels +=1
        if num_vowels%2==0:
            score +=2
        else:
            score +=1
    return score
n=int(input("enter number of words"))
words=input("enter the words").split()
print(score_words(words))
'''
#-------ordereddict--------------
#an ordereddict is a dictionary that remembers the order of the keys that were inserted first
#if new one is replaced then values changes
#---input-----------
'''9
banana fries 12
potato chips 30
candy 5
apple juice 10
candy 5
candy 5
candy 5
candy 5
apple juice 10
potato chpis 30'''

'''
from collections import OrderedDict
n=int(input("enter number of times"))
new=OrderedDict()
for i in range(n):
    x=input("enter the input()").split()
    item=' '.join(x[0:len(x)-1])
    price=int(x[-1])
    if item in new:
        new[item] +=price
    else:
        new[item]=price
ans=list(new.items())
for item in ans:
    print(item[0],item[1])
'''

#-----set mutations--------------------------

#--------update---------------
'''h=set("Hacker")
r=set("Rank")
h.update(r)
print(h)'''
#----------intersection_update--------common elements-------------
'''h=set("Hacker")
r=set("Rank")
h.intersection_update(r)
print(h)'''
#-----difference_update--removing common elements--------------
'''h=set("Hacker")
r=set("Rank")
h.difference_update(r)
print(h)'''
#----symmetric_diffrence_update--------------
#if element is present it will remove if not it will insert element
'''h=set("Hacker")
r=set("Rank")
h.symmetric_difference_update(r)
print(h)'''
'''
n=int(input("enter no.of elements"))#n=int(input())
a=set(map(int,input("enter the elements with space").split()))#a=set(map(int,input().split()))
l=int(input("enter number of operations"))#l=int(input())
for i in range(l):
    orp,i=input("enter your operations").split()#input().split()
    s=set(map(int,input("enter the other set").split()))#=set(map(int,input().split()))
    if orp=="intersection_update":
        a.intersection_update(s)
    elif orp=="update":
        a.update(s)
    elif orp=="symmetric_difference_update":
        a.symmetric_difference_update(s)
    elif orp=="difference_update":
        a.difference_update(s)
print(sum(a))
'''
#---input------------
'''
16
1 2 3 4 5 6 7  8 9 10 11 12 13 14 24 52
4
in 10
2 3 5 6 8 9 1 4 7 11
update 2
55 56
symm 5
22 7 35 62 58
diff 7
11 22 35 55 58 56 62 66
#----------------output----38
'''

#-----symmetric difference---------------
#input----------#to find uncommon elements and sort in order
'''4           
2 4 5 9     
4   
2 4 11 12'''
'''
n=int(input("enter how many elements in set1"))
n1=set(list(map(int,input("enter the elements in set1 with gap").split())))
#n1=set(list(map(int,input().split())))
m=int(input("enter how many elements in set2"))
m1=set(list(map(int,input("enter the elements in set2 with gap").split())))
#m1=set(list(map(int,input().split())))
res=n1.symmetric_difference(m1)
print(res)
list1=list(res)
list1.sort()
for i in list1:
    print(i)
'''
#-----------various operations in set----------------
#---------------input-------------------
'''
9 #total number of eng newspapers reading persons
1 2 3 4 5 6 7 8 9 #id's of reading persons
9 #french newspapers reading persons
10 1 2 3 11 21 55 6 8
'''
#task to find how many members reading english paper #difference
#task to find who either eng or french but not both
#task to find total members at least one newspaper
#task to find total both newspaper
'''
n=int(input("enter total number of english newspaper members"))
eng=set(map(int,input("enter id's of persons").split()))
n1=int(input("enter total number of french newspaper members"))
french=set(map(int,input("enter id's of persons").split()))
print("count of only english newspapers reading menbers")
print(len(eng.difference(french)))
print("count of either eng or french but not both")
print(len(eng.symmetric_difference(french)))
print("count of at least one newspaper reading persons")
print(len(eng.union(french)))
print("count of both reading members")
print(len(eng.intersection(french)))

'''
#------------------captions room-----------
#----input-----------
'''
5#there 6 group of families which are taken separate room and one caption room then find caption room number
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2
#caption room is unique
'''
'''
n=int(input("enter how many members in a room"))
rooms=list(map(int,input("enter the room members").split()))
lst=set(rooms)
for i in lst:
    rooms.remove(i)
now=set(rooms)
ans=lst.difference(now)
ans=list(ans)
print(ans[0])
'''

#---------check subset--------------
#-----input-----
'''3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2
'''
#checking a is sub set of b or not
'''
n=int(input("enter no.of operations"))
while n!=0:
    a=int(input("enter no.of elements in set a"))
    set_a=set(map(int,input("enter elements in set a").split()))
    #print(set_a)
    b=int(input("enter no.of elements in set b"))
    set_b=set(map(int,input("enter elements in set b").split()))
    #print(set_b)
    if set_a.issubset(set_b):
        print("True")
    else:
        print("False")
    n=n-1
'''
#-------------check super strict set---
#if given n sets is not present one return false
#----------input---------
'''
1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12
'''
'''
a=set(map(int,input("enter the elements in set a").split()))
n=int(input("no.of other sets"))
C=0
while n!=0:
    b=set(map(int,input("enter elements in other set").split()))
    if a!=b:
        if a.issuperset(b):
            C=C+0
        else:
            C=C+1
    else:
        c=c+1
    n=n-1
if C==0:
    print("True")
else:
    print("False")
'''    
#-----------------no-idea------------------------------------
#-----------------input---------------
'''
3 2
1 5 3
3 1
5 7
'''
'''
n,m=map(int,input("enter n m values").split())
arr=list(map(int,input("enter array elements").split()))
a=set(map(int,input("enter values in a").split()))
b=set(map(int,input("enter values in b").split()))
h=0
for i in arr:
    if i in a:
        h=h+1
    elif i in b:
        h=h-1
    else:
        pass
print(h)
'''
#---------find angle MBC------------
#----------inpuut----------
'''
10
10
'''

'''
from math import atan,degrees
ab=int(input("enter lenght of ab"))
bc=int(input("enter lenght ogf bc"))
print(round(degrees(atan(ab/bc))),chr(176),sep='')
'''
#-------------polar coordinates--------------------
#------------input-----------------------
#1+2j
'''
import cmath
z=input("enter the complex")
print(abs(complex(z)))
print(cmath.phase(complex(z)))
'''
#-------gintroS-----------------------------------
#-------input---Sorting1234------------
#---------output----------ginortS1324--------------
s=input()
alpha=[i for i in s if i.isalpha()]
upper=[i  for i in alpha if i.isupper()]
upper.sort()
lower=[i for i in alpha if i.islower()]
lower.sort()
num=[int(i) for i in s if i.isdigit()]
even=[str(i) for i in num if i%2==0]
even.sort()
odd=[str(i) for i in num if i%2!=0]
odd.sort()
res=lower+upper+odd+even
print("".join(res))








    











        









            





















        
