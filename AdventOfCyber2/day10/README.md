# Day10 - Don't be sElfish !

## using enum4Linux

located at `/root/Desktop/Tools/Miscellaneous`.

`./enum4linux.pl -a $ip` lists everything

To get the users : `./enum4linux.pl -U $ip`

![nc-listener](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day10/enum-users.png)

To get the shares (containing datas) : `./enum4Linux.pl -S $ip`

![nc-listener](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day10/enum-shares.png)

To connect to a share, we use the **smbclient tool** `smbclient //$ip/<sharename>`

![nc-listener](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day10/smbclient.png)

aaand that's kinda all for today !
