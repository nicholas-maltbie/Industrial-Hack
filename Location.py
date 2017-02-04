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
        
def find_location2(ip_address):
    """Finds the location (long, latt) of an ip_address using censys"""
    data = json.loads(open('censyskey', 'r').read())

    API_URL = "https://www.censys.io/api/v1/search/certificates"
    UID = data["API ID"]
    SECRET = data["Secret"]

    res = requests.post(API_URL, 
                        data= {
                                "query":"80.http.get.headers.server:Apache",
                                "page":2,
                                "fields":["ip", "location.country", "autonomous_system.asn"]
                                },
                        auth=(UID, SECRET))
    return res
    #if res.status_code == 200:
    #    content = res.content.decode('utf-8')
    #    loaded = json.loads(content)
    #    return loaded['location']['longitude'], loaded['location']['latitude']
   #
   #https://censys.io/ipv4?q=location.country_code%3A+DE+and+protocols%3A+%28%2223%2Ftelnet%22+or+%2221%2Fftp%22%29
        
def group_by_location(ip_addresses):
    """Takes a group of ips and returns a dictionary with a key values of 
    location each with entires of a list of ips at that location"""
    groups = {}
    for address in ip_addresses:
        loc = find_location(address)
        if loc in groups:
            groups[loc].append(address)
        else:
            groups[loc] = [address]
    return groups
    
