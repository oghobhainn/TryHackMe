# Networking Tools

## Ping - "Hello ? Is anyone there ?"
The ping command is used when we want to test whether a connection to a remote source is possible.
It works using the ICMP (Internet Control Message Protocol), and is very portative.
```
ping <target> (DNS or IP)
```
![Ping example](https://github.com/oghobhainn/TryHackMe/blob/main/images/ping.png)

## Traceroute - Back when people hadn't smartphones, we used maps

Traceroute allows you to see every intermediate step between your computer and the ressource it requested - and there's a lot of them !
It also uses the ICMP protocol.
```
traceroute <destination>
```
![Traceroute example](https://github.com/oghobhainn/TryHackMe/blob/main/images/traceroute.png)
