# TryHackMe CheatSheet

## nmap

```
nmap -sV -sC -v $ip
nmap -p- $ip
```

## gobuster

```
apt-get install gobuster
gobuster dir -u http://$ip:<port> -w /usr/share/wordlists/rockyou.txt (or /wordlists/dirb/big.txt to downlaod)
curl -o big.txt https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/big.txt
```

## burpsuite

### Fuzz



## NOTES:

- reverse shell : a RS is being called on the remote host and forces this host to make a connection to me. So I'm listening for incoming connections, upload and have the shell executed.
1. php: 
```
hello
```
2. python:
```
bonjour
```
- other 
