# Day 16 - Help ! Where's Santa ?

Today is about scripting again, but in a more practical way. 

First we have to see at what port is the website given (not the usual 80 or 443), by `nmap`ping it we find out there's an open port on `$ip:8000`. That's it !
There we have lot and lot links to check out, and we don't want to do this manually. We could check the source code to see where they're leadind us, but that's not the point of the day.
Let's use a script we've seen on the previous day ! not forgetting to install the libraries we need using `pip install <...>` 

```
python3 linkfinder.py | uniq
```
and we see the link we're looking for : `http://$ip/api/api_key`

Now we have to find the correct `$api_key`. It's and __odd number, between 0 and 100__. So let's brute these values :-).

There I made the mistake of not printing line by line but only the last time, so the defense mechanism has been activated...

![mistake](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day16/mistake.png)

but hopefully it didn't block us to get the answer we were looking for, `api_key number 57` !

![correct-api-key](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day16/correct-api-key.png)
