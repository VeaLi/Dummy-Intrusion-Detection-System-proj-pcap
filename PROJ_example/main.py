from funs.build_dict import build_dict
from funs.agg import agg
from funs.primary import primary
from funs.secondary import secondary
from funs.catch import catch
import pickle
import pandas as pd
import time
import numpy as np
import warnings

def drop(df):
    for col in list(df):
        if 'src' in col or 'dst' in col or 'id' in col:
            df.drop(col,axis=1,inplace=True)
    return df


def main(I = 'eth0',drop=drop):

    def warn(*args, **kwargs):
        pass
    warnings.warn = warn
    
    binary = pickle.load(open('funs/model_data/binary', 'rb'))
    model = primary(model=binary)

    multi = pickle.load(open('funs/model_data/multi', 'rb'))
    model_ = secondary(model=multi)
    model_.read_cat()
    
    while True:
        try:
            catch(I) # writing to dump
            df = build_dict()
            df = agg(df)
            statinfo = os.stat('cap.pcap')
            df['size'] = statinfo.st_size # there is about 200000 features in pcap that wiresahrk can offer let's consider files size atleast!
            df = drop(df)
            model.data = df # building record
            res,resb = model.predict() # predict label for record
            d = {0:'no anomalies',1:'it looks like an anomaly'}
            print(res[0],' ',end='')
            
            res[0] = int(res[0]>0.53)
            
            print(d[res[0]], time.ctime(),'\n')

            if resb[0]==1 and res[0]==1:
                print('it can be ...')
                model_.data = df
                res,labels = model_.predict()

                for l,r in zip(labels,res[0]):
                    if l!='normal':
                        print('-'*(1+int(str(r)[2])),r," : ",l)
            
            
        except Exception as e:
            print(e)










if __name__ == '__main__':
    main()
