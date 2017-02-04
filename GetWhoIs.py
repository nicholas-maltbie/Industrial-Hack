"""This will use the Censys data to determine information concerning the 
owner of different ip addresses. This file requires a API ID and Secret from a
Censys account and these must be in a file 'censys' (no extension)."""
import censys
import json
import requests

def get_who_is(ip_address):
    """Finds the location (long, latt) of an ip_address using censys"""
    data = json.loads(open('censyskey', 'r').read())

    API_URL = "https://censys.io/ipv4/" + ip_address + "/rawwhois/_data"
    UID = data["API ID"]
    SECRET = data["Secret"]

    res = requests.get(API_URL, 
                        auth=(UID, SECRET))
    #if res.status_code == 200:
    #    content = res.content.decode('utf-8')
    #    loaded = json.loads(content)
    
    a = res.content.decode('utf-8').replace('\n', '').replace('&#34', '')
    a = a[a.index('{') : len(a) - a[::-1].index('}')]
    a = a.replace(';', '"')
    loaded = {}
    try:
        loaded = json.loads(a);
    except json.decoder.JSONDecodeError:
        print("Error loading JSON file");
    return loaded;

def get_contacts(whois_data):
    """parse all dictionaries that are mapped by the word 'contact'"""
    found = []
    for key in whois_data:
        if key == "contact":
            found.append(whois_data[key])
        elif type(whois_data[key]) == dict:
            found.extend(get_contacts(whois_data[key]))
    return found

def get_all_data(ip_address):
    """Given an ip address, this will search for all whois information tied to 
    this address."""
    a = get_who_is(ip_address)
    if a != None:
        a = get_contacts(a)
    return a
    
