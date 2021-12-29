# Networking

- [OSI Model](./osi/osi.md)
- [DNS](./dns/dns.md)
- [UDP](./udp/udp.md)
- [TCP](./tcp/tcp.md)

## What happens when you type *www.google.com* in your browser?

Every device located on the internet is uniquely identified by the unique id called *ip address*.
so, when we type the URL *http://www.google.com* in our browser, this is given as an input to a *service* to fetch the ip address of the server that contains google.com, i.e. 

This service is termed as DNS (Domain Name Service).

![DNS Basics](networking1.drawio.svg)

Now, the browser gets the IP of google.com from DNS systems and the browser sents requests to that IP address.

![Diagram](networking2.drawio.svg)