# ----- importing basics -----

# importing text files
with open('filename_smth.txt', 'r') as file:
  print(file.read())

# importing flat files using numpy (arrays)
filename = 'filename_here.txt'
data = np.loadtxt(filename, delimiter = ',') #skiprows = 1, #usecols = [0,2]

# importing flat files using pandas
df = pd.read_csv('filename.csv')
data_array = df.to_numpy #(converting to numpy array)

# importing with pandas with custom params
df = pd.read_csv('filename.csv', sep = '\t', comment = '#', na_values = ['NaN'])

# ----- importing different file types (EXCEL) -----

# pickled files
import pickle 
with open('pickled_file.pkl', 'rb') as file: #read-only binary
  data = pickle.load(file)
print(data)

# excel sheets
file = 'excel_filename.xlsx'
data = pd.ExcelFile(file)
print(data.sheet_names)

# parcing a sheet into a dataframe
df = xls.parse('sheet_filename')

# ----- importing different file types (SAS/STATA) -----

# importing SAS files
import pandas as pd
from sas7bdat import SAS7BDAT
with SAS7BDAT('filename_here.sas7bdat') as file:
  df_sas = file.to_data_frame()

# importing STATA files
data = pd.read_stata('filename_here.dta')

# importing HDF5 files 
import h5py
filename = 'filename_here.hdf5'
data = h5py.File(filename, 'r')

# exploring the HDF5 file
for key in data.keys():
  print(key)

# importing MATLAB files
import scipy.io
filename = 'filename_here.mat'
mat = scipy.io.loadmat(filename)

# ----- relational databases in Python -----

# creating a database engine (SQLAlchemy)
from sqlalchemy import create_engine
engine = create_engine('sqlite:///Student_data.sqlite')

# explore the values in the database
table_names = engine.table_names()
print(table_names)

# querying the database in python
from sqlalchemy import create_engine
import pandas as pd
engine = create_engine('sqlite:///Student_data.sqlite')
con = engine.connect()
# executing the actual query
rs = con.execute('SELECT * FROM Courses')
df = pd.DataFrame(rs.fetchall()) # storing it in a dataframe
df.columns = rs.keys()
con.close()

# querying but with a context manager
with engine.connect() as con:
  rs = con.execute('SELECT StudentID, AverageGrade, CourseName FROM Students')
  df = pd.Dataframe(rs.fetchmany(size = 5))
  df.columns = rs.keys()

# querying in one line using pandas
engine = create_engine('sqlite:///Student_data.sqlite')
df = pd.read_sql_query('SELECT * FROM Students', engine)

# ----- advanced relational database -----

# inner joining with pandas
engine = create_engine('sqlite:///Order_data.sqlite')
df = pd.read_sql_query('SELECT OrderID, CompanyName FROM Orders
                       INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID', engine)


# -- END 
    
                       
