import socket, zlib, select, string, sys, binascii, zstandard

def display() :
	you="\33[33m\33[1m"+" You:"+"\33[0m"
	sys.stdout.write(you)
	sys.stdout.flush()

def main():
    if len(sys.argv)<2:
        host = raw_input("Enter host ip address: ")
    else:
        host = sys.argv[1]

    port = 5001
    name=raw_input("\33[34m\33[1m Enter username: \33[0m")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    try :
        s.connect((host, port))
    except :
        print "\33[31m\33[1m Can't connect to the server \33[0m"
        sys.exit()
    s.send(name)
    display()
    while 1:
        socket_list = [sys.stdin, s]
        rList, wList, error_list = select.select(socket_list , [], [])
        for sock in rList:
            if sock == s:
                data = sock.recv(4096) 
                compress = zlib.compressobj(zlib.Z_DEFAULT_COMPRESSION, zlib.DEFLATED, +15)
                compressed_data = compress.compress(data)
                cdata += compress.flush()
                f = open('compressed.dat', 'w')
                f.write(cdata)
                f.close()
                CHUNKSIZE = 1024
                if not data :
                    print '\33[31m\33[1m \rDisconnected\n \33[0m'
                    sys.exit()
                else :
                    data2 = zlib.decompressobj()
                    my_file = open('compressed.dat', 'rb')            
                    buf = my_file.read(CHUNKSIZE)
                         while buf:
                           decompressed_data = data2.decompress(buf)
                           buf = my_file.read(CHUNKSIZE)
                           ddata += data2.flush()
                           #ddata = zlib.decompress(ddata)
                           sys.stdout.write(ddata)
                           display()
            else :
                msg=sys.stdin.readline()
                s.send(msg)
                display()

if __name__ == "__main__":
    main()

