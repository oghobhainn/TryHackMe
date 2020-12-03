# Day 02 - Web Exploitation

Second day of the advent, we reach a different website:

![website](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day02/website.png)

## GET param and URL

A classic URL would be `https://tryhackme.com/?user=oghobhainn` where we add a GET parameter, which is the user. Here the name of the user was given.

![website-get](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day02/website-get.png)

## File Uploads

When you have the ability to upload files to a server, you have a path straight to RCE (Remote Command Execution). An upload form with no restrictions would mean that you could upload a script that, when executed, connects back to your attacking machine and gives you the ability to run any command you want. 
It is very uncommon to find a file upload with _no filtering_, but less uncommon one with _flawed filtering techniques_ which can be circumvented to upload a malicious script.
The scrit has to be writte in a language which the server can execute : most of the time in _PHP_.

In this exemple, There's a _File Extension Filtering_, which checks the file extensions of uploaded files. This is done by specifying a list of allowed extensions. Here its _jpeg, jpg, png, _.
Many extension filters split a filename at the dot (.) and check what comes after it against the list. This makes it very easy to bypass by uploading a double-barrelled extension (e.g. .jpg.php).

When implementing an upload system, it's good practice to upload the files to a directory that can't be accessed remotely. But it's _otften not the case_, and scripts are uploaded to a subdir on the webserver (/uploads, /images, /ressources,...)

![website-sourcecode](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day02/website-sourcecode.png)

## Reverse Shell

Now that we know that we can upload and what file's extension is authorized, we need to decide _what_ to upload.
The most common would be a _Reverse Shell_, a script that creates a network connection _from_ the server, _to_ our attacking machine.
Majority of servers are in PHP-backend, so we need a php script ; we can find one at `/usr/share/webshells/php/php-reverse-shell.php`.

We juste have to edit the `$IP`and the `$PORT` into the IP of our attacking machine, and an arbitrary port.

![reverse-shell](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day02/reverse-shell.png)

Then we navigate to the file, execute it and _voilà!_, the connexion is set.

![reverse-shell-schema](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day02/reverse-shell-schema.png)

## Reverse Shell Listener

A _Reverse Shell Listener_ is used to open a network socket to receive a raw connection (the reverse shell ? :-)). We can do it using _netcat_.
We can create a listener to an uploaded reverse shell using `sudo nc -lnvp $443` (the port precised in the reverse shell file). 
Once netcat has been setup, our reverse shell will be able to connect back to this when activated !

Aaaaand here's our _flag_ !

![flag-time](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day02/flag-time.png)
