"""This module will be reponsible for filtering owners and extra informaiton 
from a list of contact information from the GetWhoIs module."""
import GetWhoIs

default_blacklist = ['wirelessdataspco.org']

def get_all_owner_info(addresses):
    """Give this a list of addresses, this will find all the owner information 
    accross the different addresses."""
    return {address:GetWhoIs.get_all_data(address) for address in addresses}
    
def filter_blacklist_email_domains(owner_info, blacklist):
    """Given a dict of address : list of get_all_data, this will remove all 
    addresses where the domain of the 'email' field is in the blacklist"""
    for addr in owner_info:
        contacts = owner_info[addr]
        for contact in contacts[:]:
            marked = False
            for domain in blacklist:
                emails = contact['email']
                if emails:
                    for email in emails:
                        if email['value'].endswith(domain):
                            marked = True
            if marked:
                contacts.remove(contact)
    return owner_info
    
