import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels as sm
import warnings
import sys
from sklearn import linear_model
from sklearn import datasets

warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")

class data_models():
    
    def __init__(self,data):
        self.data = data


    def linear_fit(self):
        
        try:
            df=self.data
            Lseq=[]
            for j in range(len(df.columns)):
                Lseq=Lseq+[j]
            X=np.array(Lseq)
            X=X.reshape(3,1)
            X=pd.DataFrame(X)
            Y=df[["SEDS_RETCB_IN_A"]]
            lm = linear_model.LinearRegression()
            model = lm.fit(X,Y)
            predictions = lm.predict(X) 
            self.result=(predictions)[1:3]
            return self.result
        
        except Exception as f:
            print("{} following error occured please look into the code again".format(f))
