# ----- Basic data problems -----

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

# ----- duplicate data problems -----

# finding the duplicate values
column_names = ['first_name', 'last_name', 'address']
duplicated = student_graduation.duplicated(subset = column_names, keep = False)
student_graduation[duplicated].sort_values(by = 'first_name')

# dropping the duplicates
student_graduation.drop_duplicates(inplace = True)

# ----- text and categorical data problems (value membership constraints)-----

# categorical problems
categories['student_course'] = categories['student_course'] = ['CE' , 'CpE' 'ME']

# finding incosistent categories (finds the courses that are in student_graduation that are not in the categories table)
inconsistent = set(student_graduation['student_course']).difference(categories['student_course']) 
print(inconsistent)
inconsistent_rows = student_graduation['student_course'].isin(inconsistent)
student_graduation[inconsistent_rows]

# dropping the inconsistent categories
consistent_data = student_graduation[~inconsistent_rows]

# ----- value inconsistency-----
