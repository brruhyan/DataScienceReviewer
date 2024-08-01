# Preprocessing data

#-------------------------------------

# Dealing with categorical features (dummy variables)
# scikit-learn (OneHotEncoder()) | pandas (get_dummies())

import_pandas as pd 
courses_df = pd.read_csv('students.csv')
courses_dummies = pd.get_dummies(courses_df['course'], drop_first = True)
courses_dummies = pd.concat([courses_df, courses_dummies], axis = 1)
courses_dummies = courses_dummies.drop('course', axis = 1)

# encoding dummy variables with 1 categorical feature
courses_dummies = pd.get_dummies(courses_df, drop_first = True)

#-------------------------------------

# Linear Regression with dummmy variables
from sklearn.model_selection import cross_val_score, KFold
from sklearn.linear_model import LinearRegression
X = courses_dummies.drop('popularity', axis = 1).values
y = courses_dummies['popularity'].values
#splitting
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2,
                                                    random_state = 42)
kf = KFold(n_splits = 5, shuffle = True, random_state = 42)
linear = LinearRegression()
linear_cv = cross_val_score(linear, X_train, y_train, cv = kf,
                            scoring = "neg_mean_squared_error")
print(np.sqrt(-linear_cv))

#-------------------------------------

# Handling missing data
music_df = music_df.dropna(subset = ['genre', 'popularity', 'loudness'])

# imputation (categorical values)
from sklearn.impute import SimpleImputer
x_category = music_df['genre'].values,reshape(-1,1)
x_num = music_df.drop(['genre', 'popularity'], axis = 1).values
y  = music_df['popularity'].values
X_train_cat, X_test_cat, y_train, y_test = train_test_split(X_category,y, test_size = 0.2,
                                                    random_state = 12)
X_train_num, X_test_num, y_train, y_test = train_test_split(X_num,y, test_size = 0.2,
                                                    random_state = 12)
imp_category = SimpleImputer(strategy = 'most_frequent')
X_train_cat = imp_category.fit_transform(X_train_cat)
X_test_cat = imp_category.transform(X_test_cat)

# imputation (numerical values)
imp_num = SimpleImputer()
X_train_num = imp_num.fit_transform(X_train_num)
X_test_num = imp_num.transform(X_test_num)
X_train = np.append(X_train_num, X_train_cat, axis = 1)
X_test = np.append(X_test_num, X_test_cat, axis = 1)

#-------------------------------------

# imputing with a pipeline
from sklearn.pipeline import Pipeline
music_df = music_df.dropna(subset = ['genre', 'popularity', 'loudness'])
music_df['genre'] = np.where(music_df['genre'] == 'Rock', 1,0) #replaces rock genre with 1
X = music_df.drop('genre', axis = 1).values
y = music_df['genre'].values
#instantiating the pipeline
steps = [('imputation', SimpleImputer()),
         ('logistic_regression', LogisticRegression())]\
pipeline = Pipeline(steps)
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3,
                                                    random_state = 42)
pipeline.fit(X_train, y_train)
pipeline.score(X_test, y_test)

#-------------------------------------

# Centering and scaling
