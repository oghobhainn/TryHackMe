# Shut the F\**brrrrp*\*ck Up, Morty !

## Preparation

Just using the env variables to store the IP
```
export ip=$10.10.220.74
```

## Enumeration

I'm using nmap to see what ports are accessible.

![nmap](https://github.com/oghobhainn/TryHackMe/blob/main/images/rickmorty/nmap.png)

I see the ```80```port is accessible, an http website !
going on there, I first just learn that I don't know my username. Which I didn't even know I was looking or :-)

![website](https://github.com/oghobhainn/TryHackMe/blob/main/images/rickmorty/website.png)

When inspecting the element, I find this interesting comment

![username](https://github.com/oghobhainn/TryHackMe/blob/main/images/rickmorty/username.png)

Then that's about all, I need to know what hidden files/links/dir there might be !
First I think about using ```gobuster``` but it doesn't really work.
```
gobuster dir -u http://$ip/ -w /usr/share/wordlists/rockyou.txt
```
I picked the wordlist at random, and that's probably the mistake. There isn't even robots.txt in it, which is supposed to be basic.
So looking for other ways, I stumble upon ```dirsearch```, which I install.
And it took a few minutes, but that was exactly what I was looking for ! 

![dirsearch](https://github.com/oghobhainn/TryHackMe/blob/main/images/rickmorty/dirsearch.png)

First we look at the login.php
But we're missing a password (and not sure our username is correct)
Then we look at the robots.txt, and we find an interesting-password-looking string !

![robots.txt](https://github.com/oghobhainn/TryHackMe/blob/main/images/rickmorty/robots.txt.png)

Combining the 2, we reach a command panel

![command-panel](https://github.com/oghobhainn/TryHackMe/blob/main/images/rickmorty/command-panel.png)

It's a command panel, so we try running a basic ```ls```

![command-panel-ls](https://github.com/oghobhainn/TryHackMe/blob/main/images/rickmorty/command-panel-ls.png)

but we can't ```cat``` anything ...

![command-panel-error](https://github.com/oghobhainn/TryHackMe/blob/main/images/rickmorty/command-panel-cat.png)

but we can ```less```the files !

![command-panel-clue](https://github.com/oghobhainn/TryHackMe/blob/main/images/rickmorty/command-panel-less.png)

![command-panel-ingredient](https://github.com/oghobhainn/TryHackMe/blob/main/images/rickmorty/command-panel-ingredient.png)

*Here we have our first ingredient !*
