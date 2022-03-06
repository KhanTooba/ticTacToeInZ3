from Marabou.maraboupy import Marabou

def convert(c):
    c=str(c)
    if "1" in c:
        return "010"
    elif "0" in c:
        return "100"
    elif "2" in c:
        return "001" 
    return "" 

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

def giveData():
    f = open("UnformattedData.csv","r")
    c=1
    rows=[]
    b=0
    for row in f:
        if c!=1:
            arr = (str(row).replace(" ","").replace("\n","")).split(",")
            arr2 = [int(k) for k in arr]
            # print(arr2)
            if arr2[10]==0:
                rows.append(arr2)
                b=b+1
        c=c+1
    return rows, b, c

def goodBad(arr):
    if (arr[0]==1 and arr[1]==1 and arr[2]==0 and arr[9]==2) or (
        arr[0]==1 and arr[1]==0 and arr[2]==1 and arr[9]==1)or (
        arr[0]==0 and arr[1]==1 and arr[2]==1 and arr[9]==0):
        return 1 #This is a winning move
    if (arr[3]==1 and arr[4]==1 and arr[5]==0 and arr[9]==5) or (
        arr[3]==1 and arr[4]==0 and arr[5]==1 and arr[9]==4)or (
        arr[3]==0 and arr[4]==1 and arr[5]==1 and arr[9]==3):
        return 1 #This is a winning move
    if (arr[6]==1 and arr[7]==1 and arr[8]==0 and arr[9]==8) or (
        arr[6]==1 and arr[7]==0 and arr[8]==1 and arr[9]==7)or (
        arr[6]==0 and arr[7]==1 and arr[8]==1 and arr[9]==6):
        return 1 #This is a winning move
    if (arr[0]==1 and arr[3]==1 and arr[6]==0 and arr[9]==6) or (
        arr[0]==1 and arr[3]==0 and arr[6]==1 and arr[9]==3)or (
        arr[0]==0 and arr[3]==1 and arr[6]==1 and arr[9]==0):
        return 1 #This is a winning move
    if (arr[1]==1 and arr[4]==1 and arr[7]==0 and arr[9]==7) or (
        arr[1]==1 and arr[4]==0 and arr[7]==1 and arr[9]==4)or (
        arr[1]==0 and arr[4]==1 and arr[7]==1 and arr[9]==1):
        return 1 #This is a winning move
    if (arr[2]==1 and arr[5]==1 and arr[8]==0 and arr[9]==8) or (
        arr[2]==1 and arr[5]==0 and arr[8]==1 and arr[9]==5)or (
        arr[2]==0 and arr[5]==1 and arr[8]==1 and arr[9]==2):
        return 1 #This is a winning move
    if (arr[0]==1 and arr[4]==1 and arr[8]==0 and arr[9]==8) or (
        arr[0]==1 and arr[4]==0 and arr[8]==1 and arr[9]==4)or (
        arr[0]==0 and arr[4]==1 and arr[8]==1 and arr[9]==0):
        return 1 #This is a winning move
    if (arr[6]==1 and arr[4]==1 and arr[2]==0 and arr[9]==2) or (
        arr[6]==1 and arr[4]==0 and arr[2]==1 and arr[9]==4)or (
        arr[6]==0 and arr[4]==1 and arr[2]==1 and arr[9]==6):
        return 1 #This is a winning move
    
    
    if (arr[0]==2 and arr[1]==2 and arr[2]==0 and arr[9]!=2) or (
        arr[0]==2 and arr[1]==0 and arr[2]==2 and arr[9]!=1)or (
        arr[0]==0 and arr[1]==2 and arr[2]==2 and arr[9]!=0):
        return 0 #This is a case 2 bad move
    if (arr[3]==2 and arr[4]==2 and arr[5]==0 and arr[9]!=5) or (
        arr[3]==2 and arr[4]==0 and arr[5]==2 and arr[9]!=4)or (
        arr[3]==0 and arr[4]==2 and arr[5]==2 and arr[9]!=3):
        return 0 #This is a case 2 bad move
    if (arr[6]==2 and arr[7]==2 and arr[8]==0 and arr[9]!=8) or (
        arr[6]==2 and arr[7]==0 and arr[8]==2 and arr[9]!=7)or (
        arr[6]==0 and arr[7]==2 and arr[8]==2 and arr[9]!=6):
        return 0 #This is a case 2 bad move
    if (arr[0]==2 and arr[3]==2 and arr[6]==0 and arr[9]!=6) or (
        arr[0]==2 and arr[3]==0 and arr[6]==2 and arr[9]!=3)or (
        arr[0]==0 and arr[3]==2 and arr[6]==2 and arr[9]!=0):
        return 0 #This is a case 2 bad move
    if (arr[1]==2 and arr[4]==2 and arr[7]==0 and arr[9]!=7) or (
        arr[1]==2 and arr[4]==0 and arr[7]==2 and arr[9]!=4)or (
        arr[1]==0 and arr[4]==2 and arr[7]==2 and arr[9]!=1):
        return 0 #This is a case 2 bad move
    if (arr[2]==2 and arr[5]==2 and arr[8]==0 and arr[9]!=8) or (
        arr[2]==2 and arr[5]==0 and arr[8]==2 and arr[9]!=5)or (
        arr[2]==0 and arr[5]==2 and arr[8]==2 and arr[9]!=2):
        return 0 #This is a case 2 bad move
    if (arr[0]==2 and arr[4]==2 and arr[8]==0 and arr[9]!=8) or (
        arr[0]==2 and arr[4]==0 and arr[8]==2 and arr[9]!=4)or (
        arr[0]==0 and arr[4]==2 and arr[8]==2 and arr[9]!=0):
        return 0 #This is a case 2 bad move
    if (arr[6]==2 and arr[4]==2 and arr[2]==0 and arr[9]!=2) or (
        arr[6]==2 and arr[4]==0 and arr[2]==2 and arr[9]!=4)or (
        arr[6]==0 and arr[4]==2 and arr[2]==2 and arr[9]!=6):
        return 0 #This is a case 2 bad move
    return 1

