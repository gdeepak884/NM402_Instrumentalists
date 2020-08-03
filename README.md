# NM402_Instrumentalists
## Approach 
 
 ### INFERRED
      These fields contain values that can be inferred from other
      values (for example, the size of the frame carrying the packet)
      and thus do not have to be handled at all by the compression
      scheme.
   
 ### STATIC
      These fields are expected to be constant throughout the
      lifetime of the packet stream. Static information must in some
      way be communicated once. STATIC fields whose values define a
      packet stream. They are in general handled as STATIC.
      These STATIC fields are expected to have well-known values and
      therefore do not need to be communicated at all.
 
 ### CHANGING
      These fields are expected to vary randomly within a limited
      value set or range or in some other manner.
      
![Approach](./approach.docx)


## Tesing 

**Testing on localserver:**
The `chat server/` subdirectory contains test applications.

       1. python server.py
       2. python client.py 127.0.0.1 1234 with username{ex. deepak}
       3. python client.py 127.0.0.1 1234 with another username{ex. gdeepak}

### References:
   
   ROHC paper RFC 3095,
   White Paper Header Compression The portion are partially or completely taken from different resources
   Zlib Python Library
   Socket Programming
