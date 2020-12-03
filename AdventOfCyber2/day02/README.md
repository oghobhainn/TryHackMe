# Day 02 - Web Exploitation

Second day of the advent, we reach a different website:

![website](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day02/website.png)

## GET param and URL

A classic URL would be `https://tryhackme.com/?user=oghobhainn` where we add a GET parameter, which is the user. Here the name of the user was given.

![website-get](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day02/website-get.png)

## File Uploads

When you have the ability to upload files to a server, you have a path straight to RCE (Remote Command Execution). An upload form with no restrictions would mean that you could upload a script that, when executed, connects back to your attacking machine and gives you the ability to run any command you want. 
It is very uncommon to find a file upload with __no filtering__, but less uncommon one with __flawed filtering techniques__ which can be circumvented to upload a malicious script.
The scrit has to be writte in a language which the server can execute : most of the time in __PHP__.

In this exemple, There's a __File Extension Filtering__, which checks the file extensions of uploaded files. This is done by specifying a list of allowed extensions. Here its __jpeg, jpg, png,__.
Many extension filters split a filename at the dot (.) and check what comes after it against the list. This makes it very easy to bypass by uploading a double-barrelled extension (e.g. .jpg.php).

When implementing an upload system, it's good practice to upload the files to a directory that can't be accessed remotely. But it's __otften not the case__, and scripts are uploaded to a subdir on the webserver (/uploads, /images, /ressources,...)

![website-sourcecode](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day02/website-sourcecode.png)

## Reverse Shell

Now that we know that we can upload and what file's extension is authorized, we need to decide __what__ to upload.
The most common would be a __Reverse Shell__, a script that creates a network connection __from__ the server, __to__ our attacking machine.
Majority of servers are in PHP-backend, so we need a php script ; we can find one at `/usr/share/webshells/php/php-reverse-shell.php`.

We juste have to edit the `$IP`and the `$PORT` into the IP of our attacking machine, and an arbitrary port.

![reverse-shell](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day02/reverse-shell.png)

Then we navigate to the file, execute it and __voilà!__, the connexion is set.

![reverse-shell-schema](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day02/reverse-shell-schema.png)

## Reverse Shell Listener

A __Reverse Shell Listener__ is used to open a network socket to receive a raw connection (the reverse shell ? :-)). We can do it using _netcat_.
We can create a listener to an uploaded reverse shell using `sudo nc -lnvp $443` (the port precised in the reverse shell file). 
Once netcat has been setup, our reverse shell will be able to connect back to this when activated !

Aaaaand here's our __flag__ !

![flag-time](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day02/flag-time.png)
