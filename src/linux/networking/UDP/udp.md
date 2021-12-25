# UDP

When a client makes a DNS request, after filling the necessary application payload:
- it passes the payload to the kernel via **sendto** system call
- kernel picks a random port number(>1024) as source port number and puts 53 as destination port number and sends the packet to lower layers
- the kernel on server side receives the packet, it checks the port number and queues the packet to the application buffer of the DNS server process which makes a **recvfrom** system call and reads the packet. 
- This process by the kernel is called multiplexing(combining packets from multiple applications to same lower layers) and demultiplexing(segregating packets from single lower layer to multiple applications).

> Multiplexing and Demultiplexing is done by the Transport layer

**UDP** is one of the simplest transport layer protocol and it does only *multiplexing and demultiplexing*