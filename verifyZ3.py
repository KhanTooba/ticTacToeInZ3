from time import time
import keras
from tensorflow import keras
import z3
import numpy as np

modelKeras = keras.models.load_model("classifier.h5")

def convert(c):
    c=str(c)
    if "1" in c:
        return "010"
    elif "0" in c:
        return "100"
    elif "2" in c:
        return "001" 
    return 0 

def convertMove(c):
    c=str(c)
    if "0" in c:
        return "100000000"
    elif "1" in c:
        return "010000000"
    elif "2" in c:
        return "001000000"
    elif "3" in c:
        return "000100000"
    elif "4" in c:
        return "000010000"
    elif "5" in c:
        return "000001000"
    elif "6" in c:
        return "000000100"
    elif "7" in c:
        return "000000010"
    elif "8" in c:
        return "000000001" 
    return 0 

def Relu(x):
    return np.vectorize(lambda y: z3.If(y >= 0 , y, z3.RealVal(0)))(x)

def result(x):
    w1, b1, w2, b2, w3, b3, w4, b4 = modelKeras.get_weights()
    l1 = w1.T @ x +b1
    l1_out = Relu(l1)
    l2 = w2.T @ l1_out +b2
    l2_out = Relu(l2)
    l3 = w3.T @ l2_out +b3
    l3_out = Relu(l3)
    l4 = w4.T @ l3_out +b4
    l4_out = Relu(l4)
    return l4

def query1():
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
    s.add(z3.Not(z3.Or(z3.And(myArray[0]==0,myArray[1]==1,myArray[2]==1,move==0),
                        z3.And(myArray[0]==1,myArray[1]==0,myArray[2]==1,move==1),
                        z3.And(myArray[0]==1,myArray[1]==1,myArray[2]==0,move==2),
                        
                        z3.And(myArray[3]==0,myArray[4]==1,myArray[5]==1,move==3),
                        z3.And(myArray[3]==1,myArray[4]==0,myArray[5]==1,move==4),
                        z3.And(myArray[3]==1,myArray[4]==1,myArray[5]==0,move==5),
                        
                        z3.And(myArray[6]==0,myArray[7]==1,myArray[8]==1,move==6),
                        z3.And(myArray[6]==1,myArray[7]==0,myArray[8]==1,move==7),
                        z3.And(myArray[6]==1,myArray[7]==1,myArray[8]==0,move==8),
                    
                        z3.And(myArray[0]==0,myArray[3]==1,myArray[6]==1,move==0),
                        z3.And(myArray[0]==1,myArray[3]==0,myArray[6]==1,move==3),
                        z3.And(myArray[0]==1,myArray[3]==1,myArray[6]==0,move==6),
                        
                        z3.And(myArray[1]==0,myArray[4]==1,myArray[7]==1,move==1),
                        z3.And(myArray[1]==1,myArray[4]==0,myArray[7]==1,move==4),
                        z3.And(myArray[1]==1,myArray[4]==1,myArray[7]==0,move==7),
                        
                        z3.And(myArray[2]==0,myArray[5]==1,myArray[8]==1,move==2),
                        z3.And(myArray[2]==1,myArray[5]==0,myArray[8]==1,move==5),
                        z3.And(myArray[2]==1,myArray[5]==1,myArray[8]==0,move==8),
                        
                        z3.And(myArray[0]==0,myArray[4]==1,myArray[8]==1,move==0),
                        z3.And(myArray[0]==1,myArray[4]==0,myArray[8]==1,move==4),
                        z3.And(myArray[0]==1,myArray[4]==1,myArray[8]==0,move==8),
                        
                        z3.And(myArray[6]==0,myArray[4]==1,myArray[2]==1,move==6),
                        z3.And(myArray[6]==1,myArray[4]==0,myArray[2]==1,move==4),
                        z3.And(myArray[6]==1,myArray[4]==1,myArray[2]==0,move==2))))

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

    s.add(z3.Or(z3.And(myArray[0]==0,myArray[1]==2,myArray[2]==2,move!=0),
                            z3.And(myArray[0]==2,myArray[1]==0,myArray[2]==2,move!=1),
                            z3.And(myArray[0]==2,myArray[1]==2,myArray[2]==0,move!=2),

                            z3.And(myArray[3]==0,myArray[4]==2,myArray[5]==2,move!=3),
                            z3.And(myArray[3]==2,myArray[4]==0,myArray[5]==2,move!=4),
                            z3.And(myArray[3]==2,myArray[4]==2,myArray[5]==0,move!=5),
                            
                            z3.And(myArray[6]==0,myArray[7]==2,myArray[8]==2,move!=6),
                            z3.And(myArray[6]==2,myArray[7]==0,myArray[8]==2,move!=7),
                            z3.And(myArray[6]==2,myArray[7]==2,myArray[8]==0,move!=8),
                            
                            z3.And(myArray[0]==0,myArray[3]==2,myArray[6]==2,move!=0),
                            z3.And(myArray[0]==2,myArray[3]==0,myArray[6]==2,move!=3),
                            z3.And(myArray[0]==2,myArray[3]==2,myArray[6]==0,move!=6),
                            
                            z3.And(myArray[1]==0,myArray[4]==2,myArray[7]==2,move!=1),
                            z3.And(myArray[1]==2,myArray[4]==0,myArray[7]==2,move!=4),
                            z3.And(myArray[1]==2,myArray[4]==2,myArray[7]==0,move!=7),
                            
                            z3.And(myArray[2]==0,myArray[5]==2,myArray[8]==2,move!=2),
                            z3.And(myArray[2]==2,myArray[5]==0,myArray[8]==2,move!=5),
                            z3.And(myArray[2]==2,myArray[5]==2,myArray[8]==0,move!=8),
                            
                            z3.And(myArray[0]==0,myArray[4]==2,myArray[8]==2,move!=0),
                            z3.And(myArray[0]==2,myArray[4]==0,myArray[8]==2,move!=4),
                            z3.And(myArray[0]==2,myArray[4]==2,myArray[8]==0,move!=8),
                            
                            z3.And(myArray[6]==0,myArray[4]==2,myArray[2]==2,move!=6),
                            z3.And(myArray[6]==2,myArray[4]==0,myArray[2]==2,move!=4),
                            z3.And(myArray[6]==2,myArray[4]==2,myArray[2]==0,move!=2)))
            
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
    c=0
    b=0
    print(s.check())
    # print(s.model())
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
        step=-1
        for i in range(9):
            if i==s.model()[move]:
                # print(i)
                step=i
                break
        newRow=[]
        input=""
        count1 = 0
        for element in toSend:
            if count1==9:
                input = input + convertMove(element)
            elif count1==10:
                output = str(element)
            else:
                input = input + convert(element)
            count1=count1+1
        newRow = list(input+convertMove(str(i)))
        x= z3.IntVector('x',36)
        s2 = z3.Solver()
        for i in range(36):
            s2.add(x[i]==int(newRow[i]))
        
        sample1 = [int(k) for k in newRow]
        out = modelKeras.predict([sample1])

        y_pred = result(x)
        s2.add(y_pred[0]>y_pred[1])
        if out[0][0]<out[0][1] and s2.check()==z3.unsat:
            print("Exception exists in: ",toSend,";",step)
            print("result returned by DNN: ",out)
            return -1
        s.add(z3.Or( myArray[0] != s.model()[myArray[0]], myArray[1] != s.model()[myArray[1]],
                    myArray[2] != s.model()[myArray[2]], myArray[3] != s.model()[myArray[3]],
                    myArray[4] != s.model()[myArray[4]], myArray[5] != s.model()[myArray[5]],
                    myArray[6] != s.model()[myArray[6]], myArray[7] != s.model()[myArray[7]],
                    myArray[8] != s.model()[myArray[8]], move!= s.model()[move]))
    return 0

