import pickle
import pandas as pd
from sklearn.linear_model import LogisticRegression as lr
from sklearn.multiclass import OneVsRestClassifier as OVR
from sklearn.utils import shuffle
from sklearn.model_selection import cross_val_score
import numpy as np
#we are not scaling features at this moment


def create_binary_multi_model():
    DOOM  = 42

    #for small dataset drop these columns
    def drop(df):
        for col in list(df):
            if 'src' in col or 'dst' in col or 'id' in col:
                df.drop(col,axis=1,inplace=True)

    path = 'DATA'

    df = pd.read_csv('model_data/DATA/trainb.csv')
    df = shuffle(df)

    print('\nabsolute correlation :')

    print(df.corr()[['label']].apply(lambda x: np.round(((x**2)**0.5),4))['label'].sort_values(ascending=False).head(100))

    drop(df)
    Y = df.label
    df = df.drop('label',axis=1)

    df = df.fillna(-1)
    print(df.shape)
    clf = lr(random_state=DOOM,solver='liblinear',penalty='l1',max_iter=50)

    clf = clf.fit(df,Y)
    filename = 'binary'
    pickle.dump(clf, open(filename, 'wb'))

    print('roc_auc : ')
    print(cross_val_score(clf, df,Y,cv=3,verbose=3,scoring='roc_auc'))

    print('Number of nonzero weights : ',sum((clf.coef_!=0)[0]))

    #multi (secondary)

    path = 'DATA'

    df = pd.read_csv('model_data/DATA/trainl.csv')
    df = shuffle(df)
    drop(df)
    Y = pd.read_csv('model_data/DATA/labels.csv')

    df = df.fillna(-1)
    print(df.shape)
    clf = OVR(lr(random_state=DOOM,solver='lbfgs', penalty='l2',max_iter=2000)).fit(df,Y)
    filename = 'multi'
    pickle.dump(clf, open(filename, 'wb'))




create_binary_multi_model()
