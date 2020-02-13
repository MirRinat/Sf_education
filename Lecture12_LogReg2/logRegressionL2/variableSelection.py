import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import openpyxl

from logRegression.logRegressionL2.helperFiles.WOE import data_vars

dropColsHC = [
'funded_amnt',
'funded_amnt_inv',
'installment',
'total_pymnt',
'out_prncp_inv',
'total_pymnt_inv',
'total_rec_prncp',
'total_rec_int',
'last_pymnt_amnt',
'collection_recovery_fee',
'total_acc',
]

df = pd.read_csv("Data/150K.csv",skipinitialspace=True)

#df.corr().to_excel('CorrelationMatrix.xlsx')
df.drop(dropColsHC,axis=1,inplace=True)
sb.heatmap(df.corr(),cmap="Blues")
#plt.show()

final_iv, IV = data_vars(df, df.default_ind)
IV.to_excel('IVOutput.xlsx')