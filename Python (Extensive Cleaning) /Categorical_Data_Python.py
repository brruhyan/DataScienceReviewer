# initial exploration of categorical data

print(student_data['average_grade'].describe())
print(student_data['average_grade'].value_counts()) #frequency table
print(student_data['average_grade'].value_counts(normalize = True)) #relative frequency

# setting an object dtype to categorical (categorical saves data)

student_data['Course'] = student_data['Course'].astype('category')

# creating a categorical series

my_categories = ['CpE', 'CE', 'ME' 'ENSE']
new_category = pd.Series(my_categories, dtype = 'category')

# creating a categorical series with order
my_categories = ['CpE', 'CE', 'ME' 'ENSE']
new_category = pd.Categorical(my_categories, categories = ['ENSE', 'CpE', 'CE', 'ME'], ordered = True)

# specifiying dtypes when reading data
student_dtypes = {'Course' : 'category'}
student = pd.read_csv('student_data.csv', dtype = student_dtypes)

# ------------------------------------

#grouping data by categories in pandas
