# II. Create an IP address converter (dotted decimal to binary):
#
#    A. Prompt a user for an IP address in dotted decimal format.
#
#    B. Convert this IP address to binary and display the binary result on the screen (a binary string for each octet).
#
#    Example output:
#    first_octet    second_octet     third_octet    fourth_octet
#    0b1010        0b1011000        0b1010         0b10011

ip_addr = raw_input ("Please enter a valid ip address: ")

# Split ip address in octects a create a list
ip_list = ip_addr.split(".")

# Convert calues from the list to integers and convert to binary
first_octet_binary = bin(int(ip_list[0]))
second_octet_binary = bin(int(ip_list[1]))
third_octet_binary = bin(int(ip_list[2]))
fourth_octet_binary = bin(int(ip_list[3]))


# print values align to the left in columns
print "%-20s %-20s %-20s %-20s" % ("first_octet", "second_octet", "third_octet", "fourth_octet")
print "%-20s %-20s %-20s %-20s" % (first_octet_binary, second_octet_binary, third_octet_binary, fourth_octet_binary)