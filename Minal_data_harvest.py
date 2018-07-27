# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 19:33:09 2018

@author: meenal
"""

import quandl
import pandas as pd
state=['SEDS_RETCB_IN_A','SEDS_RETCB_IA_A','SEDS_RETCB_HI_A']
source_org='EIA'
"""

load_data(): this needs to be called for loading the function. This function calls the get_data function.
             
"""

class data_harvest():
        """

        """
        def __init__(self):
            self.indiana_renewable_consume = 0
            self.data =0
            
            
        def get_data(self):
           
             try:
                  self.indiana_renewable_consume = quandl.get('EIA/SEDS_RETCB_IN_A',authtoken="EDCKwiyMXrBfB9cWzDM4")
                  self.data = 0
                  print("Done Loading the data.")
                  return self.indiana_renewable_consume

             except Exception as f:
                print("{} following error occured please look into the code again".format(f))
                print("{} following error occured please look into the code again".format(f))
                
                
                
        def load_data(self):
            """
            Loads the final data and the renaming of certain columns. And in the end joins all features.
            Thereby making all features into a single dataset.


            """
            self.data=pd.DataFrame()
            df=pd.DataFrame()
            try:
                for i in state:
                    df=quandl.get("{}/{}".format(source_org,i),start_date="2011-12-31",end_date="2013-12-31",api_key="EDCKwiyMXrBfB9cWzDM4")
                    self.data[i]=df["Value"]
                return self.data
                
            except Exception as f:
                print(f)
