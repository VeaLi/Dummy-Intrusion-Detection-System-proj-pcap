import pandas as pd



def create_binary():
    df = pd.read_csv('../Dataset_creation/YOUR_DATASET_WILL_BE_HERE/TRAIN.csv')


    def f(x):
        if 'normal' in x:
            return 0
        else:
            return 1

    df['label'] = df['raw_label'].apply(f)
    df = df.drop('raw_label',axis=1)
    df.to_csv('model_data/DATA/trainb.csv',index=False)




create_binary()
