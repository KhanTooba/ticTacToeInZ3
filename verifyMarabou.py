from maraboupy import Marabou
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

def MarabouResult(x, move, y_true, nnetFile, filename):
    inputNames = ['Placeholder']
    outputName = 'y_out'
    network = Marabou.read_tf(filename = filename, inputNames = inputNames, outputName = outputName)
    # c=0
    inputVars = network.inputVars[0][0]
    outputVars = network.outputVars[0]
    for j in range(9):
        value = convert(x[j])
        i = j*3
        network.setLowerBound(inputVars[i],int(value[0]))
        network.setUpperBound(inputVars[i],int(value[0]))
        network.setLowerBound(inputVars[i+1],int(value[1]))
        network.setUpperBound(inputVars[i+1],int(value[1]))
        network.setLowerBound(inputVars[i+2],int(value[2]))
        network.setUpperBound(inputVars[i+2],int(value[2]))
    
    network.setLowerBound(outputVars[1], 194.0)
    network.setUpperBound(outputVars[1], 210.0)
    # for var in network.inputVars[0]:
    #     # eq1: 1 * var = 0
    #     eq1 = MarabouCore.Equation(MarabouCore.Equation.EQ)
    #     eq1.addAddend(1, var)
    #     eq1.setScalar(x[c])
    #     c = c + 1
    #     net1.setLowerBound(var, 0)
    #     net1.setUpperBound(var, 1)
    
    return 0

def query1(rows):
    for r in rows:
        move = r[9]
        y_true = r[10]
        x = r[0:9]
        # y_predict = MarabouResult(x, move, y_true)
        # Now, encode the following constraints in Marabou:
        # The move should be second case of bad i.e when the second player is winning and first player played the wrong move
        # The move should not itself be a winning one in which case it will become a good move
        # Result of the DNN is good but Such a move is bad and the result is hence wrong


        print(x,"->",move,"->",y_true)    

rows, b, c = giveData()
constrainedRows = putConstraints(rows)
query1(constrainedRows)