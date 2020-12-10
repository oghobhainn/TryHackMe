# Day09 - Anyone Can Be Santa !

## FTP - File Transfer Protocol

FTP servers are used to share files between devices.

![ftp](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day09/ftp.png)

The standard for these two connections are the __ports 20 (data) and 21 (Commands)__.
Commands involve actions such as listing or navigating directories, writing to files ...
The data port is where actual data such as the dowloading/uploading of files are transferred over.

To connect to our vulnerable instance, we simply use `ftp $ip`

![]()

![connect](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day09/connect.png)

|Command|Description|
|-------|-----------|
|ls|List files and directories in the working directory on the FTP server|
|cd|Change our working directory on the FTP server|
|pwd|Prints the current working directory|
|get|Download a file from the FTP server to our device|
|put|Upload a file from our device to the FTP server|

We list what are inside, and see there's a `/public` dir on which we have all the rights.

![public-dir](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day09/public-dir.png)

![cd](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day09/cd.png)

There's a shell script in the server, let's `get`it !

Inside, a simple shell script is written to do some backups every minute.

![shell](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day09/shell.png)

If we can download a file, it may be possible that we have the perms to upload one ? Uploading a file requires separate permissions that shouldn't be granted to the "anonymous" user. However, permissions are very easy to oversight - SPOILER ! - it is the case here.

We get the correct payload on this [CheatSheet](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md#bash-tcp), put it in the file and upload it back on the FTP server. The file is written in bash, so will be our paylaod.

![malicious-bash](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day09/malicious-bash.png)

Now we have to set up a __netcat listener__ to catch the connection, using `nc -lvnp 4444`

And after waiting a minute for the backup to be triggered once again, here we are !

![nc-listener](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day09/nc-listener.png)
