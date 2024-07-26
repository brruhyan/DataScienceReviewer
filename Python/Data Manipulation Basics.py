#Sorting values by a specific column
df = df.sort_values('column_name')
#Sorting two columns at once, sorting column_name1 by ascending order and column_name2 by descending order
df = df.sort_values('column_name', ascending = False) 
df = df.sort_values(['column_name1, column_name2'], ascending = [True, False]) 

#Selecting a specific column in a dataframe
new_df = df[['column_name1', 'column_name2']]
#Subsetting based on metrics
new_df = df[df['column_name'] > 1000]
new_df = df[(df["column_name1"] < 1000) & (df["column_name2"] == "metric")]

#Creating new columns in a dataframe based on an operation
new_df['new_column'] = df['column_name1'] + df['column_name2']

#join data using pandas (inner join), the inner join returns values with those rows that have common characteristics. 
joined_df = dataframe1.merge(dataframe2, on = 'common_column', #this only works when both dataframes have common columns
                      suffixes = ('_df1' , 'df2'))       #the suffixes is there to determine which table the values came from

#three tables merging
joined_df = dataframe1.merge(dataframe2, on = 'common_column').merge(dataframe3, on = 'common_column') 
joined_df = dataframe1.merge(dataframe2, on = 'common_column').merge(dataframe3, on = 'common_column',
                                                                    suffixes = ('_df1', 'df2'))

#join using pandas (left join), left join returns all values of the left dataframe (dataframe1)
#all common columns found in the right (dataframe2) dataframe will be added to the left dataframe
joined_df = dataframe1.merge(dataframe2, on = 'common_column', how = 'left') 
