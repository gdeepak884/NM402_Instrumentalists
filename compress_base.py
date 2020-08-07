from scapy.all import *
from packetClass import *
import socket
import time,sys
import pickle
from gethash import *

dict = {}

HEADERSIZE = 10


if len(sys.argv) != 3: 
	print ("Correct usage: script, IP address, port number")
	exit() 
IP_address = str(sys.argv[1]) 
Port = int(sys.argv[2]) 

s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
s.bind((IP_address,Port))
s.listen(5)

clientsocket=1
address =1

def pkt_callback(pkt):
    # pkt.show()
    # print(pkt[IP].version)
    
    ip1 = ip(pkt[IP].version, pkt[IP].ihl, pkt[IP].tos, pkt[IP].len, pkt[IP].id, pkt[IP].flags, pkt[IP].frag, pkt[IP].ttl, pkt[IP].proto, pkt[IP].chksum, pkt[IP].src, pkt[IP].dst, pkt[IP].options)
    tcp1 = tcp(pkt[TCP].sport, pkt[TCP].dport, pkt[TCP].seq, pkt[TCP].ack, pkt[TCP].dataofs, pkt[TCP].reserved, pkt[TCP].flags, pkt[TCP].window, pkt[TCP].chksum, pkt[TCP].urgptr, pkt[TCP].options)

    # print(pkt1)
    st = pkt[IP].src + " " + pkt[IP].dst + " " + str(pkt[TCP].sport) + " " + str(pkt[TCP].dport) + " " + str(pkt[IP].version) + " " + str(pkt[IP].proto)
    # print(st)
    hid = hash1(st) & 0xffffffff
    
    print("calculated: ", hid)

    if(hid in dict):
        comp = tcpipmod(True, hid, pkt[IP].ihl, pkt[IP].tos, pkt[IP].len, pkt[IP].id, pkt[IP].flags, pkt[IP].frag, pkt[IP].ttl, pkt[IP].chksum, pkt[IP].options, pkt[TCP].seq, pkt[TCP].ack, pkt[TCP].dataofs, pkt[TCP].reserved, pkt[TCP].flags, pkt[TCP].window, pkt[TCP].chksum, pkt[TCP].urgptr, pkt[TCP].options)
    else:
        dict[hid] = st
        comp = tcpip(False, pkt[IP].version, pkt[IP].ihl, pkt[IP].tos, pkt[IP].len, pkt[IP].id, pkt[IP].flags, pkt[IP].frag, pkt[IP].ttl, pkt[IP].proto, pkt[IP].chksum, pkt[IP].src, pkt[IP].dst, pkt[IP].options, pkt[TCP].sport, pkt[TCP].dport, pkt[TCP].seq, pkt[TCP].ack, pkt[TCP].dataofs, pkt[TCP].reserved, pkt[TCP].flags, pkt[TCP].window, pkt[TCP].chksum, pkt[TCP].urgptr, pkt[TCP].options)
    
    comp.tellStatus()
    msg = pickle.dumps(comp)
    msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
    #print(msg)
    clientsocket.send(msg)
    # print("hash: ",hash(s) & 0xffffffff)
    # debug statement


while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")

    # d = Person("We won SIH",2020)
    sniff(iface="wlo1", prn=pkt_callback, filter="tcp and host 192.168.43.199", store=0)
    # msg = pickle.dumps(d)
    # msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
    # print(msg)
    # clientsocket.send(msg)
