from meraki_sdk.meraki_sdk_client import MerakiSdkClient
from meraki_sdk.exceptions.api_exception import APIException
import json
import csv
import re
from dotenv import load_dotenv
import os

load_dotenv()

def mac_reverse(m_r):
    m_r = m_r[::-1]
    return m_r

def mac_to_int(m_i):
    for x in range(0,6):
        m_i[x] = int(m_i[x], base=16)
    return m_i

def mac_combine(m_c):
    mac_str = ''
    for x in range(0,6):
        mac_str += m_c[x]
        if x < 5:
            mac_str += ':'
    return mac_str
    
def increment_mac(mac, switch_model):
    if switch_model == 'MS22' or switch_model == 'MS42' or switch_model == 'MS42P':
        if switch_model == 'MS22':
            num_ports = int(re.sub('[^0-9]','', switch_model))
            num_ports = num_ports + 2
        if switch_model == 'MS42':
            num_ports = int(re.sub('[^0-9]','', switch_model))
            num_ports += 6
        if switch_model == 'MS42P':
            temp = []
            temp = re.findall('[0-9]+', switch_model)
            num_ports = int(temp[0]) 
            num_ports += 6
    else:
        # split model into list - example 'MS350' , '24P'
        x = switch_model.split('-')
        # use regex to export only numbers in sequence 1
        #num_ports = re.sub('[^0-9]','', x[1])
        temp = []
        temp = re.findall('[0-9]+', x[1])
        num_ports = int(temp[0])
    # split mac to list
    mac_split = mac.split(':')
    # convert sequences to ints
    mac_list = []
    for x in range(0,int(num_ports)):
        mac_split = mac_to_int(mac_split)
        # reverse mac list
        mac_split = mac_reverse(mac_split)
        for i in range(0,6):
            if mac_split[i] < 255:
                mac_split[i] += 1
                break
            else:
                mac_split[i] = 0
        for i in range(0,6):
            mac_split[i] = f'{mac_split[i]:02x}'
        mac_split = mac_reverse(mac_split)
        mac_list.append(mac_combine(mac_split))
    return mac_list

#Open CSV file for writing
interface_mac_table = open('Interface-MAC-Table.csv', 'w')
csvwriter = csv.writer(interface_mac_table)

#Create header for CSV file
mac_header = ['Switch Name', 'Model', 'Base MAC']
for x in range(1,49):
    mac_header.append(f'Port {x}')

#Write header
csvwriter.writerow(mac_header)

# comment to search network only
org_id = {}
org_id['organization_id'] = os.getenv('organization_id')

# uncomment to search network only
#network_id = os.getenv('network_id')
x_cisco_meraki_api_key = os.getenv('api_key')

client = MerakiSdkClient(x_cisco_meraki_api_key)
devices_controller = client.devices

try:
    #Gets devices for a specific network
    #result = devices_controller.get_network_devices(network_id)
    # if you want only switches in a network, comment line below and uncomment above line
    result = devices_controller.get_organization_devices(org_id)
    for d in result:
        model = d['model']
        if model.startswith('MS'):
            row = []
            base_mac = d['mac']
            row.append(d['name'])
            row.append(model)
            row.append(base_mac)
            row += increment_mac(base_mac, model)
            csvwriter.writerow(row)
except APIException as e: 
    print(e)

interface_mac_table.close()
