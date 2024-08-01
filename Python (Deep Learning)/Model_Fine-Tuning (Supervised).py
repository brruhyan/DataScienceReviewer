# Evaluating Model Performance
#-------------------------------------

# Confusion Matrix
from sklearn.metrics import classification_repeort, confusion_matrix
knn = KNeighborsClassifier(n_neighbors = 7)
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size - 0.4,
                                                    random_state = 42)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
      
#-------------------------------------

# Logistic Regression and ROC curve
# if p > 0.5 data is labeled as 1 and vice versa
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size - 0.3,
                                                    random_state = 42)
logreg.fit(X_train, y_train)
y_pred = logred.predict(X_test)

# Predicting probabilities
# calculating the probability of positive or negative
y_pred_prob = logred.predict_proba(X_test)[:,1]
print(y_pred_prob[0]) 

# ROC curve 
# shows how different thresholds affect the false and negative positive rates
# if p = 0, then the model predicts 1 for all positive values and incorreclty predict all negative values
# if p = 1, then the model predicts 0 for all
from sklearn.metrics import roc_curve
fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)
plt.plot([0,1], [0,1], 'k--')
plt.plot(fpr, tpr)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.show()

# ROC AUC 
# if target is 0, 1 then we calculate the area under the curve
from sklearn.metrics import roc_auc_score
print(roc_auc_score(y_test, y_pred_prob))

#-------------------------------------

# Hyperparameter Tuning 
# it is essential to cross-validate to avoid overfitting the parammeters to the test set

# Grid Searching (cross validation)
from sklearn_model.selection import GridSearchCV
kf = KFold(n_splits = 5, shuffle = True, random_state = 42)
param_grid = {"alpha" : np.arange(0.0001, 1, 10),
              "solver": ['saq', 'lsqr']}
ridge = Ridge()
ridge_cv = GridSearchCV(ridge, param_grid, cv = kf)
ridge_cv.fit(X_train, y_train)
print(ridge_cv.best_params_, ridge_cv.best_score_)
                         
