import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#creating a scatter plot
sns.scatterplot(x = metric_a, y = metric_b)

#creating a countplot
sns.countplot(y = metric)

#creating a plot with a dataframe
df = pd.read_csv('df.csv')
sns.countplot(x = 'metric', data = df)

#scatterplot with a dataframe
#Hue basically differentiates the plot by color
sns.scatterplot(x = 'metric_a', y = 'metric_b', data = df, hue = 'metric_hue') 

#creating a countplot with a customized color scheme
palettes = {'MetricA' : 'blue' , 'MetricB' : 'green'}
sns.countplot(x = 'metric_a', y = 'metric_b', data = df, palette = palettes, hue = 'metric_hue')

#using relplots instead of the conventional syntax
#this is better than the conventional since we can create multiple plots at once using the col or row function
sns.relplot(x = 'metric_a', y = 'metric_b', kind = 'scatter', data = df)

#creating a subplot based on a certain group of metric
#in the context of student data, x could denote their average grade, while y could denote the grade level.
#col could then denote their average study time, this creates a different scatter plots based on the ave study time metric
sns.relplot(x = 'metric_a', y = 'metric_b', kind = 'scatter', data = df, col = 'metric')

#customizing scatterplots
#do note that style has different functions, refer to the sns documentation
sns.relplot(x = 'metric_a', y = 'metric_b', data = df, size = 'cylinders', kind = 'scatter',
           style = 'origin', hue = 'metric_hue')

#creating lineplots, refer to the documentation for more parameters.
sns.relplot(x = 'metric_a', y = 'metric_b', data = df, kind = 'line', ci = 'sd' )

#creating categorical plots
#similar with relplot col could be removed
#in order to use the order parameter, first create a list of categories and pass it to the order parameter
sns.catplot(y = 'metric_a', data = df, kind = 'count', col = 'category')
sns.catplot(x = 'metric_a' ,y = 'metric_b', data = df, kind = 'bar', col = 'category', order = categories)   

#creating boxplots, the sym parameter omits outliers in the data
sns.catplot(x = 'metric_a', y = 'metric_b', data = df, sym = '', kind = 'box')

#creating point plots
sns.catplot(x = 'metric_a', y = 'metric_b' data = df, capsize = 0.2, kind = 'point', join = False)

#customizing your sns plots
sns.set_style('whitegrid') #this changes the background of the plot
sns.set_context('paper') #changes the scaling of the plot
sns.set_pallete('Blues') #changes the color of each plot, refer to the documentation for all palettes

#customizing your plots #2
g = sns.relplot(x = 'data1', y = 'data2', data = df, kind = 'scatter')
g.fig.suptitle('Insert string here') #since we are using a relplot, this adds an individual title to each generated plot
g.set_title('Insert string here') #this adds a title to the whole plot
g.set(xlabel = 'String here', ylabel = 'string here')

#customizing your plots #3
plt.xticks(rotation = 90) #rotates the plot labels
