
# import pyshark

# cap  = pyshark.LiveCapture(interface = 'lo')

# for pkt in enumerate(cap):
#     if 'ip' in pkt:
#         print (pkt,flush = True)
# cap.close()

from scapy.all import *
import zlib
# zlib.crc32(s) 

dict = {}

class ip:  
    
    # Class Variable  
    #static_var = 'any'             
    
    # The init method or constructor  
    def __init__(self, version, ihl, tos, len, id, flags, frag, ttl, proto, chksum, src, dst, options):  
        # Instance Variable      
        self.version = version 
        self.ihl = ihl
        self.tos = tos
        self.len = len
        self.id = id
        self.flags = flags
        self.frag = frag
        self.ttl = ttl
        self.proto = proto
        self.chksum = chksum
        self.src = src
        self.dst = dst
        self.options = options
    
class tcp:  
    
    # Class Variable  
    #static_var = 'any'             
    
    # The init method or constructor  
    def __init__(self, sport, dport, seq, ack, dataofs, reserved, flags, window, chksum, urgptr, options):  
        # Instance Variable      
        self.sport = sport 
        self.dport = dport
        self.seq = seq
        self.ack = ack
        self.dataofs = dataofs
        self.reserved = reserved
        self.flags = flags
        self.window = window
        self.chksum = chksum
        self.urgptr = urgptr
        self.options = options

# hashed values
# version 
# proto
# src
# dst
# sport
# dport
class tcpipmod:
    def __init__(self, compressed, hid, ihl, tos, len, id, ipflags, frag, ttl, ipchksum, ipoptions, seq, ack, dataofs, reserved, tcpflags, window, tcpchksum, urgptr, tcpoptions):  
        # Instance Variable
        self.compressed = compressed 
        self.hid = hid   
        self.ihl = ihl
        self.tos = tos
        self.len = len
        self.id = id
        self.ipflags = ipflags
        self.frag = frag
        self.ttl = ttl
        self.ipchksum = ipchksum
        self.ipoptions = ipoptions
        self.seq = seq
        self.ack = ack
        self.dataofs = dataofs
        self.reserved = reserved
        self.tcpflags = tcpflags
        self.window = window
        self.tcpchksum = tcpchksum
        self.urgptr = urgptr
        self.tcpoptions = tcpoptions

# hashed values
# version 
# proto
# src
# dst
# sport
# dport
class tcpip:
    def __init__(self, compressed, version, ihl, tos, len, id, ipflags, frag, ttl, proto, ipchksum, src, dst, ipoptions, sport, dport, seq, ack, dataofs, reserved, tcpflags, window, tcpchksum, urgptr, tcpoptions):  
        # Instance Variable
        self.compressed = compressed
        self.version = version    
        self.ihl = ihl
        self.tos = tos
        self.len = len
        self.id = id
        self.ipflags = ipflags
        self.frag = frag
        self.ttl = ttl
        self.proto = proto
        self.ipchksum = ipchksum
        self.src = src
        self.dst = dst
        self.ipoptions = ipoptions
        self.sport = sport 
        self.dport = dport
        self.seq = seq
        self.ack = ack
        self.dataofs = dataofs
        self.reserved = reserved
        self.tcpflags = tcpflags
        self.window = window
        self.tcpchksum = tcpchksum
        self.urgptr = urgptr
        self.tcpoptions = tcpoptions

def pkt_callback(pkt):
    # pkt.show()
    # print(pkt[IP].version)
    
    ip1 = ip(pkt[IP].version, pkt[IP].ihl, pkt[IP].tos, pkt[IP].len, pkt[IP].id, pkt[IP].flags, pkt[IP].frag, pkt[IP].ttl, pkt[IP].proto, pkt[IP].chksum, pkt[IP].src, pkt[IP].dst, pkt[IP].options)
    tcp1 = tcp(pkt[TCP].sport, pkt[TCP].dport, pkt[TCP].seq, pkt[TCP].ack, pkt[TCP].dataofs, pkt[TCP].reserved, pkt[TCP].flags, pkt[TCP].window, pkt[TCP].chksum, pkt[TCP].urgptr, pkt[TCP].options)

    # print(pkt1)
    s = pkt[IP].src + " " + pkt[IP].dst + " " + str(pkt[TCP].sport) + " " + str(pkt[TCP].dport)
    hid = hash(s) & 0xffffffff
    if(hid in dict):
        comp = tcpipmod(True, hid, pkt[IP].ihl, pkt[IP].tos, pkt[IP].len, pkt[IP].id, pkt[IP].flags, pkt[IP].frag, pkt[IP].ttl, pkt[IP].chksum, pkt[IP].options, pkt[TCP].seq, pkt[TCP].ack, pkt[TCP].dataofs, pkt[TCP].reserved, pkt[TCP].flags, pkt[TCP].window, pkt[TCP].chksum, pkt[TCP].urgptr, pkt[TCP].options)
    else:
        dict[hid] = s
        comp = tcpip(False, pkt[IP].version, pkt[IP].ihl, pkt[IP].tos, pkt[IP].len, pkt[IP].id, pkt[IP].flags, pkt[IP].frag, pkt[IP].ttl, pkt[IP].proto, pkt[IP].chksum, pkt[IP].src, pkt[IP].dst, pkt[IP].options, pkt[TCP].sport, pkt[TCP].dport, pkt[TCP].seq, pkt[TCP].ack, pkt[TCP].dataofs, pkt[TCP].reserved, pkt[TCP].flags, pkt[TCP].window, pkt[TCP].chksum, pkt[TCP].urgptr, pkt[TCP].options)
    # print("hash: ",hash(s) & 0xffffffff)
    print(comp.compressed)
    print('---------------------------------------------------------') # debug statement

sniff(iface="#####", prn=pkt_callback, filter="tcp and host ###########", store=0)
