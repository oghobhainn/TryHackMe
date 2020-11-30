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
-vv		very verbose
-A		AGGRESSIVE scan, no matter how loud you are
-T[0-5]	paranoid, sneaky, polite, normal, agressive or insane timing. Paranoid et Sneaky évitent les IDS (Intrusion Detection System), 'polite' prend moins de bande passante, 'Agressive' accélère les scans, 'Insane' suppose que le réseau est ultra rapide et que plus de vitesse vaut moins de précision.
-p		scans a specific range of ports (0-1000 for ex, can also be a single port)
-p-		scans all ports
-Pn		to not ping the host
--script vuln	scans for any vulnerabilities
```
