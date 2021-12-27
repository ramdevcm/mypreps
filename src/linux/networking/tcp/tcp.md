# TCP
TCP is a transport layer protocol like [UDP](../udp/udp.md) but it guarantees *reliability, flow control* and *congestion control*.

>TCP guarantees reliable delivery by using sequence numbers. 

![TCP 3 Way-HandShake](tcp1.drawio.svg)

## TCP Demo

```
tcpdump -S -i any port 80
```
-S
--absolute-tcp-sequence-numbers
Print absolute, rather than relative, TCP sequence numbers.

```
curl www.github.com
curl www.linkedin.com
```

![TCP Demo](tcp2.drawio.svg)

from this, you can observe the sequence and acknowledgement numbers of the client and the server. 

## References
[inetdaemon.com](https://www.inetdaemon.com/tutorials/internet/tcp/3-way_handshake.shtml)