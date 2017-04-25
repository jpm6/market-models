import numpy as np
import pandas as pd

def crossValidation(filename):
    df=pd.read_csv(filename)
    df=df.drop([".Name", ".Symbol"], axis=1)     ##Deleting .Name and .Symbol
    
    ##Lables
    lables = np.asarray(df.columns)
    data = np.asmatrix(df)
    
    ##70-30 split, 70% train data and 30% rain data
    np.random.shuffle(data)
    row, column = np.array(data).shape
    training_set_size = int(row*0.70)
    train_data = data[:training_set_size]
    test_data = data[training_set_size:]
    
    return lables, train_data, test_data

if __name__ == '__main__':
    lables, train_data, test_data = crossValidation("binary-04-19-2017.csv")
    
    ##We dont have to save the files. 
    ##Save the csv file for lables, test data and train data
    np.savetxt("test_data_lables.csv", lables, fmt="%s", delimiter=",")
    np.savetxt("train_data_lables.csv", test_data, fmt="%s", delimiter=",")
    np.savetxt("train_data.csv", train_data, fmt="%s", delimiter=",")
    np.savetxt("test_data.csv", test_data, fmt="%s", delimiter=",")    

