# Day 01 - Web Exploitation

## Drop this cookie on the ground mthrfckr !

cookie are displayed on the 'inspect page'

Mix of numbers and a-f letters is hexadecimal. We can decode it using ```echo "a1e6b98cd" | xxd -r -p```.

This gives us : 

![cookie auth](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day01/decode16.png)

The format of the data is of JSON, thanks to ft_Services :-)

We can then change our username to santa's (no caps!), and encode it back into hexadecimal

Then we can change the auth cookie's value, which is for the moment mine, to santa's and refresh the page. Here we are, hohoho'ing with a big beard !

See you tomorrow kiddo's.
