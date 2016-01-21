# I. Prompt a user to input an IP address.  Re-using some of the code from class3, exercise4--determine if the IP address is valid.
# Continue prompting the user to re-input an IP address until a valid IP address is input.

while True:

    try:

        ip_addr = raw_input("Enter a IP Address: ")

        ip_addr2 = ip_addr.split(".")

        ip_address = []


        for i in ip_addr2:
            integer = int(i)
            ip_address.append(integer)



        if len(ip_address) != 4:
            print "IP address is invalid. IP address must have 4 octets"

        if ip_address[0] > 223:
            print "IP address is invalid. Firts octet must be between 1 - 223"

        elif ip_address[0] == 127:
            print "IP address is invalid. Firts octet cannot be 127"

        elif ip_address[0] == 169 and ip_address[1] == 254:
            print "The IP address cannot be in the 169.254.X.X address space."

        elif ip_address[1] > 255:
            print "The second octet must range between 0 - 255."

        elif ip_address[2] > 255:
            print "The third octet must range between 0 - 255."

        elif ip_address[3] > 255:
            print "The fourh octet must range between 0 - 255."

        else:
            break

    except IndexError as e:
        print "------------------------------------------"
        print str(e)
        print "------------------------------------------"
        print "The Ip Address is icomplete. Please write correct IP"

    except ValueError as e:
        print "------------------------------------------"
        print str(e)
        print "------------------------------------------"
        print "The Ip Address is icomplete. Please write correct IP"

print "IP address is valid: %s" % ip_addr