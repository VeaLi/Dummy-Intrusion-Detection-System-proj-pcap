import subprocess as sub
import time


def catch(INTERFACE = 'eth0'):
    start = time.time()
    #-c 200
    p = sub.Popen(('tcpdump', '-i',INTERFACE,'-c','200','port','not','22','-w','cap.pcap'), stdout=sub.PIPE)
    while True:
        if time.time()>start+5:
            p.send_signal(subprocess.signal.SIGTERM)
            return 0
            
                    
