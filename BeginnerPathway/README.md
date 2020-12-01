# Beginner Pathway - becoming a padawan

## Basic useful commands
```
ssh <user>@<host>
su <user>

find <dir> -name <name> -type <f,d,...> 2>/dev/null
curl -O url
hostname
ifconfig
```

## PrivEsc - climbing to the top

### SUID/GUID
Files with the SUID/GUID bit set can be run with the perms of the file owner/group
To find them :
```
find /perm -perm -u=s -type f 2>/dev/null
```
### /etc/passwd
Text file containing a list of the system's account. If it's writable by a non-root user (mistake), we can add a new user into it with root perms.
An user is stored like this :
```
test:x:0:0:root:/root/bin/bash
username:passwd:uid:gid:uid-info:homedir:command/shell
```
- *username*
- *password* encrypted in /etc/shadow file. Here it's the hash of the passwd.
- *User ID* each user has an UID. 0 is for roots and UIDS 1-99 for predefined accounts. 100-999 are reserved by system for admin and system accounts/groups.
- *GID* the primary groupd ID, stored in /etc/group file
- *User ID info* the comment field (with phone number, address...)
- *Home Dir* the absolute path to the directory the user will be in when they log in. If it doesn't exist, it becomes /
- *Command/Shell* the absolute path of a command or shell (/bin/bash)

To add a new user, we first need a hashed password ([salt] being the new user's name):
```
openssl passwd -1 -salt [salt] [password]
```
To modify /etc/passwd, open it with vi/vim/nano and write on it. echo "..." didn't work, dk why.

## TCP/IP

The three-way handshake consists of three stages. First the connecting terminal (our attacking machine, in this instance) sends a TCP request to the target server with the SYN flag set. The server then acknowledges this packet with a TCP response containing the SYN flag, as well as the ACK flag. Finally, our terminal completes the handshake by sending a TCP request with the ACK flag set.
![TCP/IP Three-Way Handshake](https://github.com/oghobhainn/TryHackMe/blob/main/images/TCP-IP.png)
