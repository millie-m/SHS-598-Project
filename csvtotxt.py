# -*- coding: utf-8 -*-
"""
@author: mmrun
"""

import pandas as pd
import io
import os
df=pd.read_csv('test_data.csv')

#df = pd.read_csv(io.StringIO(temp), sep="|", header=None)
#for coloumn in df.values:
 #   coloumn[:,4].tofile(str(coloumn[0])+'.txt', sep="\t", format="%s")
print(df.iloc[:,1])
nrows=df.shape[0]
for i in range(nrows):
    varpathname=df.iloc[i,1]
    #print(i,":",varpathname)
    filename = os.path.basename(varpathname)
    actualname=os.path.splitext(filename)[0]
    #print(actualname)
    #df.iloc[i,3].to_csv(actualname +'.txt', sep="\t", format="%s")
    #df_object.to_csv('xgboost.txt', sep='\t', index=False)
    with open(actualname +".txt", "w") as file:      
        file.write(df.iloc[i,3] + "\n")