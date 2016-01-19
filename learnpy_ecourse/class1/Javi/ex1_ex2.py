# Use the split method to divide the following IPv6 address into groups of 4 hex digits (i.e. split on the ":")
# FE80:0000:0000:0000:0101:A3EF:EE1E:1719
# Use the join method to reunite your split IPv6 address back to its original value.

ipv6 = "FE80:0000:0000:0000:0101:A3EF:EE1E:1719"

hex_digits = ipv6.split(":")

print hex_digits

original = ":".join(hex_digits)

print original

