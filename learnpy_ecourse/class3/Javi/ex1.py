# I. Create an IP address converter (dotted decimal to binary).  This will be similar to what we did in class2 except:
#
#    A. Make the IP address a command-line argument instead of prompting the user for it.
#        ./binary_converter.py 10.88.17.23
#
#    B. Simplify the script logic by using the flow-control statements that we learned in this class.
#
#    C. Zero-pad the digits such that the binary output is always 8-binary digits long.  Strip off the leading '0b' characters.  For example,
#
#        OLD:     0b1010
#        NEW:    00001010
#
#    D. Print to standard output using a dotted binary format.  For example,
#
#        IP address          Binary
#      10.88.17.23        00001010.01011000.00010001.00010111
#
#
#    Note, you might need to use a 'while' loop and a 'break' statement for part C.
#
#        while True:
#            ...
#            break       # on some condition (exit the while loop)
#
#    Python will execute this loop again and again until the 'break' is encountered.

#!/usr/bin/env python

import sys

# create a blank list (needed because I use .append() method below)
binary = []

if len(sys.argv) == 2:
    ip_addr = sys.argv.pop()

else:
    print "You are made an error. Try to write 2 arguments"

octets = ip_addr.split(".")
print octets

if len(octets) == 4:
    for ip in octets:
        conversion = bin(int(ip))

        # Strip off "0b" string from octets
        conversion = conversion[2:]

        # Add 0s to reach 8 characters each string
        while True:
            if len(conversion) >= 8:
                break
            conversion = "0" + conversion
        binary.append(conversion)

else:
    print "You have entered invalid ip address %s" % (ip_addr)


octets_binary = '.'.join(binary)
#print octets_binary


print "%-20s %-20s" % ("IP address", "Binary")
print "%-20s %-20s" % (ip_addr, octets_binary)





