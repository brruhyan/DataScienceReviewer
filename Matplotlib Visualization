#importing dataset with time
graduation_data = pd.read_csv('graduation.csv', parse_dates=['date'], index_col = 'date')

#extracting the year from a date column
graduation_data['graduation_year'] = graduation_data['graduation_date'].dt.year
graduation_data["graduation_month"] = graduation_data["graduation_date"].dt.month

#plotting time series data
ax.plot(graduation_data.index, graduation_data['average_grade'])
#plotting specific times 
eigthies = graduation_data['1980-01-01', '1989-12-31']
ax.plot(eighties.index, eighties['average_grade'])
        