def putConstraints(rows):
    ConstrainedRows = []
    for row in rows:
        if goodBad(row)==0:
            ConstrainedRows.append(row)
    return ConstrainedRows

def modify(data, step, output):
    x=[]
    for i in range(9):
        value = convert(str(data[i]))
        x.append(value[0])
        x.append(value[1])
        x.append(value[2])
    move = convertMove(str(step))
    for i in move:
        x.append(i)
    x.append(str(output))
    return x

def MarabouResult(data, move, y_true):
    filename = "/home/tooba/Documents/ticTacToeInZ3/classifier/saved_model.pb"
    x = modify(data,move,y_true)
    network = Marabou.read_tf(filename)
    # inputNames = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14",
    #                 "15","16","17","18","19","20","21","22","23","24","25","26","27",
    #                 "28","29","30","31","32","33","34","35","36"]
    # outputName = "output"
    # network = Marabou.read_tf(filename = filename, inputNames = inputNames, outputName = outputName)
    # c=0
    inputVars = network.inputVars[0][0]
    outputVars = network.outputVars[0]
    for i in range(36):
        network.setLowerBound(inputVars[i],int(x[i]))
        network.setUpperBound(inputVars[i],int(x[i]))
    
    network.setLowerBound(outputVars[1], 0)
    network.setUpperBound(outputVars[1], 1)
    network.setLowerBound(outputVars[0], 0)
    network.setUpperBound(outputVars[0], 1)

    eq1 = Marabou.MarabouCore.Equation(Marabou.MarabouCore.Equation.GE)
    eq1.addAddend(outputVars[0],outputVars[1])
    network.addEquation(eq1)

    vals, stats = network.solve("marabou.log")
    print(vals)
    print(stats)
    return 0

def filterOut(data):
    rows = []
    for d in data:
        if d[4]==1:
            if d[0]==1 or d[2]==1 or d[6]==1 or d[8]==1:
                rows.append(d)
    return rows

def query1(rows):
    for r in rows:
        move = r[9]
        y_true = r[10]
        x = r[0:9]
        y_predict = MarabouResult(x, move, y_true)
        # Now, encode the following constraints in Marabou:
        # Result of the DNN is good but Such a move is bad and the result is hence wrong
        print(x,"->",move,"->",y_true,"->",y_predict)    

def query2(data):
    for r in rows:
        move = r[9]
        y_true = r[10]
        x = r[0:9]
        y_predict = MarabouResult(x, move, y_true)
        # Now, encode the following constraints in Marabou:
        # Result of the DNN is good but Such a move is bad and the result is hence wrong
        print(x,"->",move,"->",y_true,"->",y_predict)    

rows, b, c = giveData()
constrainedRows = putConstraints(rows)
query1(constrainedRows)

rowsForQuery2 = filterOut(constrainedRows)
query2(rowsForQuery2)