# intitial exploration

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

# ----------grouping data for aggregation------------------------

# grouping data by categories in pandas
student_group = student_data.groupby(by = ['Course'].mean())

# grouping data and specifiying the columns to aggregate
student_group = student_data.groupby(by = ['Course'])['Age', 'ave_grade'].sum()

# grouping by multiple columns 
student_group = student_data.groupby(by = ['Course', 'Sex'])['average_grade].mean()

# ---------manipulating categories---------------------------

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

# rename categories
replace_map = {'CS' : 'Comp Sci'}
student['course'] = student['course'].cat.rename_categories('CS' : 'Computer Science')
student['course'] = student['course'].cat.replace(replace_map)

# reordering categories
student['year_level'] = student['year_level'].cat_reorder_categories(
  new_categories = ['1st', '2nd', '3rd', '4th', '5th'], 
  ordered = True)

# printing out categories
print(student['course'].cat.categories
      
# ---------cleaning and accessing data-------------------------

# removing spaces from data
student['course'] = student['course'].str.strip()

# capitalization
student['Name'] = student['Name'].str.title()

# accessing data with specific strings
student['Name'].str.contains('Bry', regex = False)
# accessing with a loc
student.loc[student['Course'] == 'CpE', 'Irregular'].value_counts(sort = False)

# ---------visualization with categorical data-------------------------

# box plot
sns.catplot(
  x = 'Course', y = 'average_grade,
  data = student_data, kind = 'box)

#bar charts
sns.catplot(x = 'Course', y = 'average_grade,
            data = student_data, kind = 'bar')
#pair plot
sns.catplot(x = 'Course', y = 'average_grade', data = student_data,
            hue = 'Irregular', dodge = True, kind = 'point')

# multiple categories using catplots (facetgrid)
# separates irregular students and non-irreg students and then plots the number of students in each course (irreg or not)
sns.catplot(x = 'Irregular', kind = 'count',
            col = 'Course', col_wrap = 2, 
            palette = sns.color_palette('Set1', data = student_data))

#customizing your plots
ax.fig.suptitle('insert string here')
ax.set_axis_labels('insert string here')
plt.subplots_adjust(top = .9)     
sns.set(font_scale = 1.4)
sns.set_style("whitegrid")

# ---------encoding---------------------------------------

# one hot encoding basics
student_data = pd.get_dummies(student_data['Course'])

#specific data
student_data_onehot = pd.get_dummies(student_data, columns = ['Course'], prefix = "")
                              
# label encoding (assigns a number to the course based on alphabetical order)
student_data['course_id'] = student_data['course'].cat.codes

# creating a code map (for large datasets)
codes = student_data['course'].cat.codes
categories = student_data['course']
name_map = dict(zip(codes, categories))

# boolean coding (if yes = 1, no = 0)
student_data['Irregular'] = np.where(
  student_data['Irregular'].str.contains('Yes', regex = False), 1,0)

# updating NaN values
student.loc[student['student_type'].isna(), 'student_type'] = 'dropped'

# ----end--

                
