# Wonderland - It's getting curiouser and curiouser...

## Nmap

Let's scan the ports and see what's going on ...

![nmap](https://github.com/oghobhainn/TryHackMe/blob/main/images/wonderland/nmap.png)

`80` is open, it's probably a website !

![website](https://github.com/oghobhainn/TryHackMe/blob/main/images/wonderland/website.png)

Nice image, but nothing else to see. Let's __gobuster__ this to find hidden directories.

![gobuster](https://github.com/oghobhainn/TryHackMe/blob/main/images/wonderland/gobuster.png)

The `/img` dir only contains references for the first webpage.

The `/poem` dir has a nice poem, but gobuster indicates nothing else... and I see nothing special by inspecting it.

But in the `/r` dir, we find a subdir `/a` ! Then an subsubdir `/b`, `/b`, `/i`, `/t`..... and here we are !

![rabbithole](https://github.com/oghobhainn/TryHackMe/blob/main/images/wonderland/rabbithole.png)

And in the source code of the page, there's an interesting string : *alice:HowDothTheLittleCrocodileImproveHisShiningTail*. Could be a password ?

![rabbithole-sourcecode](https://github.com/oghobhainn/TryHackMe/blob/main/images/wonderland/rabbithole-sourcecode.png)


