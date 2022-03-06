from abc import *
import z3

def checkFun(arr, step):
    s = z3.Solver()
    myArray = z3.IntVector('myArray',9)
    # arr=[0,2,0,2,1,1,2,0,1]
    for i in range(len(arr)):
        s.add(myArray[i]==arr[i])

    # step=7

    s.add(z3.Or(z3.And(myArray[0]==0,myArray[1]==1,myArray[2]==1,step==0),
                        z3.And(myArray[0]==1,myArray[1]==0,myArray[2]==1,step==1),
                        z3.And(myArray[0]==1,myArray[1]==1,myArray[2]==0,step==2),
                        
                        z3.And(myArray[3]==0,myArray[4]==1,myArray[5]==1,step==3),
                        z3.And(myArray[3]==1,myArray[4]==0,myArray[5]==1,step==4),
                        z3.And(myArray[3]==1,myArray[4]==1,myArray[5]==0,step==5),
                        
                        z3.And(myArray[6]==0,myArray[7]==1,myArray[8]==1,step==6),
                        z3.And(myArray[6]==1,myArray[7]==0,myArray[8]==1,step==7),
                        z3.And(myArray[6]==1,myArray[7]==1,myArray[8]==0,step==8),
                    
                        z3.And(myArray[0]==0,myArray[3]==1,myArray[6]==1,step==0),
                        z3.And(myArray[0]==1,myArray[3]==0,myArray[6]==1,step==3),
                        z3.And(myArray[0]==1,myArray[3]==1,myArray[6]==0,step==6),
                        
                        z3.And(myArray[1]==0,myArray[4]==1,myArray[7]==1,step==1),
                        z3.And(myArray[1]==1,myArray[4]==0,myArray[7]==1,step==4),
                        z3.And(myArray[1]==1,myArray[4]==1,myArray[7]==0,step==7),
                        
                        z3.And(myArray[2]==0,myArray[5]==1,myArray[8]==1,step==2),
                        z3.And(myArray[2]==1,myArray[5]==0,myArray[8]==1,step==5),
                        z3.And(myArray[2]==1,myArray[5]==1,myArray[8]==0,step==8),
                        
                        z3.And(myArray[0]==0,myArray[4]==1,myArray[8]==1,step==0),
                        z3.And(myArray[0]==1,myArray[4]==0,myArray[8]==1,step==4),
                        z3.And(myArray[0]==1,myArray[4]==1,myArray[8]==0,step==8),
                        
                        z3.And(myArray[6]==0,myArray[4]==1,myArray[2]==1,step==6),
                        z3.And(myArray[6]==1,myArray[4]==0,myArray[2]==1,step==4),
                        z3.And(myArray[6]==1,myArray[4]==1,myArray[2]==0,step==2))) 
    if s.check() == z3.sat:
        return "good"

    s = z3.Solver()
    myArray = z3.IntVector('myArray',9)
    # arr=[0,2,0,2,1,1,2,0,1]
    for i in range(len(arr)):
        s.add(myArray[i]==arr[i])

    # step=7

    s.add(z3.Or(z3.And(myArray[0]==0,myArray[1]==1,myArray[2]==1,step!=0),
                        z3.And(myArray[0]==1,myArray[1]==0,myArray[2]==1,step!=1),
                        z3.And(myArray[0]==1,myArray[1]==1,myArray[2]==0,step!=2),
                        
                        z3.And(myArray[3]==0,myArray[4]==1,myArray[5]==1,step!=3),
                        z3.And(myArray[3]==1,myArray[4]==0,myArray[5]==1,step!=4),
                        z3.And(myArray[3]==1,myArray[4]==1,myArray[5]==0,step!=5),
                        
                        z3.And(myArray[6]==0,myArray[7]==1,myArray[8]==1,step!=6),
                        z3.And(myArray[6]==1,myArray[7]==0,myArray[8]==1,step!=7),
                        z3.And(myArray[6]==1,myArray[7]==1,myArray[8]==0,step!=8),
                    
                        z3.And(myArray[0]==0,myArray[3]==1,myArray[6]==1,step!=0),
                        z3.And(myArray[0]==1,myArray[3]==0,myArray[6]==1,step!=3),
                        z3.And(myArray[0]==1,myArray[3]==1,myArray[6]==0,step!=6),
                        
                        z3.And(myArray[1]==0,myArray[4]==1,myArray[7]==1,step!=1),
                        z3.And(myArray[1]==1,myArray[4]==0,myArray[7]==1,step!=4),
                        z3.And(myArray[1]==1,myArray[4]==1,myArray[7]==0,step!=7),
                        
                        z3.And(myArray[2]==0,myArray[5]==1,myArray[8]==1,step!=2),
                        z3.And(myArray[2]==1,myArray[5]==0,myArray[8]==1,step!=5),
                        z3.And(myArray[2]==1,myArray[5]==1,myArray[8]==0,step!=8),
                        
                        z3.And(myArray[0]==0,myArray[4]==1,myArray[8]==1,step!=0),
                        z3.And(myArray[0]==1,myArray[4]==0,myArray[8]==1,step!=4),
                        z3.And(myArray[0]==1,myArray[4]==1,myArray[8]==0,step!=8),
                        
                        z3.And(myArray[6]==0,myArray[4]==1,myArray[2]==1,step!=6),
                        z3.And(myArray[6]==1,myArray[4]==0,myArray[2]==1,step!=4),
                        z3.And(myArray[6]==1,myArray[4]==1,myArray[2]==0,step!=2))) 
    if s.check() == z3.sat:
        return "bad"
    
    s = z3.Solver()
    myArray = z3.IntVector('myArray',9)
    # arr=[0,2,0,2,1,1,2,0,1]
    for i in range(len(arr)):
        s.add(myArray[i]==arr[i])
        
    s.add(z3.Or(z3.And(myArray[0]==0,myArray[1]==2,myArray[2]==2,step!=0),
                        z3.And(myArray[0]==2,myArray[1]==0,myArray[2]==2,step!=1),
                        z3.And(myArray[0]==2,myArray[1]==2,myArray[2]==0,step!=2),

                        z3.And(myArray[3]==0,myArray[4]==2,myArray[5]==2,step!=3),
                        z3.And(myArray[3]==2,myArray[4]==0,myArray[5]==2,step!=4),
                        z3.And(myArray[3]==2,myArray[4]==2,myArray[5]==0,step!=5),
                        
                        z3.And(myArray[6]==0,myArray[7]==2,myArray[8]==2,step!=6),
                        z3.And(myArray[6]==2,myArray[7]==0,myArray[8]==2,step!=7),
                        z3.And(myArray[6]==2,myArray[7]==2,myArray[8]==0,step!=8),
                        
                        z3.And(myArray[0]==0,myArray[3]==2,myArray[6]==2,step!=0),
                        z3.And(myArray[0]==2,myArray[3]==0,myArray[6]==2,step!=3),
                        z3.And(myArray[0]==2,myArray[3]==2,myArray[6]==0,step!=6),
                        
                        z3.And(myArray[1]==0,myArray[4]==2,myArray[7]==2,step!=1),
                        z3.And(myArray[1]==2,myArray[4]==0,myArray[7]==2,step!=4),
                        z3.And(myArray[1]==2,myArray[4]==2,myArray[7]==0,step!=7),
                        
                        z3.And(myArray[2]==0,myArray[5]==2,myArray[8]==2,step!=2),
                        z3.And(myArray[2]==2,myArray[5]==0,myArray[8]==2,step!=5),
                        z3.And(myArray[2]==2,myArray[5]==2,myArray[8]==0,step!=8),
                        
                        z3.And(myArray[0]==0,myArray[4]==2,myArray[8]==2,step!=0),
                        z3.And(myArray[0]==2,myArray[4]==0,myArray[8]==2,step!=4),
                        z3.And(myArray[0]==2,myArray[4]==2,myArray[8]==0,step!=8),
                        
                        z3.And(myArray[6]==0,myArray[4]==2,myArray[2]==2,step!=6),
                        z3.And(myArray[6]==2,myArray[4]==0,myArray[2]==2,step!=4),
                        z3.And(myArray[6]==2,myArray[4]==2,myArray[2]==0,step!=2)))
        

    if s.check() == z3.sat:
        return "bad"
    else:
        return "good"

