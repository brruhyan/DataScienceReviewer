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

# Cross Validation 
# cross validation is to avoid generalization on unseen data

from sklearn.model_selection import cross_val_score, KFold
kf = KFold(n_splits = 6, shuffle = True, random_state = 62)
reg = LinearRegression()
cross_val = cross_val_score(reg, X,y, cv = kf)
print(cross_val)
print(np.mean(cross_val), np.std(cross_val)) 
print(np.quantile(cross_val), [0.025, 0.975) # confidence interval

#-------------------------------------

# Regularzation
# Ridge regression (the performance of the model gets worse as alpha  increases)
from sklearn.linear_model import Ridge
scores = []
for alpha in [0.1, 1.0, 10.0, 100.0, 1000.0]:
  ridge = Ridge(alpha = alpha)
  ridge.fit(X_train, y_train)
  y_predict = ridge.predict(X_test)
  scores.append(ridge.score(X_test, y_test))
print(scores)

# Lasso regression
# THIS IS USED TO SELECT THE IMPORTANT FEATURES OF A DATASET (shrinks the coefficient of less imporatnt features to 0)
# The performance of the model decreases as the alpha exceeds 20
from sklearn.linear_model import Lasso
scores = []
for alpha in [0.1, 1.0, 10.0, 100.0, 1000.0]:
  lasso = Lasso(alpha = alpha)
  lasso.fit(X_train, y_train)
  lasso_predict = ridge.predict(X_test)
  scores.append(lasso.score(X_test, y_test))
print(scores)

#-------------------------------------

# Feature Selection with Lasso
from sklearn.linear_model import Lasso
X = diabetes_df.drop("glucose", axis = 1).values
y = diabetes_df['glucose'].values
names = diabetes_df.drop("glucose", axis = 1).columns
lasso = Lasso(alpha = 0.1)
lasso_coef = lasso.fit(X,y).coef_
#plotting the coefficient for each feature
plt.bar(names, lasso_coef)
plt.xticks(rotation = 45) #the higher the coefficient the more important it is
plt.show()
