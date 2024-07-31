# Classification models

# k-Nearest Neighbors (first step)
from sklearn.neighbors import KNeighborsClassifier
x = df[['total_day_income', 'total_night_income']].values
y = df['churn'].values
# second step
knn = KNeighborsClassifier(n_neighbords = 15)
