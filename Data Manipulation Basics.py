#This is a data analyst reviewer solely created for my review for the data scientist certification.
#This reviewer could also serve as a steppping stone for aspiring data analyst such as myself. 
#Feel free to share this with your peers!"""

#Sorting values by a specific column
df = df.sort_values('column_name')
#Sorting two columns at once, sorting column_name1 by ascending order and column_name2 by descending order
df = df.sort_values('column_name', ascending = False) 
df = df.sort_values(['column_name1, column_name2'], ascending = [True, False]) 
