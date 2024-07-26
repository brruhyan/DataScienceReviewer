#This part covers the basics of aggregating summary statistics in a dataframe
import pandas as pd
import numpy as np
pd.read_csv('salesDf.csv')

#Aggregating the mean and median of a dataframe
salesDf['column_name'].mean()
salesDf['column_name'].median()

#Selecting the min and max of a specific column
salesDf['column_name'].min()
salesDf['column_name'].max()

#Getting the cumulative sum of a dataframe and saving it as a new column
salesDf['new_column'] = salesDf['column_name'].cumsum()
salesDf['new_column'] = salesDf['column_name'].cummax()

#Dropping duplicates in a dataframe
new_df = salesDf.drop_duplicates(subset = ['column_name1', 'column_name2'])
#Subsetting a row and then dropping duplicates in that row
new_df = salesDf[salesDf['grouped_column']].drop_duplicates(subset = 'column_name')

#Counting the number of values in a column
df_count = salesDf['column_name'].value_counts()
df_count = salesDf['column_name'].value_counts(normalize = True, sort = True) #gets the proportion and sorts

#Subsetting a certain row and getting its metrics
df_metricA = salesDf[salesDf['group'] == 'A']['column_name'].sum()
#Calculating a certain colummns metric 
df_metricGroups = salesDf.groupby('group')['column_name'].sum()
#Calculating the total sum sales of all groups by the days where it is a holiday
df_metricGroupSpecific = salesDf.groupby(['group', 'certain_day'])['column_name'].sum() 

#multiple summary statistics in one line of code
df_sales = salesDf.groupby('group')['column_name'].agg([np.min, np.max])
df_sales = salesDf.groupby('group')[['column_name1', 'column_name2']].agg([np.min, np.max])

#Aggregating data in a table form
df_sales = salesDf.pivot_table(values = 'columnName_withNumericVals', index = 'group')
df_sales = salesDf.pivot_table(values = 'columnName_withNumericVals', index = 'group', 
                              aggfunc = [np.mean, np.median])     

