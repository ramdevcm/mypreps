# DNS
>Domain Names are the simple human-readable names for websites. The Internet understands only IP addresses but humans give names for that IP address.

## DNS Resolution
When someone tries to use *google.com*, the browser tries to convert this by passing it through different layers and finally fetches the IP address of *google.com*. This process is called DNS resolution.

***DNS is an application layer protocol that runs on top of UDP(most of the times).***

>DNS servers usually listen on port number 53

## Troubleshooting DNS

- start with the root DNS servers and perform non-recursive queries following the nameserver delegation of sub-domains until we find the authoritative DNS servers. 
- at that point, we query the server for the host information we need. 
- if the answer is correct and no errors are given, we know DNS is working properly.

Two tools exist that assist us in troubleshooting DNS:

1. dig
2. nslookup