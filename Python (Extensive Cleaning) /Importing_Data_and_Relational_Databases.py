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
