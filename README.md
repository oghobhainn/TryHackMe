# TryHackMe CheatSheet

## Remote connexion

###If we have the password:

```
ssh <username>@$ip(:<port>)
```

###If we have an SSH private key:

-put it into a file
-change its mods `chmod 600 <privatekey_file>`

```
ssh -i privatekey_file <username>@ip
```

but if the SSH private key is __password protected__, we can use John The Ripper.

First we have to 'tranlsate' the privatekey_file into something usable by john.

```
/opt/john/ssh2john.py <privatekey_file> > tojohn.txt
```

Then we can run __John The Ripper__ itself, and it gives us the password for the ssh rsa key connection : 

```
/opt/john/john forjohn.txt --wordlist=/opt/share/usernames/wordlists/rockyou.txt
```

## Ports Scanning - nmap

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

## enum4linux

__enumerating data from windows and samba hosts__

```
apt-get install enum4linux
enum4linux/enum4linux.pl -a $ip | tee enum4linux.log
```

## hydra

__password guesser__

```
hydra -l $username -P /usr/share/wordlists/rockyou.txt ssh://$ip
```

(`ssh` specifies the kind of connexion we're using.)

## privEsc

### linpeas

```
git clone https://raw.githubusercontent.com/carlospolop/privilege-escalation-awesome-scripts-suite/master/linPEAS/linpeas.sh
```

If we know the creds, we can use it `scp` (copy files and directory between two locations.). We put it into the shared memory directory. 

```
scp linpeas.sh $username@$ip:/dev/shm
```

## burpsuite

### Fuzz



## NOTES:

### reverse shell : a RS is being called on the remote host and forces this host to make a connection to me. So I'm listening for incoming connections, upload and have the shell executed.
- php: 
```
hello
```
- python:
```
bonjour
```
- other 
