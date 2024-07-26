#importing dataset with time
graduation_data = pd.read_csv('graduation.csv', parse_dates=['date'], index_col = 'date')

#extracting the year from a date column
graduation_data['graduation_year'] = graduation_data['graduation_date'].dt.year
graduation_data["graduation_month"] = graduation_data["graduation_date"].dt.month

#plotting time series data
fig, ax = plt.subplots()
ax.plot(graduation_data.index, graduation_data['average_grade'])
#plotting specific times 
eigthies = graduation_data['1980-01-01', '1989-12-31']
ax.plot(eighties.index, eighties['average_grade'])
#setting x and y label
ax.set_xlabel, ax.set_ylabel('Label')

#making a plot where both plots share the same x-axis
fig, ax = plt.subplot()
ax.plot(graduation_data.index, graduation_data['average_grade'], color = 'red')
ax.set_ylabel('Insert String Here', color = 'red')
ax.tick_params('y', colors = 'red')

ax2 = ax.twinx()
ax2.plot(eighties.index, eighties['average_grade'], color = 'blue')
ax2.set_ylabel('Insert String Here', color = 'blue')
ax2.tick_params('y', colors = 'blue')
plt.show()

#function that plots time series by color
def plot_timeseries(axes, x, y, color, xlabel, ylabel):
        axes.plot(x,y color = color)
        axes.set_xlabel(xlabel)
        axes.set_ylabel(ylabel, color = color)
        axes.tick_params('y', colors = color)
        
#how to use the function
plot_timeseries(ax2, graduation_data.index, graduation_data['average_grade],
                red, "Insert Label 1", 'Insert Label 2")

#annotating your plots
ax.annotate("Insert String", xy = (pd.Timestamp('specific time'), 95)) #annotates the graduation_year that exceeded 95% passing.       