s = z3.Solver()
myArray = z3.IntVector('myArray',9)
for i in range(9):
    s.add(z3.Or(myArray[i]==1, myArray[i]==2, myArray[i]==0))

counter2 = z3.IntVector('counter2',10)
counter1 = z3.IntVector('counter1',10)
counter3 = z3.IntVector('counter3',10)
move = z3.Int('move')
s.add(counter1[0]==0)
s.add(counter2[0]==0)
s.add(counter3[0]==0)
s.add(z3.And(move>=0,move<=8))
# print(type(move))
s.add(z3.Not(z3.Or(z3.And(myArray[0]==1,myArray[1]==1,myArray[2]==1),
                    z3.And(myArray[0]==2,myArray[1]==2,myArray[2]==2),
                    
                    z3.And(myArray[3]==1,myArray[4]==1,myArray[5]==1),
                    z3.And(myArray[3]==2,myArray[4]==2,myArray[5]==2),
                    
                    z3.And(myArray[6]==1,myArray[7]==1,myArray[8]==1),
                    z3.And(myArray[6]==2,myArray[7]==2,myArray[8]==2),
                    
                    z3.And(myArray[0]==1,myArray[3]==1,myArray[6]==1),
                    z3.And(myArray[0]==2,myArray[3]==2,myArray[6]==2),
                    
                    z3.And(myArray[1]==1,myArray[4]==1,myArray[7]==1),
                    z3.And(myArray[1]==2,myArray[4]==2,myArray[7]==2),
                    
                    z3.And(myArray[2]==1,myArray[5]==1,myArray[8]==1),
                    z3.And(myArray[2]==2,myArray[5]==2,myArray[8]==2),
                    
                    z3.And(myArray[0]==1,myArray[4]==1,myArray[8]==1),
                    z3.And(myArray[0]==2,myArray[4]==2,myArray[8]==2),
                    
                    z3.And(myArray[6]==1,myArray[4]==1,myArray[2]==1),
                    z3.And(myArray[6]==2,myArray[4]==2,myArray[2]==2))))  

