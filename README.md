# NM402_Instrumentalists

## Abstract:
  Due to the rapid evolution of internet and wireless networks a need of the efficient 
    transmission over the channels for QOS. Efficiency is extremely vital once the value
    of transmission is extremely high. Example, in SATCOM networks operate under low bandwidth 
    & power limited scenarios. In order to effectively utilize the network resources,
    the overheads are required to be reduced in the user traffic. Header compression will 
    play a vital role in payload transmission. The result of compression is that there's 
    less and necessary information to send across the link, which in effect, will increase
    the bandwidth of the link.


## Approach 
 We are going to optimize bandwidth usage to reduce the amount of redundant protocol operational
    overhead transmitted with every packet which is belonging to the same packet stream, the version, 
    flow label, next header, source address, and destination address fields are identical. In the IPV4,
    IPV6 and TCP header fields remain static between consecutive packets belonging to the same packet stream. 
    TCP headers include not only static and random fields, but also dynamic fields (i.e., TCP sequence numbers)
    that change incrementally between two consecutive packets.
 
 ### INFERRED

   These fields contain values that can be inferred from other
    values (for example, the size of the frame carrying the packet)
    and thus do not have to be handled at all by the compression
    scheme.
   
 ### STATIC
  
  These fields are expected to be constant throughout the
    lifetime of the packet stream. Static information must in some
    way be communicated only once. STATIC fields whose values define a
    packet stream. They are in general handled as STATIC.
    These STATIC fields are expected to have well-known values and
    therefore do not need to be communicated at all.
 
 ### CHANGING
  
  These fields are expected to vary randomly within a limited
    value set or range or in some other manner.
      
![Approach](./approach.docx)


## Testing 

**Testing on localserver:**

The `chat server/` subdirectory contains test applications.
The `main.py` file can be used to track header fields, send packets and can also used to find open ports.

       >> python server.py
       >> python client.py 127.0.0.1 1234 with username{ex. deepak}
       >> python client.py 127.0.0.1 1234 with another username{ex. gdeepak}

## Result
   Acheived compression ratio of approx. 25% per TCP/IP Packet
   
## References:
   
   ROHC paper RFC 3095,
   White Paper Header Compression The portion are partially or completely taken from different resources
   Zlib Python Library
   Socket Programming
