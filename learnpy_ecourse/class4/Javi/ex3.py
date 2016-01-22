# III. Create a program that converts the following uptime strings to a time in seconds.

# uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
# uptime2 = '3750RJ uptime is 1 hour, 29 minutes'
# uptime3 = 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'
# uptime4 = 'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'

# For each of these strings store the uptime in a dictionary using the device name as the key.

# During this conversion process, you will have to convert strings to integers.  For these string to integer conversions use try/except to catch any string to integer conversion exceptions.

# For example:
# int('5') works fine
# int('5 years') generates a ValueError exception.

# Print the dictionary to standard output.

import pprint

MINUTE_SECONDS = 60
HOUR_SECONDS = 60 * MINUTE_SECONDS
DAY_SECONDS = 24 * HOUR_SECONDS
WEEK_SECONDS = 7 * DAY_SECONDS
YEAR_SECONDS = 365 * DAY_SECONDS

uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
uptime2 = '3750RJ uptime is 1 hour, 29 minutes'
uptime3 = 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'
uptime4 = 'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'

device = {}

for line in (uptime1, uptime2, uptime3, uptime4):
    uptime_time = line.split(",")
    (device_name, uptime_filed) = uptime_time[0].split(" uptime is")
    uptime_time[0] = uptime_filed
    #print uptime_time

    uptime_seconds = 0

    for line in uptime_time:

        if "years" in line:
            (years, junk) = line.split(" years")
            try:
                uptime_seconds += int(years) * 31536000
            except ValueError:
                print "Error conversion"

        elif "weeks" in line:
            (weeks, junk) = line.split(" weeks")
            try:
                uptime_seconds += int(weeks) * 604800
            except ValueError:
                print "Error conversion"

        elif "days" in line:
            (days, junk) = line.split(" days")
            try:
                uptime_seconds += int(days) * 86400
            except ValueError:
                print "Error conversion"

        elif "hours" in line:
            (hours, junk) = line.split(" hours")
            try:
                uptime_seconds += int(hours) * 3600
            except ValueError:
                print "Error conversion"

        elif "minutes" in line:
            (minutes, junk) = line.split(" minutes")
            try:
                uptime_seconds += int(minutes) * 60
            except ValueError:
                print "Error conversion"

        device[device_name] = uptime_seconds

pprint.pprint(device)

