#hello world
import os
from base64 import *
print("Time for a challenge ! Ready ? [y/n]")
crypted = open("encodedflag.txt", "r")
line = crypted.read()
i = 0
while i < 5:
	line = b16decode(line)
	i+=1
i = 0
while i < 5:
	line = b32decode(line)
	i += 1
i = 0
while i < 5:
	line = b64decode(line)
	i+=1
print(line)
