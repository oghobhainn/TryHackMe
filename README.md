# TryHackMe

## Linux Commands
```
ssh <user>@<host>	-> remotely accessing a machine !!! it's / @ \ between the two.
su	<user>			-> to change user on same machine
find <dir> -name <name> -type (f file, d dir, ...) 2>/dev/null (to avoid all non authorized access msges)
chmod 421-421-421 (for ex: chmod 760) for rights on read, write and exec.
chown 				-> changes the user and the group who the file belongs to (see with ls -la)
		example :	to set the owner of <file> to be 'master' : chown master file.
					to set owner and group to master : chown master:master file
curl				-> to download a file
	-O				keeps the original name
		example :	curl -O https://github.com/rebootuser/LinEnum/blob/master/LinEnum.sh
hostname		: to know the host of the machine
cat /etc/passwd ( | grep user) : to know how many users of the machine there are
cat /etc/shells		: to know how many shells are currently running


```
### Cronjobs

located in the spool directory (/var/spool/cron/crontabs). There are all the cronjobs for all users, except the root user 
stored in tables called crontabs

To display contents of the root user’s crontab, use the less command:

crontab -l		:	to list all the cronjobs for the current user

### SUID/GUID

The first step in Linux privilege escalation exploitation is to check for files with the SUID/GUID bit set. This means that the file or files can be run with the permissions of the file(s) owner/group.
An *SUID binary* any file has read/write/execute permissions for an user, a group and the other :
|user|group|others|
|rwx|rwx|rwx|
|421|421|421|
When special permission is given to each user it becomes SUID or SGID. When extra bit "4" is set to user(Owner), it becomes SUID (Set User ID) and when bit "2" is set to group it becomes SGID (Set Group ID).
SO we're looking for
```
SUID : rws-rwx-rwx
GUID : rwx-rws-rwx
```
To find SUID binaries : find / -perm -u=s -type f 2\>/dev/null
The  -u=s means any of the permission bits mode are set

## Linux Registers

## Linux PrivEsc - Privilege Escalation
![privEsc Tree](https://github.com/oghobhainn/TryHackMe/blob/main/images/privEscTree.png)
### LinEnum
Simple Bash script that performs common commands related to privEsc.
```
curl -O https://github.com/rebootuser/LinEnum/blob/master/LinEnum.sh
```


## Web Fondamentals

Once the browser knows the IP address (thanks to the DNS), it can ask for the web page using GET REQUEST (http verb). Extra resources like jss, images, css... get their own GET REQUEST.
HTTP runs on port 80 -> CTF: if port 80 is open, there's probably a website listening to you
HTTPS runs on port 443 (secured http connexion).

HTML defines the structure of the page
CSS allows you to change how the pages look
JavaScript is a programming language that runs in the browser and allows you to make pages interactive or load extra content.

### HTTP verbs

- *GET* to retrieve content. *curl* is a GET REQUEST		ex: curl http://10.10.82.69:8081/ctf/get
- *POST* to send data to a web server (adding a comment, performing a login)	ex: curl -X POST --data="flag_please" http://< IP >
- * *

#### HTTP Responses
- *100-199*: Information
- *200-299*: Successes (200 OK is the "normal" response for a GET)
- *300-399*: Redirects (the information you want is elsewhere)
- *400-499*: Client errors (You did something wrong, like asking for something that doesn't exist)
- *500-599*: Server errors (The server tried, but something went wrong on their side)

### COOKIES
Cookies are small bits of data that are stored in your browser. Each browser will store them separately, so cookies in Chrome won't be available in Firefox. They have a huge number of uses, but the most common are either session management or advertising (tracking cookies). Cookies are normally sent with every HTTP request made to a server.

Why Cookies ? Because HTTP is stateless (Each request is independent and no state is tracked internally).
Cookies can be broken down into several parts. Cookies have a name, a value, an expiry date and a path. The name identifies the cookie, the value is where data is stored, the expiry date is when the browser will get rid of the cookie automatically and the path determines what requests the cookie will be sent with.

#### Manipulating Cookies

Using your browser's developer tools, you can view and modify cookies. In Firefox, you can open the dev tools with F12. In the Storage tab, you can see cookies that the website has set. There's also a "+" button to allow you to create your own cookies. You can modify all cookies that you can see in this panel, as well as adding more.
- To get a cookie : curl http://< ip >:8081/ctf/getcookie -c cookielist.txt	(then check the cookielist file)
- To add a cookie : curl http://< ip >:8081/ctf/sendcookie --cookie < name > = < value >

## Networking

### Overview of the OSI - Open System Interconnection
OSI is a standardised model behind computer networking.
![OSI Model](https://github.com/oghobhainn/TryHackMe/blob/main/images/OSI_model.png)

But IRL we use the TCP/IP model, which is less understanbl but actually the same things happen.



## OpenVPN
