# Nmap - a bright torch in a dark room

Every computer has a total of 65535 available ports, many registered as standard ports (80 for HTTP, 443 for HTTPS...).
*Nmap* will connect to each port of the target in turn. Depending how the port responds, it can be determined as being open, closed or filtered (firewall). Once we know which ports are open, we can then look at enumerating which services are running on each port.

FLAGS :
```
-sS		SYN scan is the default option
-sU		UDP scan
-o		enables OS detection
-sV		service version detection
-v		verbosity flag
-vv		very verbose /!\ALWAYS PUT THIS ONE/!\
-A		AGGRESSIVE scan, no matter how loud you are
-T[0-5]	paranoid, sneaky, polite, normal, agressive or insane timing. Paranoid et Sneaky évitent les IDS (Intrusion Detection System), 'polite' prend moins de bande passante, 'Agressive' accélère les scans, 'Insane' suppose que le réseau est ultra rapide et que plus de vitesse vaut moins de précision.
-p		scans a specific range of ports (0-1000 for ex, can also be a single port)
-p-		scans all ports
-Pn		to not ping the host
--script vuln	scans for any vulnerabilities
```
It's very useful to save the result of the scan in a file, so that we only need to run it once. This reduces network traffic and thus chance of detection + a reference to give to clients.
```
-oA		major format
-oN		normal format
-oG		grepabale format
```

There are 3 basic scan types:
```
-sT		TCP Connect Scans
-sS		Syn "Half-Open" Scans"
-uU		UDP Scans
```

The NSE - Nmap Scripting Engine - extends the functionnalities by a lot.
We can use them with the ```--script=<NSE>``` flag. Some of them : 
```
safe		won't affect the target
intrusive	Not-safe : likely to affect the target
vuln		Scan for vulnerabilities
exploit		Attempt to exploit a vulnerability
auth		Attempts to bypass authentification for running services
brute		attempts to bruteforce credentials for running services
discovery	attempts to query running services for further information about the network
```
To have more informations on a specific script, we can type ```nmap --script-help <script-name>``` or [here](https://nmap.org/nsedoc/) is a full list of scripts and their arguments.
