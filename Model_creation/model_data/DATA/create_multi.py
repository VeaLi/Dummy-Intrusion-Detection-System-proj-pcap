import pandas as pd


def create_multi():
    df = pd.read_csv('../Dataset_creation/YOUR_DATASET_WILL_BE_HERE/TRAIN.csv')


    CAT = ['dos','inject','scan','infect','capture_flag','normal','exploit','worm']


    def f(x):
        for c in CAT:
            if c in x.lower():
                return c
        else:
            return 'unrecognized_anomaly'

    df['label'] = df['raw_label'].apply(f)
    Y = df['label']
    df.drop(['label','raw_label'],axis=1,inplace=True)

    Y = pd.get_dummies(Y)

    df.to_csv('model_data/DATA/trainl.csv',index=False)
    Y.to_csv('model_data/DATA/labels.csv',index=False)
    with open('available_cat.txt','w') as f:
        f.write(' '.join(Y.columns.tolist()))
    print(Y.columns)




create_multi()
