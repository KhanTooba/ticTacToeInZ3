import z3
import copy

def checkFun(arr, step):
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

print(checkFun([0, 0, 0, 1, 1, 2, 2, 2, 1],2))