# 2. Create a second program that expands upon the program from exercise 1.
#
# This program will keep track of which network devices are physically adjacent to each other (physically connected to each other).
#
# You will accomplish this by adding a new field (adjacent_devices) to your network_devices inner dictionary.  adjacent_devices will be a list of hostnames that a given network device is physically connected to.
#
# For example, the dictionary entries for 'R1' and 'SW1' should look as follows:
#
# 'R1': {'IP': '10.1.1.1',
#         'adjacent_devices': ['SW1'],
#         'device_type': 'Router',
#         'model': '881',
#         'vendor': 'Cisco'},
#
#  'SW1': {'IP': '10.1.1.22',
#          'adjacent_devices': ['R1', 'R2', 'R3', 'R4', 'R5'],
#          'device_type': 'Switch',
#          'model': 'WS-C2950-24',
#          'vendor': 'cisco'},
#
#
#
# For the output to this exercise, print network_devices to standard output.  Your output should look similar to the following (six network devices with their associated attributes including 'adjacent_devices').
#
# {'R1': {'IP': '10.1.1.1',
#         'adjacent_devices': ['SW1'],
#         'device_type': 'Router',
#         'model': '881',
#         'vendor': 'Cisco'},
#  'R2': {'IP': '10.1.1.2',
#         'adjacent_devices': ['SW1'],
#         'device_type': 'Router',
#         'model': '881',
#         'vendor': 'Cisco'},
#  'R3': {'IP': '10.1.1.3',
#         'adjacent_devices': ['SW1'],
#         'device_type': 'Router',
#         'model': '881',
#         'vendor': 'Cisco'},
#  'R4': {'IP': '10.1.1.4',
#         'adjacent_devices': ['SW1'],
#         'device_type': 'Router',
#         'model': '881',
#         'vendor': 'Cisco'},
#  'R5': {'IP': '10.1.1.5',
#         'adjacent_devices': ['SW1'],
#         'device_type': 'Router',
#         'model': '881',
#         'vendor': 'Cisco'},
#  'SW1': {'IP': '10.1.1.22',
#          'adjacent_devices': ['R1', 'R2', 'R3', 'R4', 'R5'],
#          'device_type': 'Switch',
#          'model': 'WS-C2950-24',
#          'vendor': 'cisco'}}