def query2():
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
    s.add(z3.Not(z3.Or(z3.And(myArray[0]==0,myArray[1]==1,myArray[2]==1,move==0),
                        z3.And(myArray[0]==1,myArray[1]==0,myArray[2]==1,move==1),
                        z3.And(myArray[0]==1,myArray[1]==1,myArray[2]==0,move==2),
                        
                        z3.And(myArray[3]==0,myArray[4]==1,myArray[5]==1,move==3),
                        z3.And(myArray[3]==1,myArray[4]==0,myArray[5]==1,move==4),
                        z3.And(myArray[3]==1,myArray[4]==1,myArray[5]==0,move==5),
                        
                        z3.And(myArray[6]==0,myArray[7]==1,myArray[8]==1,move==6),
                        z3.And(myArray[6]==1,myArray[7]==0,myArray[8]==1,move==7),
                        z3.And(myArray[6]==1,myArray[7]==1,myArray[8]==0,move==8),
                    
                        z3.And(myArray[0]==0,myArray[3]==1,myArray[6]==1,move==0),
                        z3.And(myArray[0]==1,myArray[3]==0,myArray[6]==1,move==3),
                        z3.And(myArray[0]==1,myArray[3]==1,myArray[6]==0,move==6),
                        
                        z3.And(myArray[1]==0,myArray[4]==1,myArray[7]==1,move==1),
                        z3.And(myArray[1]==1,myArray[4]==0,myArray[7]==1,move==4),
                        z3.And(myArray[1]==1,myArray[4]==1,myArray[7]==0,move==7),
                        
                        z3.And(myArray[2]==0,myArray[5]==1,myArray[8]==1,move==2),
                        z3.And(myArray[2]==1,myArray[5]==0,myArray[8]==1,move==5),
                        z3.And(myArray[2]==1,myArray[5]==1,myArray[8]==0,move==8),
                        
                        z3.And(myArray[0]==0,myArray[4]==1,myArray[8]==1,move==0),
                        z3.And(myArray[0]==1,myArray[4]==0,myArray[8]==1,move==4),
                        z3.And(myArray[0]==1,myArray[4]==1,myArray[8]==0,move==8),
                        
                        z3.And(myArray[6]==0,myArray[4]==1,myArray[2]==1,move==6),
                        z3.And(myArray[6]==1,myArray[4]==0,myArray[2]==1,move==4),
                        z3.And(myArray[6]==1,myArray[4]==1,myArray[2]==0,move==2))))

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

    s.add(z3.Or(z3.And(myArray[0]==0,myArray[1]==2,myArray[2]==2,move!=0),
                            z3.And(myArray[0]==2,myArray[1]==0,myArray[2]==2,move!=1),
                            z3.And(myArray[0]==2,myArray[1]==2,myArray[2]==0,move!=2),

                            z3.And(myArray[3]==0,myArray[4]==2,myArray[5]==2,move!=3),
                            z3.And(myArray[3]==2,myArray[4]==0,myArray[5]==2,move!=4),
                            z3.And(myArray[3]==2,myArray[4]==2,myArray[5]==0,move!=5),
                            
                            z3.And(myArray[6]==0,myArray[7]==2,myArray[8]==2,move!=6),
                            z3.And(myArray[6]==2,myArray[7]==0,myArray[8]==2,move!=7),
                            z3.And(myArray[6]==2,myArray[7]==2,myArray[8]==0,move!=8),
                            
                            z3.And(myArray[0]==0,myArray[3]==2,myArray[6]==2,move!=0),
                            z3.And(myArray[0]==2,myArray[3]==0,myArray[6]==2,move!=3),
                            z3.And(myArray[0]==2,myArray[3]==2,myArray[6]==0,move!=6),
                            
                            z3.And(myArray[1]==0,myArray[4]==2,myArray[7]==2,move!=1),
                            z3.And(myArray[1]==2,myArray[4]==0,myArray[7]==2,move!=4),
                            z3.And(myArray[1]==2,myArray[4]==2,myArray[7]==0,move!=7),
                            
                            z3.And(myArray[2]==0,myArray[5]==2,myArray[8]==2,move!=2),
                            z3.And(myArray[2]==2,myArray[5]==0,myArray[8]==2,move!=5),
                            z3.And(myArray[2]==2,myArray[5]==2,myArray[8]==0,move!=8),
                            
                            z3.And(myArray[0]==0,myArray[4]==2,myArray[8]==2,move!=0),
                            z3.And(myArray[0]==2,myArray[4]==0,myArray[8]==2,move!=4),
                            z3.And(myArray[0]==2,myArray[4]==2,myArray[8]==0,move!=8),
                            
                            z3.And(myArray[6]==0,myArray[4]==2,myArray[2]==2,move!=6),
                            z3.And(myArray[6]==2,myArray[4]==0,myArray[2]==2,move!=4),
                            z3.And(myArray[6]==2,myArray[4]==2,myArray[2]==0,move!=2)))

    s.add(z3.Or(myArray[0]==1,myArray[2]==1,myArray[8]==1,myArray[6]==1))
    s.add(myArray[4]==1)

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
    print(s.check())
    # print(s.model())
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
        step=-1
        for i in range(9):
            if i==s.model()[move]:
                # print(i)
                step=i
                break
        newRow=[]
        input=""
        output=""
        count1 = 0
        for element in toSend:
            if count1==9:
                input = input + convertMove(element)
            else:
                input = input + convert(element)
            count1=count1+1
        newRow = list(input+convertMove(str(i)))
        x= z3.IntVector('x',36)
        s2 = z3.Solver()
        for i in range(36):
            s2.add(x[i]==int(newRow[i]))
        
        sample1 = [int(k) for k in newRow]
        out = modelKeras.predict([sample1])

        y_pred = result(x)
        s2.add(y_pred[0]>y_pred[1])
        if out[0][0]<out[0][1] and s2.check()==z3.unsat:
            print("Exception exists in: ",toSend,";",step)
            print("result returned by DNN: ",out)
            return -1
        s.add(z3.Or( myArray[0] != s.model()[myArray[0]], myArray[1] != s.model()[myArray[1]],
                    myArray[2] != s.model()[myArray[2]], myArray[3] != s.model()[myArray[3]],
                    myArray[4] != s.model()[myArray[4]], myArray[5] != s.model()[myArray[5]],
                    myArray[6] != s.model()[myArray[6]], myArray[7] != s.model()[myArray[7]],
                    myArray[8] != s.model()[myArray[8]], move!= s.model()[move]))
    return 0

def ques3():
    print("\n\nWorking for first query using z3:")
    t1 = time.time()
    q1 = query1()
    t2 = time.time()
    if q1==0:
        print("No such example exists for the first query.")
    print("Time taken by query 1 in Z3 was: ", t2-t1, " seconds")

def ques4():
    print("\n\nWorking for second query using z3:")
    t1 = time.time()
    q2 = query2()
    t2 = time.time()
    if q2==0:
        print("No such example exists for the second query.")
    print("Time taken by query 2 in Z3 was: ", t2-t1, " seconds")

ques3()
ques4()