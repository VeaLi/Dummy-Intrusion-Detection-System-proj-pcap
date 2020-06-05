import pandas as pd
from tqdm import tqdm_notebook as tqdm
import numpy as np
import warnings
def warn(*args, **kwargs):
    pass





def agg(df=None):

    '''
    greedy statistic evaluation
    in: pandas.DataFrame
    out: pandas.DataFrame

    example: agg(df = my_df)
    '''

    warnings.warn = warn
    
    try:

        for col in list(df):
            df[col] = df[col].replace([np.inf,-np.inf],-1)
            df[col] = df[col].fillna(-1)

        try:
            df['eth_dst'] = df['eth_dst'].apply(lambda x: sum([ord(xx) for xx in str(x)]))
            df['ip_dst'] = df['ip_dst'].apply(lambda x: sum([ord(xx) for xx in str(x)]))
            df['eth_src'] = df['eth_src'].apply(lambda x: sum([ord(xx) for xx in str(x)]))
            df['ip_src'] = df['ip_src'].apply(lambda x: sum([ord(xx) for xx in str(x)]))
            df['ip_flags'] = df['ip_flags'].apply(lambda x: sum([ord(xx) for xx in str(x)]))
            df['tcp_flags'] = df['tcp_flags'].apply(lambda x: sum([ord(xx) for xx in str(x)]))
            df['tcp_options'] = df['tcp_options'].apply(lambda x: sum([ord(xx) for xx in str(x)]))


        except Exception as e:
            #print(df)
            #if empty DataFrame
            return df

        COLS = list(df)[:]

        df = df.fillna(-1)
        
        for col in COLS:
            df['nunique_'+col]=df[col].nunique()
            df['std_'+col]=df[col].std()
            df['mean_'+col]=df[col].mean()
            df['meadian_'+col]=df[col].median()
            df['min_'+col]=df[col].min()
            df['max_'+col]=df[col].max()
            df['mean_diff_'+col]= np.mean(np.diff(df[col].values.tolist()))
            df['std_diff_'+col]= np.std(np.diff(df[col].values.tolist()))

        for col in COLS:
            df[col] = df[col].apply(np.log1p)
            df[col] = df[col].replace([np.inf,-np.inf],-1)
            df[col] = df[col].fillna(-1)

        for col in COLS:
            df['lnunique_'+col]=df[col].nunique()
            df['lstd_'+col]=df[col].std()
            df['lmean_'+col]=df[col].mean()
            df['lmeadian_'+col]=df[col].median()
            df['lmin_'+col]=df[col].min()
            df['lmax_'+col]=df[col].max()
            df['lmean_diff_'+col]= np.mean(np.diff(df[col].values.tolist()))
            df['lstd_diff_'+col]= np.std(np.diff(df[col].values.tolist()))

        for col in list(df):
            df[col] = df[col].replace([np.inf,-np.inf],-1)
            df[col] = df[col].fillna(-1)

        df = df.drop(COLS,axis=1)
        df = df.head(1)
        
    except Exception as e:
        print(e,'something went wrong, check size of the file!')

    return df