for i in range(9):
    s.add(z3.If(myArray[i]==2,counter2[i+1]==counter2[i]+1,counter2[i+1]==counter2[i]))
    s.add(z3.If(myArray[i]==1,counter1[i+1]==counter1[i]+1,counter1[i+1]==counter1[i]))
    s.add(z3.If(myArray[i]!=0,counter3[i+1]==counter3[i]+1,counter3[i+1]==counter3[i]))
    s.add(z3.Implies(move == i, myArray[i] == 0)) 
    
s.add(z3.Or(counter1[9]==2, counter1[9]==3))
s.add(z3.Or(counter2[9]==2, counter2[9]==3))
s.add(z3.Or(counter3[9]==4, counter3[9]==6))
x = z3.Int('x')
x = counter2[9]+counter2[9]
s.add(z3.Or(x==4, x==6))
c = 0
# print(s.check())
while s.check() == z3.sat:
    m = s.model()
    arr = sorted ([(d, m[d]) for d in m], key = lambda x: str(x[0]))
    u=0
    time=1
    toSend=[]
    for a in arr:
        if str(a[0]) != None and "counter" not in str(a[0]):
            u=u+1
            if time==1:
                u=0
            if time!=1:
                toSend.append(a[1])
            time=time+1
           
            if u==3:
                u=0
    for i in range(9):
        if i==s.model()[move]:
            # print(i)
            break
    print(toSend,";",i,";",end="")
    print(checkFun(toSend,i))
    c = c+1
    s.add(z3.Or( myArray[0] != s.model()[myArray[0]], myArray[1] != s.model()[myArray[1]],
                 myArray[2] != s.model()[myArray[2]], myArray[3] != s.model()[myArray[3]],
                 myArray[4] != s.model()[myArray[4]], myArray[5] != s.model()[myArray[5]],
                 myArray[6] != s.model()[myArray[6]], myArray[7] != s.model()[myArray[7]],
                 myArray[8] != s.model()[myArray[8]], move!= s.model()[move]))

print(c)