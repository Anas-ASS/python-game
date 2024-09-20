
import textwrap
n=int(input())

for i in range(1,n+1):
    print(f"{i}{"  "}{oct(i)[2:]}{"    "}{hex(i)[2:].upper()}{"     "}{bin(i)[2:]}")
    
v=n*3

for i in range(1,n,2):
    p=".|"*i
    print(p.center(v,"-"))
print("WELCOME".center(v,"-"))
for i in range(n-2,0,-2):
    p=".|"*i
    print(p.center(v,"-"))


n=input()
x=int(input())
def wrap(n,x):
    return textwrap.fill(n,x)
print(wrap(n,x))
n=input()

print(n.rjust(20," "))
print(n.center(20))

n= input()
c=input()

print(n.count(c))



n=input("name")
c=input("namel")
print(f"""
      Hello
      {n}
      {c}
      you just develop 
      python
      
      """)
n= input().split()
n="-".join(n)
print(n)
n=input()
def switchcase(x):
     return x.swapcase()
print(switchcase(n))
         



n=int(input())
listi=list(map(int,input().split()))
t=tuple(listi)
print(hash(t))
l=[]

n=input()
for i in range(int(n)):
    k,*line=input().split()
    if k=="insert":
        l.insert(int(line[0]),int(line[1]))
    elif k=="print":
        print(l)
    elif k=="remove":
        l.remove(int(line[0]))
    elif k=="append":
        l.append(int(line[0]))
    elif k=="sort":
        l.sort()
    elif k=="pop":
        l.pop()
    elif k=="reverse":
        l.reverse()
    else:
        print("uncorecct value ")





student={}
for i in range (int (input())):
    name,*line=input().split()
    score=list(map(float,line))
    student[name]=score
queryname=input()
if  queryname in student:
    print( sum(student[queryname])/len(student[queryname]))




print("Hello,World")
a=[]
sett=set()
for i in range (int (input())):
    name=input("name")
    score=int(input("score"))
    a.append([name,score])
    sett.add(score)
secondscor=sorted(sett)[1]
secoundst=[student[0] for student in a if student[1]==secondscor]
secoundst.sort()
for student in secoundst:
    print(student,a[score])

while b in a:
    a.remove(b)
c=min(a)
while c in a:
    print (c)
arr=map(int,input("ee").split())

bb=list(arr)
ma=max(bb)
while ma in bb:
    bb.remove(ma)

print(max(bb))
a=int(input("aaaa"))
b=int(input("aaaa"))
c=int(input("aaaa"))
n=int(input("aaaa"))
cordinate=[[i,j,k]for i in range(a+1) for j in range(b+1)for k in range(c+1)if i+j+k !=n]
print (cordinate)

while True:
    x=input("Enter your number")
    if x=="exit":
        break    
    userinput=int(x)
    if userinput %2==0 and userinput in range(2,5):
        print("Not Wierd")
    elif userinput%2==0 and userinput in range(6,20):
        print("wierd")
    elif userinput%2==0 and userinput >20:
        print("not wierd")
    else:print("wierd")

a=int(input(" enter your first number :  "))
b=int(input(" enter your second number :  "))
f=a+b
s=a-b
l=a*b
print(f"""
          {f}
          {s}
          {l}""")

def prinsqureallpositivenum(x):
    v=[]
    i=0
    while x>=0:

        v.append(i*i)
        i+=1
        x-=1
    return v
        
    

a=int(input("enter"))

print(prinsqureallpositivenum(a))

a=int(input("enter"))

def leap(b):
    x=bool
    if b%4==0:
        if b%100==0:
            if b%400==0:
                x=True
            else:
                x=False
        else:    
            x=True
    else:
        x=False
    return x
print(leap(a))





         
      
      