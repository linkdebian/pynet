# I. Create a script that does the following
#
#    A. Prompts the user to input an IP network.
#
#        Notes:
#        1. For simplicity the network is always assumed to be a /24 network
#
#        2. The network can be entered in using one of the following three formats 10.88.17.0, 10.88.17., or 10.88.17
#
#    B. Regardless of which of the three formats is used, store this IP network as a list in the following format ['10', '88', '17', '0'] i.e. a list with four octets (all strings), the last octet is always zero (a string).
#
#        Hint: There is a way you can accomplish this using a list slice.
#
#        Hint2: If you can't solve this question with a list slice, then try using the below if statement (note, we haven't discussed if/else conditionals yet; we will talk about them in the next class).
#
# >>>> CODE <<<<
#
#if len(octets) == 3:
#    octets.append('0')
#elif len(octets) == 4:
#    octets[3] = '0'
#
# >>>> END <<<<
#
#
#    C. Print the IP network out to the screen.
#
#    D. Print a table that looks like the following (columns 20 characters in width):
#
#      NETWORK_NUMBER   FIRST_OCTET_BINARY      FIRST_OCTET_HEX
#      88.19.107.0                    0b1011000                            0x58

ip_addr = raw_input ("Please enter a valid ip address: ")


ip_list = ip_addr.split(".")

# Get the fisrt third value.
ip_list = ip_list[:3]

# Add 0 value to the end.
ip_list.append("0")

#print ip_list

first_octet_binary = bin(int(ip_list[0]))
#print first_octet_binary

first_octet_hex = hex(int(ip_list[0]))
#print first_octet_hex

print "%-20s %-20s %-20s" % ("NETWORK_NUMBER", "FIRST_OCTET_BINARY", "FIRST_OCTET_HEX")
print "%-20s %-20s %-20s" % (ip_addr, first_octet_binary, first_octet_hex)


