# TryHackMe

## Linux Commands
```
ssh <user>@<host>	-> remotely accessing a machine
su	<user>			-> to change user on same machine
find <dir> -name <name> -type (f file, d dir, ...) 2>/dev/null (to avoid all non authorized access msges)
chmod 421-421-421 (for ex: chmod 760) for rights on read, write and exec.
chown 				-> changes the user and the group who the file belongs to (see with ls -la)
		example :	to set the owner of <file> to be 'master' : chown master file.
					to set owner and group to master : chown master:master file
curl				-> to download a file
	-O				keeps the original name
		example :	curl -O https://github.com/rebootuser/LinEnum/blob/master/LinEnum.sh

```


## Linux Registers

## Linux PrivEsc - Privilege Escalation
![privEsc Tree](https://github.com/oghobhainn/TryHackMe/blob/main/images/privEscTree.png)
## OpenVPN
