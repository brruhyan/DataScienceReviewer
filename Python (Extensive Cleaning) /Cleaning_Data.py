# ---------- Basic data problems ----------

# converting strings to integers (in the case that revenue has a currency sign)
sales['Revenue'] = sales['Revenue'].str.strip('₱')
sales['Revenue'] = sales['Revenue'].astype('int')
assert sales['Revenue'].dtype == 'int'

# numerical and categorical data (1 = CpE, 0 = CE, but its in integers)
df['student_course'] = df['student_course'].astype('category')

# data range constraints (this makes sure that the graduation date that is not in the future is omitted)
import datetime as dt
today_date = dt.date.today()
student_graduation[student_graduation['graduation_date'] < dt.date.today()] # upcoming graduation date cannot be in the past

# dropping data (drops those date that has an upcoming graduation date in the past)
student_graduation.drop(student_graduation[student_graduation['graduation_date'] < dt.date.today()].index, inplace = True)

# converting wrong date time to the correct time
student_graduation.loc[student_graduation['graduation_date'] < dt.date.today(), 'graduation_date'] = dt.date.today() 

# converting a date object type to a an actual date data type
student_graduation['graduation_date'] = pd.to_datetime(student_graduation['graduation_date']).dt.date

# ---------- duplicate data problems ----------

# finding the duplicate values
column_names = ['first_name', 'last_name', 'address']
duplicated = student_graduation.duplicated(subset = column_names, keep = False)
student_graduation[duplicated].sort_values(by = 'first_name')

# dropping the duplicates
student_graduation.drop_duplicates(inplace = True)

# ----- text and categorical data problems (value membership constraints) -----

# categorical problems
categories['student_course'] = categories['student_course'] = ['CE' , 'CpE' 'ME']

# finding incosistent categories (finds the courses that are in student_graduation that are not in the categories table)
inconsistent = set(student_graduation['student_course']).difference(categories['student_course']) 
print(inconsistent)
inconsistent_rows = student_graduation['student_course'].isin(inconsistent)
student_graduation[inconsistent_rows]

# dropping the inconsistent categories
consistent_data = student_graduation[~inconsistent_rows]

# ---------- value inconsistency ----------

# same categories but with different spelling and capitalization
student_graduation['student_course'] = student_graduation['student_course'].str.upper()
student_graduation['student_course'] = student_graduation['student_course'].str.lower()

# same category but with varying spaces
student_courses = student_graduation['student_course'].str.strip()

# collapsing data into categories 
# from average_grade we can collapse it into High, Average, and Low
import pandas as pd
ranges = [75, 85, 95]
group_names = ['High', 'Average', 'Low'] 
# create the student performance column
student_graduation['student_performance'] = pd.cut(student_graduation['average_grade'], bins = ranges,
                                                   labels = group_names)

# consolidating data into one category
# CpE, IS to one category named tech-related course
mapping = {'CpE' : 'Tech-related', 'IS' : 'Tech-related', 
           'CE' : 'Civil-related', 'Arki' : 'Civil-related'}
course_category['student_course'] = course_category['student_course'].replace(mapping)
course_category['student_course'].unique()

# cleaning text data and standardizing data
student_data['phone_number'] = student_data['phone_number'].str.replace("+", "00")
student_data['phone_number'] = student_data['phone_number'].str.replace("-", "")
# replacing invalid numbers to NaN
digits = student_data['phone_number'].str.len()
student_data.loc[digits < 10, 'phone_number'] = np.nan
# cleaning symbols
student_data['phone_number'].str.replace(r'\D+', '')

# ---------- advanced data problems ----------

# uniformity (identifying outliers and converting them accordingly)
temp_fah = temperatures.loc[temperatures['Temperature'] > 40, 'Temperature']
temp_cels = (temp_fah - 32) * (5/9)
temperatures.loc[temperatures['Temperatute'] > 40, 'Temperature'] = temp_cels

# datetime uniformity 
student_data['Birthday'] = pd.to_datetime(student_data['Birthday'],
                                          infer_datetime_format = True,
                                          errors = 'coerce')

# changing the datetime format
student_data['Birthdays'] = student_data['Birthdays'].dt.strftime('%d-%m-%Y')

# cross field validation (checks value integrity)
summary_courses = student_courses[['CpE', 'CE', 'ME']].sum(axis = 1)
# the total number of students per course must equal to the total column
student_total = summary_courses == student_data['total_students'] 

# cross field validation example (looking at the birthday to see if it equals to their age)
student_data['Birthday'] = pd.to_datetime(student_data['Birthday'])
today = dt.date.today()
age_calc = today.year - student_data['Birthday'].dt.year
age_equals = age_calc == student_data['Age']
# filtering ages that are not equal
inconsistent_age = student_data[~age_equals]
consistent_age = student_data[age_equls
                                                                  
# ---------- visualizing and understanding missing data ----------

# visualization of missing data
import missingno as msno
import matplotlib.pyplot as plt
msno.matrix(student_data)
plt.show()

# isolating first and then visualizing
missing = student_data[student_data['average_grade'].isna()]
missing.describe()
# visualizing the isolated data
sorted_ave = student_data.sort_values(by = 'average_grade')
msno.matrix(sorted_ave)
plt.show()

# imputing without machine learning
student_grade_mean = student_data['average_grade'].mean()
student_imputed = student_data.fillna({'average_grade' : student_grade_mean})

# ---------- record linkage ----------
