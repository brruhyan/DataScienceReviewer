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

# grouping data by categories in pandas
student_group = student_data.groupby(by = ['Course'].mean())

# grouping data and specifiying the columns to aggregate
student_group = student_data.groupby(by = ['Course'])['Age', 'ave_grade'].sum()

# grouping by multiple columns 
student_group = student_data.groupby(by = ['Course', 'Sex'])['average_grade].mean()

# ------------------------------------

# settings category values
student['course'] = student['course'].astype('category')
student['course'].value_counts(dropna = False)

# overwriting categories 
student['course'] = student['course'].cat.set_categories(
  new_categories = ['CpE', 'IE', 'ME' 'ENSE', 'IT'], ordered = True)

# adding new categories 
student['course'] = student['course'].cat.add_categories(
  new_categories = ['CS', 'IS'])

# removing categories
student['course'] = student['course'].cat.remove_categories(
  removals = ['CS', 'IS'])
