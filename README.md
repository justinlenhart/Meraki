This script generates the interface MAC addresses of a Meraki switch.

At the time of creation, there  isn't a way to get the interface MAC address of Meraki switches. There have been some use cases, such as E911, that require this information. 

You will need to modify the .env file to include your network ID and your API key.

The output is placed into a CSV file named Interface-MAC-Table.csv and a sample looks like this:

```
Switch Name,Model,Base MAC,Port 1,Port 2,Port 3,Port 4
Justin-Office,MS220-8P,88:15:44:de:09:f8,88:15:44:de:09:f9,88:15:44:de:09:fa,88:15:44:de:09:fb,88:15:44:de:09:fc
```

To get started with this script:
1. Install Python 3.X
2. Install devenv - pip3 install python-dotenv
3. Install Meraki SDK - https://developer.cisco.com/meraki/api/#/python/getting-started
4. Enable API access - https://developer.cisco.com/meraki/api/#/rest/guides/api-key
5. Put API key, org ID and network ID in .env file - https://developer.cisco.com/meraki/api/#/rest/guides/rest-api-quick-start/find-your-organization-id
