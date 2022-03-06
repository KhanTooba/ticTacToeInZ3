import csv 

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

data = []
c=0
f = open("output.txt", "r")
row = []
for line in f.readlines():
    row = []
    s1 = line.split(";")
    if len(s1)==1:
        break
    s2 = s1[0].replace("]","")
    s2 = s2.replace("[","")
    for element in s2.split(","):
        row.append(element)
    row.append(s1[1])
    if "good" in s1[2]:
        row.append(1)
    else:
        row.append(0)
    data.append(row)

header=["one","two","three","four","five","six","seven","eight","nine","move","GoodBad"]
formattedData = []
for row in data:
    newRow=[]
    input=""
    output=""
    count1 = 0
    for element in row:
        # print(element,end="")
        if count1==9:
            input = input + convertMove(element)
        elif count1==10:
            output = str(element)
        else:
            input = input + convert(element)
        count1=count1+1
    
    newRow = list(input)
    newRow.append(output)
    print(row)
    print(newRow)
    print()
    formattedData.append(newRow)

with open("UnformattedData.csv", 'w') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(header)
    csvwriter.writerows(data)

header2=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","output"]

with open("data.csv", 'w') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(header2)
    csvwriter.writerows(formattedData)
# print(formattedData)
