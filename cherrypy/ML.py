import numpy as np
import pandas as pd
import matplotlib as mp
import matplotlib.pyplot as plt
from patsy  import *
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics

#see http://nbviewer.ipython.org/github/justmarkham/gadsdc1/blob/master/logistic_assignment/kevin_logistic_sklearn.ipynb
#most of the logistic regression steps came from this nice blog post

def get_probs(age , gcsmotor , daysicu , normalscan):

    #df = pd.read_csv('D:\\ds_ldn\\modified-data\\data-cleaned1.csv')
    df = pd.read_csv('/home/sarikan/d_drive/ds_ldn/modified-data/data-cleaned1.csv')

    #plt.hist(df[(df['6M5_Living'] > 0) & (df['6M5_Living'] <= 3)] )
    #items = df[(df['6M5_Living'] > 0) & (df['6M5_Living'] <=  3) ]
    #plt.hist(df['6M5_Home'])



    y,X = dmatrices('Res6M5_Home ~ AGE + GCS_MOTOR + EO_DaysICU + EO_Normal_scan', df, return_type='dataframe')
    #print X.columns
    # flatten y into a 1-D array
    y = np.ravel(y)

    # instantiate a logistic regression model, and fit with X and y
    model = LogisticRegression()
    model = model.fit(X, y)

    # check the accuracy on the training set
    #model.score(X, y)

    # check the accuracy on the training set
    # examine the coefficients

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

    probs = model.predict_proba([1, int(age) , int(gcsmotor) , int(daysicu) , int(normalscan)])
    state = ['No help required at home','Some help required but not every day', 'Help needed every day', 'Help needed but not due to injury' ]
    print(state[probs.argmax()])
    print(age)
    print(gcsmotor)
    print(daysicu)
    print(normalscan)
    print(probs)
    return state[probs.argmax()]

if __name__ == '__main__':
    print get_probs()