import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("CBC.csv")

def classification_model(model, data, predictors, outcome):
  
    X = data[predictors]
    y = data[outcome]
  
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.33)
  
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)
    return accuracy
    
model = LogisticRegression()
predictor_var = ['Gender', 'M', 'R', 'F', 'FirstPurch', 'ChildBks', 'YouthBks', 'CookBks', 'DoItYBks', 'RefBks', 'ArtBks', 'GeoBks', 'ItalCook', 'ItalAtlas', 'ItalArt', 'Related purchase']
outcome_var = 'Florence'

scoring = []
for i in range(10):
    classification_model(model, df,predictor_var,outcome_var)
    scoring.append(classification_model(model, df,predictor_var,outcome_var))
    
print(np.mean(scoring))