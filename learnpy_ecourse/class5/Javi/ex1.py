# 1. Parse the CDP data (see link above) to obtain the following information: hostname, ip, model, vendor, and device_type (device_type will be either 'router', 'switch', or 'unknown').
#
# From this data create a dictionary of all the network devices.
#
# The network_devices dictionary should have the following format:
#
# network_devices = {
#      'SW1': { 'ip': '10.1.1.22', 'model': 'WS-C2950-24', 'vendor': 'cisco', 'device_type': 'switch' },
#      'R1': { 'ip': '10.1.1.1', 'model': '881', 'vendor': 'Cisco', 'device_type': 'router' },
#       ...
#      'R5': { 'ip': '10.1.1.1', 'model': '881', 'vendor': 'Cisco', 'device_type': 'router' },
#  }
#
# Note, this data structure is a dictionary that contains additional dictionaries.  The key to the outer dictionary is a hostname and the data corresponding to this key is another dictionary.  For example, for 'R1':
#
# >>> network_devices['R1']
# {'ip': '10.1.1.1', 'model': '881', 'vendor': 'Cisco', 'device_type': 'router'}
#
# You can access a given attribute in the inner dictionary as follows:
# >>> a_dict['R1']['ip']
# '10.1.1.1'
#
#
# If this is confusing, you might want to experiment with it in the Python shell:
#
# ##### Python Shell - experimenting with dictionary of dictionaries #####
#
# # Initialize network_devices to be a blank dictionary
# >>> network_devices = {}
#
# # Assign the key 'R1' to network_devices using a value of a blank dictionary (in other words, I am adding a key:value pair to network_devices where the key is 'R1' and the value is {} )
# >>> network_devices['R1'] = {}
#
# # Look at network_devices at this point
# >>> network_devices
# {'R1': {}}
#
# # Add the 'ip' and 'vendor' fields to the inner dictionary
# >>> network_devices['R1']['ip'] = '10.1.1.1'
# >>> network_devices['R1']['vendor'] = 'Cisco'
# >>> network_devices
# {'R1': {'ip': '10.1.1.1', 'vendor': 'Cisco'}}
#
# ##### Python Shell - experimenting end #####
#
#
# For the output to this exercise, print network_devices to standard output.  Your output should look similar to the following (six network devices with their associated attributes).
#
# {'R1': {'device_type': 'Router',
#         'ip': '10.1.1.1',
#         'model': '881',
#         'vendor': 'Cisco'},
#  'R2': {'device_type': 'Router',
#         'ip': '10.1.1.2',
#         'model': '881',
#         'vendor': 'Cisco'},
#  'R3': {'device_type': 'Router',
#         'ip': '10.1.1.3',
#         'model': '881',
#         'vendor': 'Cisco'},
#  'R4': {'device_type': 'Router',
#         'ip': '10.1.1.4',
#         'model': '881',
#         'vendor': 'Cisco'},
#  'R5': {'device_type': 'Router',
#         'ip': '10.1.1.5',
#         'model': '881',
#         'vendor': 'Cisco'},
#  'SW1': {'device_type': 'Switch',
#          'ip': '10.1.1.22',
#          'model': 'WS-C2950-24',
#          'vendor': 'cisco'}}

