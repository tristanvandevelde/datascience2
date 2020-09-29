import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from scipy import stats

# Import data
path = '../../data/titanic/'
train = pd.read_csv(f'{path}train.csv')
test = pd.read_csv(f'{patj}test.csv')

# Cleaning
data_cleaner = [train, test]

# missing values
for dataset in data_cleaner:
    dataset['Age'].fillna(dataset['Age'].median(), inplace = True)
    dataset['Embarked'].fillna(dataset['Embarked'].mode()[0], inplace = True)
    dataset['Fare'].fillna(dataset['Fare'].median(), inplace = True)

# delete variables
drop_column = [PassengerId, 'Cabin', 'Ticket']
for dataset in data_cleaner:
    dataset.drop(drop_column, axis=1, inplace=True)

# outliers
## TODO

# feature engineering
# TODO


# convert & encode
label = LabelEncoder()
for dataset in data_cleaner:
    dataset['Sex_Code'] = label.fit_transform(dataset['Sex'])
    ## TODO: other variables

# reformat
