# OSI MODEL

>OSI - Open Systems Interconnection and consist of 7 layers.

It describes how information from a software application in one computer moves through a physical medium to the software application in another computer

![OSI Model](osi.drawio.svg)

## Application Layer
- Only layer that directly interacts with data from the user
- Protocols 
    - HTTP
    - FTP
    - SMTP
    - POP
## Presentation Layer
- it defines how two devices should *encode*, *encrypt*, and *compress* data, so it is received correctly on the other end
## Session Layer
- it creates communication channels (*sessions*)
- ensure channel is open till the communication ends
## Transport Layer
- it takes data transferred in the session layer and breaks it into “segments” on the transmitting end 
- viceversa to the above process at receiving end
- responsible for flow control and error control
## Network Layer
- takes segments from transport layer and makes it into “packets”
- routing occurs here, i.e. it finds best physical path to transfer the data to destination
- used in communication b/w different networks
## Data Link Layer
- takes packets from the network layer and breaks them into smaller pieces called as “frames”
- used in communication b/w same network
## Physical Layer
- physical cable or wireless connection between network nodes
- data gets converted into a bit stream, which is a string of 1s and 0s.