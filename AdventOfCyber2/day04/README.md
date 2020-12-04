# Day04 - Santa's Watching

## Fuzzing - saying 'sorry' after beating someone

Here we're going to use __Gobuster__. It has 3 modes: `dir, vhost and dns`.
We'll use the `dir` with the classic `big.txt` wordlist, that we can find on kali at `/usr/share/wordlists/dirb/big.txt`. There are other wordlists interesting for specific situtations (the more a wordlist suits a situation, the more efficent it will be obviously).

The other tool is gonna be __Wfuzz__. Its purpose is to remplace any word on a given string by one one of our specified wordlist, and test if it works. For example : if we want to __fuzz__ an application on *https://shibes.thm/login.php*, we'd like it to guess the correct credentials for the login form. Let's guess the two parameters could be *username* and  *password* (kinda usual).
Our wfuzz command would be `wfuzz -c -z file,mywordlist.txt -d “username=FUZZ&password=FUZZ” -u http://shibes.thm/login.php` (*-c* to show colors, *-d* to specify the paramters we want to *fuzz*, *-z* to specify what to look for. Here we're looking for *files* coming from the *big.txt* wordlisti).

## Challenge

A special wordlist for the challenge is given at `/opt/AoC-2020/Day-4/wordlist`.

If we want to query the *breed* parameter at the URL `http://shibes.xyz/api.php` using the *big.txt* wordlist,
we use `wfuzz -c -z file,big.txt http://shibes.xyz/api.php?bree=FUZZ`.

We use __Gobuster__ to find the hidden api website.

![gobuster-api](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day04/gobuster-api.png)

and we __FUZZ__ the date to find our flag

![fuzz-date](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day04/fuzz-date.png)

And here's the flag we're looking for !

![flag](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day03/flag.png)

