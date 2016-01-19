# III. You have the following four lines from 'show ip bgp':
#
# entry1 = "*  1.0.192.0/18   157.130.10.233        0 701 38040 9737 i"
# entry2 = "*  1.1.1.0/24       157.130.10.233        0 701 1299 15169 i"
# entry3 = "*  1.1.42.0/24     157.130.10.233        0 701 9505 17408 2.1465 i"
# entry4 = "*  1.0.192.0/19   157.130.10.233        0 701 6762 6762 6762 6762 38040 9737 i"
#
# Note, in each case the AS_PATH starts with '701'.
#
# Using split() and a list slice, how could you process each of these such that--for each entry, you return an ip_prefix and the AS_PATH (the ip_prefix should be a string; the AS_PATH should be a list):
#
# Your output should look like this:
#
# ip_prefix             as_path
# 1.0.192.0/18       ['701', '38040', '9737']
# 1.1.1.0/24           ['701', '1299', '15169']
# 1.1.42.0/24         ['701', '9505', '17408', '2.1465']
# 1.0.192.0/19       ['701', '6762', '6762', '6762', '6762', '38040', '9737']
#
# Ideally, your logic should be the same for each entry (I say this because once I teach you for loops, then I want to be able to process all of these in one four loop).
#
# If you can't figure this out using a list slice, you could also solve this using pop().

entry1 = "*  1.0.192.0/18   157.130.10.233        0 701 38040 9737 i"
entry2 = "*  1.1.1.0/24       157.130.10.233        0 701 1299 15169 i"
entry3 = "*  1.1.42.0/24     157.130.10.233        0 701 9505 17408 2.1465 i"
entry4 = "*  1.0.192.0/19   157.130.10.233        0 701 6762 6762 6762 6762 38040 9737 i"

prefix1 = entry1.split()
prefix2 = entry2.split()
prefix3 = entry3.split()
prefix4 = entry4.split()

ip_prefix1 = prefix1[1]
ip_prefix2 = prefix2[1]
ip_prefix3 = prefix3[1]
ip_prefix4 = prefix4[1]

# Add to list values from 4 position and exclude the last position. In this case We exclude "i"
as_path1 = prefix1[4:-1]
as_path2 = prefix2[4:-1]
as_path3 = prefix3[4:-1]
as_path4 = prefix4[4:-1]

print "%-20s %-20s" % ("ip_prefix", "as_path")
print "%-20s %-20s" % (ip_prefix1, as_path1)
print "%-20s %-20s" % (ip_prefix2, as_path2)
print "%-20s %-20s" % (ip_prefix3, as_path3)
print "%-20s %-20s" % (ip_prefix4, as_path4)






