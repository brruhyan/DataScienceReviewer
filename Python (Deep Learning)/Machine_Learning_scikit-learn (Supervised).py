# Classification models

# k-Nearest Neighbors (first step)
from sklearn.neighbors import KNeighborsClassifier
x = df[['total_day_income', 'total_night_income']].values
y = df['churn'].values
# second step (fitting the model)
knn = KNeighborsClassifier(n_neighbords = 15)
knn.fit(x,y)
# third step (predicting on new data)
predictions = knn.predict(x_new)
print('Predictions: {}'.format(predictions))

# measuring model performance (classification)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3,
                                                    random_state = 21, stratify = y)
knn = KNeighborsClassifier(n_neighbords = 15)
knn.fit(x,y)
print(knn.score(X_test, y_test))

#model complexity curve (finding which k parameter is best for learning)
train_accuracies = {}
test_accuracies = {}
neighbors = np.arange(1,26)
#looping through the array
for neighbor in neighbors:
  knn = KNeighborsClassifier(n_neighbors = neighbor)
  knn.fit(X_train, y_train)
  train_accuracies[neighbor] = knn.score(X_train, y_train)
  test_accuracies[neighbor] = knn.score(X_test, y_test)
#plotting the results
plt.figure(figsize = (8,6))
plt.title('KNN Complexity')
plt.plot(neighbors, train_accuracies.values(), label = 'Training Accuracy')
plt.plot(neighbors, test_accuracies.values(), label = 'Testing Accuracy')
plt.legend()
plt.xlabel("Varying Number of Neighbors")
plt.ylabel("Accuracy")
plt.show()

#-------------------------------------

# Regression Models (Target must be either 0 or 1)
X = diabetesDf.drop('glucose', axis = 1).values #drops glucose and stores everything else as x
y = diabetes['glucose'].values #target column

# making predictions on a single feature
X_specific_column = X[:,3] #in this case this index is equal to bmi
X_specific_column = X_specific_column.reshape(-1,1)
#fitting the model
from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(X_specific_column, y)
predictions = reg.predict(X_specific_column)
plt.scatter(X_specific_column, predictions)
plt.show()

# Linear Regression with all features
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.3,
                                                    random_state = 42)
regression = LinearRegression()
regression.fit(x_train, y_train)
y_pred = regression.predict(x_test)

#-------------------------------------

# Evaluation of model performance
# r-squared (high value indicates that the variance is correlated to the independent value)
regression.score(x_test, y_test)

# mean squared error
from sklearn.metrics import mean_squared_error
mean_squared_error(y_test, y_pred, squared = False)
print("R^2: {}".format(regression))
print("RMSE: {}".format(mean_squared_error))

#-------------------------------------

# Cross Validation
