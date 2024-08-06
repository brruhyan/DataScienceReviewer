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
