import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#creating a scatter plot
sns.scatterplot(x = metric_a, y = metric_b)
plt.show()

#creating a countplot
sns.countplot(y = metric)
plt.show()

#creating a plot with a dataframe
df = pd.read_csv('df.csv')
sns.countplot(x = 'metric', data = df)
plt.show()

#scatterplot with a dataframe
#Hue basically differentiates the plot by color
sns.scatterplot(x = 'metric_a', y = 'metric_b', data = df, hue = 'metric_hue') 

#creating a countplot with a customized color scheme
palettes = {'MetricA' : 'blue' , 'MetricB' : 'green'}
sns.countplot(x = 'metric_a', y = 'metric_b', data = df, palette = palettes, hue = 'metric_hue')
plt.show() 

#using relplots instead of the conventional syntax
#this is better than the conventional since we can create multiple plots at once using the col or row function
sns.relplot(x = 'metric_a', y = 'metric_b', kind = 'scatter', data = df)
plt.show()

#creating a subplot based on a certain group of metric
#in the context of student data, x could denote their average grade, while y could denote the grade level.
#col could then denote their average study time, this creates a different scatter plots based on the ave study time metric
sns.relplot(x = 'metric_a', y = 'metric_b', kind = 'scatter', data = df, col = 'metric')
plt.show() 

        
