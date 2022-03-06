# ticTacToeInZ3

Part 1:
1. generateData.py generates the list of all valid moves and labels them as good or bad move depending on the conditions.
2. Run python3 generateData.py>>output.txt to generate and store all possible valid moves with their labels.
3. Run python3 createCSV.py. This will create and store the csv file for training the DNN.

Part 2:
1. Run python3 classifier.py to train a DNN. This will train and store the DNN in two formats. First is a .h5 file and second is folder containing .pb file and other details.

Part 3 & 4:
1. Run python3 verifyZ3.py. This will run the verification for both query 1 and 2 mentioned in question 3 and 4 respectively.
2. Both the query outputs will be for verification using Z3.
3. Run python3 verifyMarabou.py. This will run the verification for both query 1 and 2 mentioned in question 3 and 4 respectively.
2. Both the query outputs will be for verification using Marabou.