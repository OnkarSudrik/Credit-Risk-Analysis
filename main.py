import pandas as pd 
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier

# importing the dataset 
df = pd.read_csv("D:\\Project\\new_projects\\Credit_Risk_Prediction\\UCI_Credit_Card.csv")

# changing the column names 
df.columns = ['ID','LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE', 'AGE', 'PAY_1', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6',
              'BILL_AMT1', 'BILL_AMT2', 'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6', 'PAY_AMT1', 'PAY_AMT2',
              'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6', 'Default']



# Define features and target variable
X = df.drop(columns=['Default', 'ID'])  # Features unecessary for prediction 
y = df['Default']  # Target variable

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize Gradient Boosting Classifier model
gb_model = GradientBoostingClassifier(random_state=42)

# Train the model
gb_model.fit(X_train, y_train)

# Predict on the test set
gb_pred = gb_model.predict(X_test)



# saving the model 
pickle.dump(gb_model, open('model.pkl', 'wb'))
