import pandas as pd
import os
from split import split
from agg import agg
from join import join
from build_dict import build_dict
#for jupiter notebook
#from tqdm import tqdm_notebook as tqdm
from tqdm import tqdm
import warnings
def warn(*args, **kwargs):
    pass





def mk_dir():
    try:
        os.mkdir('TEMP')
        os.mkdir('TEMP_CSV')
    except:
        _ = [os.remove('TEMP/'+f) for f in os.listdir('TEMP')]
        _ = [os.remove('TEMP_CSV/'+f) for f in os.listdir('TEMP_CSV')]
        os.rmdir('TEMP')
        os.rmdir('TEMP_CSV')
        os.mkdir('TEMP')
        os.mkdir('TEMP_CSV')


def main():
    warnings.warn = warn
    mk_dir()
    print('# split\n')
    split()
    print('# building dictionary\n')
    for file in tqdm(os.listdir('TEMP')):
        statinfo = os.stat('TEMP/'+file)

        #check if it is empty shell
        if statinfo.st_size>1000:
            try:
                df = build_dict(file)
                df = agg(df)
                
                #cant use if df on it
                if len(df.index)!=0:
                    df['size'] = df['size'] = statinfo.st_size
                    df['raw_label'] = file.replace('.pcap','')
                    df.to_csv('TEMP_CSV/'+file.replace('.pcap','.csv'),index=False)
                    
            except Exception as e:
                print(e)

    print('# collecting dataframe\n')
    r,c = join()
    print('\nGOT ',r,'nonzero records out of ',len(os.listdir('TEMP')),'files\n')
    print('df shape: ',r,'x',c)
    mk_dir()
        





if __name__ == '__main__':
    main()

