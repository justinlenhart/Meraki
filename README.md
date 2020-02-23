This script generates the interface MAC addresses of a Meraki switch.

At the time of creation, there  isn't a way to get the interface MAC address of Meraki switches. There have been some use cases, such as E911, that require this information. 

You will need to modify the .env file to include your network ID and your API key.

The output is placed into a CSV file named Interface-MAC-Table.csv and a sample looks like this:

`Switch Name,Model,Base MAC,Port 1,Port 2,Port 3,Port 4
Justin-Office,MS220-8P,88:15:44:de:09:f8,88:15:44:de:09:f9,88:15:44:de:09:fa,88:15:44:de:09:fb,88:15:44:de:09:fc`