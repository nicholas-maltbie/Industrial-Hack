import csv


def get_ips(ports):
    """This will get Ips that have given ports open.
    We would normally do this with shoden API but that involves paying money
    and we don't have money now. So we will just return IPs that the 
    program would return if it scanned the web."""
    
    return [] 

def get_ips_from_file(filename):
    """This will get Ips from a filename"""
    ipreader = csv.reader(open(filename, newline=''), delimiter=',', quotechar='"')
    ips = []
    for entry in ipreader:
        ips += entry
    return ips
