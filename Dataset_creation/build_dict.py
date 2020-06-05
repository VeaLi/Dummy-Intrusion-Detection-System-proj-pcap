from scapy.all import *
import pandas as pd
import warnings
def warn(*args, **kwargs):
    pass

# !!!CEIL=200!!! + whole weight of 1 sec pcap file

def build_dict(file,CEIL=200):
    '''
    every record in pandas.DataFrame can be secribed ad python dictionary
    this function created pandas.DataFrame from .pcap files
    in: file name
    out: df
    '''

    warnings.warn = warn
    
    #create empty record so we will have all features presented
    #even if they might exclude each other like UDP or TCP
    record1 = {}
    for feat in ['eth_dst','eth_src','eth_type','ip_version','ip_ihl','ip_tos','ip_len','ip_id','ip_flags','ip_frag','ip_ttl','ip_proto','ip_chksum','ip_src','ip_dst','udp_sport','udp_dport','udp_len','udp_chksum','tcp_sport','tcp_dport','tcp_seq','tcp_ack','tcp_dataofs','tcp_reserved','tcp_flags','tcp_window','tcp_chksum','tcp_urgptr','tcp_options']:
        record1[feat] = -1
    
    file = 'TEMP/'+file
    pcap = rdpcap(file)
    
    df = pd.DataFrame()
    CNT = [0]
    for pkt in pcap:
        if CNT[0]<CEIL:
            CNT[0]+=1
            record = record1
            
            if pkt.haslayer(Ether):
                record['eth_dst'] = pkt[Ether].dst
                record['eth_src'] = pkt[Ether].src
                record['eth_type'] = pkt[Ether].type
                
            if pkt.haslayer(IP):
                record['ip_version'] = pkt[IP].version
                record['ip_ihl'] = pkt[IP].ihl
                record['ip_tos'] = pkt[IP].tos
                record['ip_len'] = pkt[IP].len
                record['ip_id'] = pkt[IP].id
                record['ip_flags'] = pkt[IP].flags
                record['ip_frag'] = pkt[IP].frag
                record['ip_ttl'] = pkt[IP].ttl
                record['ip_proto'] = pkt[IP].proto
                record['ip_chksum'] = pkt[IP].chksum
                record['ip_src'] = pkt[IP].src
                record['ip_dst'] = pkt[IP].dst
                
                
            if pkt.haslayer(UDP):
                record['udp_sport'] = pkt[UDP].sport 
                record['udp_dport'] = pkt[UDP].dport
                record['udp_len'] = pkt[UDP].len
                record['udp_chksum'] = pkt[UDP].chksum
                
            if pkt.haslayer(TCP):
                record['tcp_sport'] = pkt[TCP].sport
                record['tcp_dport'] = pkt[TCP].dport
                record['tcp_seq'] = pkt[TCP].seq
                record['tcp_ack'] = pkt[TCP].ack
                record['tcp_dataofs'] = pkt[TCP].dataofs
                record['tcp_reserved'] = pkt[TCP].reserved
                record['tcp_flags'] = pkt[TCP].flags
                record['tcp_window'] = pkt[TCP].window
                record['tcp_chksum'] = pkt[TCP].chksum
                record['tcp_urgptr'] = pkt[TCP].urgptr
                record['tcp_options'] = pkt[TCP].options
            
            
            df = df.append(record,ignore_index=True)
    return df
