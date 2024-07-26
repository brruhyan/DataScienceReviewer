#creating a histogram
sns.histplot(data = df, x = 'data', binwidth = 1)

#defining a series of data that are not part of a certain group
#in this context. printing the not_student will print out all values, except the student data
not_student = ~population_data['demographics'].isin(['Student'])
is_student = population_data['demographics'].sin(['Student'])

#addressing missing data
population_data.isna().sum()
population_data.fillna(0, inplace = True)
population_data['Column1'].fillna(population_data['Column1'].mean(), inplace=True)

#removing spaces from a string character
population_data['Telephone_Number'} = population_data['Telephone_Number'].str.replace(" ", "")
#converting the data type
population_data['Age'] = population_data['Age'].astype(int)

#visualizing multiple variable relationships
sns.pairplot(data = graduation_data, vars = ['graduation_date', 'average_grade'])

#visulizing multiple distributions in one plot
sns.kdeplot(data = graduation_data, x = 'graduation_data', hue = 'average_grade', cut = 0)

#cross tabulating 
pd.crosstab(graduation_data['graduate_date'], graduation_data['average_grade'])
pd.crosstab(graduation_data['Course_category'], graduation_data['graduation_date'], 
            values = graduation_data['average_grade'], aggfunc = 'mean')
