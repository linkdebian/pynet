# >>>>> CODE (file test3.py) <<<<<

# !/usr/bin/env python
# import fileinput

# for line in fileinput.input():
#    print line.split(".")

# >>>>> END <<<<<

# Here is an example using this script where I echo an IP address into it and then the IP address is split into its octets.

# $ echo '192.168.1.1'  | ./test3.py
# ['192', '168', '1', '1\n']

# In the test3.py script above, how would you modify this to remove the trailing newline on the end of 192.168.1.1?


import fileinput

for line in fileinput.input():
    line = fileinput.strip()
    print line.split(".")

