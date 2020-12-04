# Day 03 - Christmas Chaos

## Burp Suite - a Rick's personnal fav

First we need to proxy our traffic through the *Burp Suite*, we can do that using this [tuto](https://portswigger.net/burp/documentation/desktop/getting-started/proxy-setup/browser) and __FoxyProxy__ (extension for web browser that allows up to easiliy route or traffic through it).

In the Burp Suite app, we can now click the proxy tab and toogle the button __Intercept is on__. BurpSuite is now helding the request until we forwad it on, so we __Forward__ it.

![proxy-toggle](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day03/proxy-toggle.png)

We then go to our favorite website (in this case, __$IP__). We fill the forms, and __Forward__ it to the BurpSuite. Then we right click on the interception, and send it to the intruder.

![fill-and-forward](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day03/fill-and-forward.png)
![intruder-tab1](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day03/intruder-tab1.png)

Then it'll appear on the intruder tab - __Burp Intruder__ is a tool to automate customize web attacks. We use it to loop through and submit a login request using a list of default credential, in the hopes that one of the usernames and passwords in the list is correct (for example, the rockyou.txt list).

![intruder-tab2](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day03/intruder-tab2.png)

We select the __Cluster bomb__ Attack Type; this attack type iterates through each payloads sets in turn, so every combination of each set is tested.
And we add the __username__ and __password__ values as positions, plus we select a list per position (telling Burp which field to update when automating a request).

![add-payload](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day03/add-payload.png)

Then we launch the attack and - tadah! - one of them sends a different result (not an error). That should be the one. It's possible to sort the results by these numbers.

![attack-results](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day03/attack-results.png)

Not forgetting to close the interception and turning off the Foxyproxy once Burpsuite has finished the attack !

![final-flag](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day03/final-flag.png)
