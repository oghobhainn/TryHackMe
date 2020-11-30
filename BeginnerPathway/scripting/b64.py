#python3

import base64
crypted = open("b64.txt", "r")
line = crypted.read()
for i in range(50):
	line = base64.b64decode(line)
print(line)
	
