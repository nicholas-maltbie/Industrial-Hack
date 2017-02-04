"""This will use the Censys data to determine information concerning the 
owner of different ip addresses"""
import censys
import json
import requests

def find_location(ip_address):
    """Finds the location (long, latt) of an ip_address using censys"""
    data = json.loads(open('censyskey', 'r').read())

    API_URL = "https://www.censys.io/api/v1"
    UID = data["API ID"]
    SECRET = data["Secret"]

    res = requests.get(API_URL + "/view/ipv4/" + ip_address, 
                        auth=(UID, SECRET))
    if res.status_code == 200:
        content = res.content.decode('utf-8')
        loaded = json.loads(content)
        return loaded['location']['longitude'], loaded['location']['latitude']
    
