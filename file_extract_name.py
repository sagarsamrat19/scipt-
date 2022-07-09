import pandas as pd
import xlrd

data = pd.read_excel("Maharashtra.xlsx")

speciesdata =data['ACTIVITY_DESCRIPTION']

for i in speciesdata:
	a = data[data['ACTIVITY_DESCRIPTION'].str.contains(i)]
	a.to_excel(i+".xlsx")
