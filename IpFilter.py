"""This module will be reponsible for filtering owners and extra informaiton 
from a list of contact information from the GetWhoIs module."""
import GetWhoIs

def get_all_owner_info(addresses):
    """Give this a list of addresses, this will find all the owner information 
    accross the different addresses."""
    return {address:GetWhoIs.get_add_data(address) for address in addresses}
    
