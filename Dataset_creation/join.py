import pandas as pd
from tqdm import tqdm
import os


def join():
    '''
    this function collects record from TEMP_CSV in one TRAIN.csv
    in: None
    out: writes to YOUR_DATASET_WILL_BE_HERE folder
    '''
    df = pd.DataFrame()
    for file in tqdm(os.listdir('TEMP_CSV')):
        dff = pd.read_csv('TEMP_CSV/'+file)
        df = df.append(dff,ignore_index=True)

    df.to_csv('YOUR_DATASET_WILL_BE_HERE/TRAIN.csv',index=False)

    print('\n\n\n')
    print('# # #')
    print(df.head())

    print(df.describe().T)
    
    return df.shape
