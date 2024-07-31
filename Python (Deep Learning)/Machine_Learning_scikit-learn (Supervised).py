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

#model complexity curve 
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
        
