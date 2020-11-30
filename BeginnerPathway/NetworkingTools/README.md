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

## Whois - Most efficient way to get a girl's number

Domain Names are leased out by companies called Domain Registrars.
The command allows you to query who a domain name is registered to. In Europe/N-A, personal details are redacted.
```
whois <domain>
```

## Dig - :notes: I am a dwarf and I'm digging a hole :musical_note: 

Dig allows us to manually query recursive DNS servers of our choice for information about domains.
When you visit a website in your web browser this all happens automatically, but dig allows us to do it manually.

```
dig <domain> @<dns-server-IP>
```
