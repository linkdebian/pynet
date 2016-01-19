# IV. You have the following string from "show version" on a Cisco router
#
# cisco_ios = "Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)"
#
# Note, the string is a single line; there is no newline in the string.
#
# How would you process this string to retrieve only the IOS version:
#
#   ios_version = "15.0(1)M4"
#
#
# Try to make it generic (i.e. assume that the IOS version can change).
#
# You can assume that the commas divide this string into four sections and that the string will always have 'Cisco IOS Software', 'Version', and 'RELEASE SOFTWARE' in it.

cisco_ios = "Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)"


# Split string a get only position 2. In this case would be "Version 15.0(1)M4"
cisco_ios_list = cisco_ios.split(",")[2]
#print cisco_ios_list



#Split "Version 15.0(1)M4" with "Version " then we would have "Version " "15.0(1)M4". The number would be the second position [1]
#ios_version = cisco_ios_list.split("Version ")[1]
#Split "Version 15.0(1)M4" with space then we would have "Version" " " "15.0(1)M4". The number would be the third position [2]
ios_version = cisco_ios_list.split(" ")[2]

print ios_version


