from subprocess import run, PIPE
import os
import time
#garbage collector 
import gc
from tqdm import tqdm
gc.enable()



def split():
    '''
    this function will split pcaps int PUT_PCAPS_HERE folder
    in: NONE
    out: FILES in TEMP folder
    '''
    pcaps = os.listdir("PUT_PCAPS_HERE")
    #ONE SECOND


    full_path = "PUT_PCAPS_HERE/"
    full_path2 = "TEMP/"

    for file in tqdm(pcaps):
        try:
            print(run(["C:\Program Files\Wireshark\editcap.exe",'-F','pcapng','-i','1',full_path+file,full_path2+file],stdout=PIPE, stderr=PIPE,check=True, universal_newlines=True).stdout)
        except Exception as e:
            print(e) 



    
