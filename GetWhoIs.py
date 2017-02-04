"""This will use the Censys data to determine information concerning the 
owner of different ip addresses"""
import censys
import json
import requests

def get_who_is(ip_address):
    """Finds the location (long, latt) of an ip_address using censys"""
    data = json.loads(open('censyskey', 'r').read())

    API_URL = "https://censys.io/ipv4/166.251.70.56/rawwhois/_data"
    UID = data["API ID"]
    SECRET = data["Secret"]

    res = requests.get(API_URL, 
                        auth=(UID, SECRET))
    #if res.status_code == 200:
    #    content = res.content.decode('utf-8')
    #    loaded = json.loads(content)
    return res;
        
